# Driving the Ozon supply-request UI

Ozon's "Заявка на поставку" (`seller.ozon.ru/app/supply/orders/multi-cluster/<id>`)
is a heavy React app with a few sharp edges. This doc exists because a session
lost real progress twice to these before figuring them out — read it first.

## The single biggest risk: unsaved state

Adding items in the "Товары для кластера <X>" modal is **not saved until you
click "Сохранить"**. Navigating, reloading, or even just closing the modal
without saving discards everything you added in that session — silently, with
no warning dialog. If you've just added 30 items and are about to do something
risky (fix a rendering glitch, switch clusters, take a long detour), **save
first**, even with quantities still at 0. Saved-but-zero is fully recoverable;
unsaved is not.

Corollary: don't `navigate()` to "refresh" the page as a fix for a rendering
problem while a modal has unsaved edits. Screenshot first, confirm what state
you're in, save if there's anything worth keeping, and only then reload.

## Rendering/viewport instability

The page intermittently renders at a tiny effective scale (contents crammed into
the top-left ~35% of the viewport) after a sequence of clicks. When this
happens, pixel-coordinate clicks silently land on the wrong element — including,
critically, on checkboxes for *other* Ozon clusters/warehouses elsewhere on the
page, which can select things the user never asked for.

- Symptom to watch for: a screenshot where table rows look compressed into a
  fraction of the image with lots of blank space around them.
- Fix that reliably works: `navigate()` to the same URL again (full reload)
  — but only after saving anything worth keeping — or `resize_window()`.
  A plain re-screenshot after waiting is not reliable.
- After any batch of coordinate-based clicks, take a verification screenshot
  before doing the next batch. Don't chain many blind coordinate clicks back to
  back when the page has been visibly unstable.

**Prefer `find` + `form_input`/click-by-ref over pixel coordinates** whenever a
recognizable label or placeholder text is available (e.g. the quantity search
box, a named cluster row). This sidesteps the scale problem entirely — an
accessibility-tree ref points at the actual element regardless of how it's
currently laid out on screen. `find` is slower per-call than a coordinate click
but far more reliable when the page has been misbehaving.

## The "Товары в заявке" search-and-add flow

1. Click the "N SKU, M шт" link in the cluster's row to open its item modal.
2. Make sure you're on the **"Товары в заявке"** tab, not "Рекомендация Ozon" —
   they look similar but the second one is a totally different bulk-add UI with
   its own checkbox-based flow. Search only works usefully on the first tab.
3. Type the exact seller article into the search box. One of two things happens:
   - A single matching result appears with an "Добавить все найденные" link —
     click it to add.
   - "По вашему запросу ничего не найдено" — **this SKU does not exist as a
     product card in Ozon's catalog.** Don't retry with slight spelling
     variations hoping to find it; report it to the user as needing a new
     product card. This is exactly the situation that produces SKUs with no
     Export/order history — the two symptoms have the same root cause.
4. Newly-added items default to **quantity 0** with a warning icon. There is no
   bulk quantity-set — each one needs its input field located and edited
   individually. This is the slow part; budget for it and consider batching in
   groups of 5-10 with a save after each group rather than adding everything
   and setting all quantities at the end (so a mistake only costs one group).
5. Click **"Сохранить"** before moving to another cluster or navigating away.

## Toggling "Единая отгрузка" (unified shipment point) across many clusters

Each cluster row has a toggle in the "Отгрузить в общей точке" column. Turning
one on **re-sorts the table** — toggled-on rows jump to the top, and everything
below shifts up by one row height. Practical consequence: don't pre-compute a
list of y-coordinates for all rows and click through them — after the first
click the second one is now aimed at the wrong row.

What works: click the **first still-off row** (always visually just below the
last toggled-on row), take a screenshot to see what shifted, click the new
first-off row, repeat. It's a few extra screenshots but avoids toggling the
wrong warehouse.

## File upload is not available

The `file_upload` tool in this environment does not accept host filesystem
paths — there is no way to script Ozon's "Загрузить через файл" bulk-import
button (drag-and-drop file picker) in this session. If bulk file upload seems
like the efficient path, it isn't currently available; fall back to the
search-and-add flow above, and tell the user file upload isn't scriptable
right now if they ask about it.

This applies to the drag-and-drop widgets specifically. The downloadable Excel
bulk-import *templates* (see "Creating a missing product card" below) are a
different mechanism — Claude can fill those in directly with openpyxl and hand
the finished file back to the user to upload themselves, which sidesteps the
tool limitation for that one step.

## Finding "Добавить все найденные" reliably

The `find` tool's returned ref for this button is unreliable — clicking it by
ref has, more than once, opened a new blank tab instead of adding the item
(likely because the accessibility tree resolves an overlapping/nested link
element rather than the actual button). Coordinate-based clicking works
consistently instead:

1. Click the search box, `ctrl+a` to select any existing text, type the exact
   article.
2. Take one screenshot (or `find` just to confirm "Найден N товар(ов)"
   appeared) to read off the pixel position of "Добавить все найденные" —
   it's a fixed offset from the search box, typically ~15-35px below and
   right-aligned in the dropdown, e.g. around `(824, 91)` when the search box
   itself is at `(670, 59)`. The exact numbers depend on modal position/zoom,
   so recheck it once per modal-open rather than assuming it's identical to a
   previous session.
3. Click that coordinate. Verify the SKU count in the "Всего N SKU" header
   incremented by 1 before moving to the next article — if it didn't, the
   click missed and needs retrying.

Once confirmed for a given modal, the same coordinate works for many
consecutive searches in that same modal (search box position doesn't move),
so a batch of `click box → ctrl+a → type → wait → click add` can be chained
via `browser_batch` for several articles at once — just re-verify the
coordinate after any scroll, resize, or reopen of the modal.

## Reconciling a live supply request against expected data

When the user provides "this is what should be in each warehouse" files
(e.g. one file per cluster) and asks to verify the live Ozon draft matches:

1. **Don't try to scrape full per-article lists from the UI as the primary
   method** — Ozon's item tables inside modals are virtualized (only ~15-20
   rows exist in the DOM at once), so `read_page`/`find` only sees whatever
   happens to be scrolled into view. Scrolling through a 90-row modal via
   screenshots to extract every row is slow and error-prone.
2. Instead, get the **per-cluster totals** first — `get_page_text` on the
   main supply-request page (not a modal) reliably returns every cluster's
   "N Товаров / M Штук / L Литров" in one call, since that list isn't
   virtualized the same way. Compare each cluster's total against the sum of
   your expected file for that warehouse. This instantly tells you which
   clusters are short and by how much, with zero scrolling.
3. **Use the quantity gap to identify *which* articles are missing before
   touching the UI.** If several clusters are all short by the same amount,
   and that amount equals the sum of a known subset of SKUs (e.g. "9 articles
   × 5 units = 45"), that's very likely exactly those SKUs missing — confirm
   with a couple of `find` searches rather than a full row-by-row scrape. A
   cluster whose gap doesn't fit a known pattern (like a lone "-37" among a
   run of "-45"s) is a flag to investigate separately rather than assume it's
   the same cause.
4. `get_page_text` reads from `<main>` and will **not** see modal content —
   modals are rendered in a separate DOM subtree (portal). Once a modal is
   open, use `read_page` (filter `all`) or targeted `find` calls instead.

## Creating a missing product card (no existing Ozon listing at all)

If a SKU search inside the supply-request modal returns "ничего не найдено",
the product doesn't exist in Ozon's catalog yet and no amount of retrying the
supply-request search will fix it — a product card has to be created first.
Two ways to help with this that don't require uploading files through the
browser:

**A. "Скопировать готовые товары" (copy an existing card as a template).**
Under Товары → Добавить товары → "Скопировать готовые товары", the seller can
search the *entire* Ozon catalog (any seller) for a similar product, add it as
a base, then override every field (barcode, article, color, price) on the
next step. This is fast for a one-off but photos still don't carry over
automatically — the "Добавление медиа" dialog only accepts drag-and-drop
files or a **Яндекс.Диск** link, not arbitrary photo URLs, so this path still
needs the user to supply images themselves (or use path B below).

**B. Fill the official bulk-import Excel template with openpyxl.** Товары →
Добавить товары → Через шаблон → pick the category → download the category's
template. Unlike the in-browser "Добавление медиа" dialog, the *template's*
"Ссылка на главное фото" / "Ссылки на дополнительные фото" columns accept
**any** direct image URL (confirmed working with `wbbasket.ru` — i.e. photos
already hosted on Wildberries for a seller's existing WB listings can be
reused as-is for the new Ozon card). This is the practical way to get photos
attached without ever needing a real file upload:
  - Fill Артикул, Название, Цвет, Бренд, package dimensions, and the photo
    URL columns from whatever source data is available (e.g. a WB product
    export for the same SKU family).
  - Leave fields you have no reliable source for — Цена, НДС, ТН ВЭД code,
    net weight — genuinely blank rather than guessing; these carry real
    financial/customs consequences and the user needs to fill them in. Say
    so explicitly rather than inventing plausible-looking values.
  - Hand the filled `.xlsx` back to the user to upload themselves (the file
    upload UI, unlike the URL-photo fields, isn't scriptable here).
  - Sibling colors/sizes of an existing product family are a good source for
    fields the primary data export doesn't have (e.g. package
    height/width/length are usually identical across colors of the same
    model) — but always prefer asking the user over silently inferring
    things like price or tax rate.

## Recovering from a dropped browser connection mid-task

The Chrome extension connection can drop mid-batch (mid-`browser_batch`, even).
When it does, the in-progress action may or may not have completed — check
state before assuming either way once reconnected. Don't retry a whole batch
blindly, since some earlier steps in it may have already landed. On
reconnection, re-verify current counts (SKU totals, quantities) against what
was expected *before* resuming, the same way as the reconciliation section
above, rather than assuming picking up where the batch left off is safe.
