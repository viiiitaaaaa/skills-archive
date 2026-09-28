---
name: warehouse-supply-allocation
description: Distribute a marketplace supply shipment (Wildberries or Ozon) across multiple fulfillment warehouses, and optionally push the result into an Ozon seller-account supply request via the browser. Use this whenever the user has a shipment quantity per SKU (often an "Export" or "Заказы" sheet with per-warehouse order/recommendation counts) and asks to split it across warehouses/clusters/склады, apply a minimum-quantity-per-warehouse cutoff, exclude weak warehouses, or fill in an Ozon/WB "заявка на поставку". Trigger on phrases like "распредели поставку по складам", "раскладка по кластерам", "сколько отгружать на каждый склад", or when the user uploads an Export sheet plus a shipment-quantity sheet and wants warehouse columns filled in.
---

# Warehouse Supply Allocation

Splits a shipment of SKUs across multiple warehouses (Wildberries "направления" or
Ozon "кластеры") in proportion to each warehouse's share of demand, while respecting
a minimum viable shipment size per warehouse. Optionally drives the Ozon seller
web UI to add the missing items to a live supply request ("заявка на поставку").

## Why this exists

Splitting a shipment strictly proportional to demand produces silly results: a
warehouse with 1% of demand gets 1% of a 400-unit shipment, i.e. 4 units — not
worth a separate delivery. The core trick is a **minimum-quantity cutoff**:
warehouses that would receive less than the minimum are dropped, and their share is
redistributed among the remaining warehouses. This mirrors how an experienced ops
person would actually plan a shipment.

There are two variants of the cutoff, and getting this distinction right matters —
confirm which one the user means before computing anything, since they produce very
different results:

1. **Per-SKU cutoff**: for a single article, if a warehouse's share works out to
   less than N units, drop it *for that article only* and redistribute among the
   other warehouses handling that article.
2. **Whole-shipment cutoff** (usually what's wanted): sum a warehouse's allocation
   across *every* SKU in the shipment. Only drop the warehouse from the *entire*
   shipment if that total is below N. This avoids the absurd outcome of shipping to
   15 warehouses with 5 units each spread across dozens of articles.

If it's ambiguous which one the user wants, ask — don't guess. Getting this wrong
means redoing every SKU.

## Step 1: Understand the inputs

You'll typically receive two kinds of sheets:

- **Export / Заказы**: one row per SKU-warehouse-region combination (or one row per
  SKU with a column per warehouse) giving order counts or "Рекомендуется к
  поставке" — this is the *weight* used to proportion the split. Match SKUs by
  seller article code (Артикул продавца / Артикул поставщика), not by name — names
  truncate and collide.
- **Shipment sheet**: one row per SKU with the quantity arriving *today* that needs
  to be split. Watch for a trailing "итого"/total row with no article — exclude it,
  or you will silently double-count the shipment total. Always sanity-check: sum
  the quantity column and confirm it against what the user told you the shipment
  size is before doing anything else.

Also watch for formulas that reference an external, closed workbook (e.g.
`='[2]Ремешки ОЗ'!...`). openpyxl loads these as formula strings with no value when
opened `data_only=False`, and **re-saving that workbook silently drops the cached
result**, corrupting rows you never intended to touch. Before writing anything
back, bake every formula cell to its last-known value:

```python
for row in ws.iter_rows():
    for cell in row:
        if isinstance(cell.value, str) and cell.value.startswith("="):
            cell.value = ws_data_only.cell(row=cell.row, column=cell.column).value
```

## Step 2: Confirm the rules before computing

Before running anything at scale, nail down with the user (a couple of quick
questions beats redoing 80 rows three times):

- Which cutoff variant (per-SKU or whole-shipment), and what's N?
- Rounding step (usually 5 units for apparel/accessories — check what the source
  sheets already use).
- Any special-case combining of warehouse columns (e.g. two small regions get
  routed through one shared warehouse — sum their weight columns together).
- If a warehouse ends up with 0 in a small-quantity edge case where not everyone
  can clear the minimum (e.g. 15 units across 4 warehouses, minimum 5 each) — is
  that acceptable, or should it fall back to concentrating in the top warehouses by
  weight?
- **Always verify the result on one or two example SKUs by hand with the user**
  before running the full sheet. It's much cheaper to catch a misunderstood rule on
  one row than on eighty.

## Step 3: Run the allocation

`scripts/allocate.py` implements the whole-shipment-cutoff variant with
largest-remainder rounding (so warehouse totals always sum exactly to the SKU
quantity — no rounding drift). Read it before adapting: `allocate_shipment()` is
the pure algorithm (no Excel I/O, easy to unit-test against a hand-worked example),
`process_workbook()` is the Excel plumbing. Copy/adjust the `__main__` block's
column mappings for the actual file layout rather than guessing new logic from
scratch — the hard part (rounding, redistribution, formula-baking) is already
solved there.

For the per-SKU-cutoff variant, drop the two-pass structure (whole-shipment totals
+ redistribution) and just run `largest_remainder_round` per SKU directly against
warehouses above the per-SKU threshold.

After running, always verify:
- Sum of all warehouse columns equals the shipment quantity, per row (not just in
  aggregate — aggregate matches can hide row-level errors that cancel out).
- No warehouse below the agreed minimum, except explicitly-approved edge cases.
- Spot-check 2-3 rows against what you and the user hand-verified in Step 2.

## Step 4 (optional): Pushing results into Ozon's live supply request

If the user wants the numbers reflected in an actual Ozon seller-account draft
("заявка на поставку", `seller.ozon.ru/app/supply/orders/...`), see
`references/ozon-browser-workflow.md` before starting. The Ozon supply UI has
several sharp edges (unsaved-state loss on navigation, viewport rendering glitches,
no bulk quantity edit) that are easy to lose a lot of work to if you don't know
about them going in.

Before adding any SKU that doesn't already appear in the export/recommendation
data, **check that it actually exists as a product card in Ozon's catalog first**
(search for it in the "Товары в заявке" search box). A SKU with no order/
recommendation history is often a SKU that was never created as a real product —
no amount of retrying the add will work, and the right next step is telling the
user which articles need a product card created, not continuing to fight the UI.
