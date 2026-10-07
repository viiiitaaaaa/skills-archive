---
name: noted-news
description: "Память «принято к сведению» из Telegram-новостей — 96 уроков и инструментов, которые она отметила с панели (экономика товара, реклама, платежи, страны, данные, лимиты Claude, инструменты «когда будет время»). Используй, когда просят «что мы приняли к сведению», «что было в новостях про …», «напомни уроки из новостей», «что я отмечала», перед решениями по рекламе, ценам, платежам, доставке, новой стране, установке инструментов, и при разборе новостей — чтобы не показывать повторно уже принятое. Триггеры: \"принято к сведению\", \"что я отмечала\", \"напомни из новостей\", \"принятые новости\", \"память новостей\"."
---

# Принято к сведению из новостей (память)

Её правило 07.10: принятые к сведению новости **на панель новостей не выводятся** — хранятся здесь. На панели только
новые, ещё не принятые и не прочитанные.

- Этот файл и `принятое.md` (полный текст карточек) **пересобираются скриптом** `C:\Users\User\tg_monitor\noted_to_skill.py`
  из `notes.json` (пометка `noted`, группа `when`). Руками не править — править заметку в notes.json и перезапустить.
- Новая карточка, которую она переслала с панели = «принято к сведению»: в notes.json дописать `"noted": "что берём"`,
  `"when": "<группа ниже>"` → `python noted_to_skill.py` → `python news.py --build` (карточка уходит с панели) →
  дальше процедура скилла dropship-lessons (урок в нужный раздел, GitHub, применить к делу).
- Когда нужен подробный текст урока — открыть `принятое.md` и найти по заголовку или ключу `канал/номер`.
- При разборе новых постов: если новость повторяет уже принятое — `skip` (дубль), не показывать снова.

## Оглавление — всего 96

### Всегда: кому можно отдавать данные (8)
- Агентам — без боевых ключей и доступа к серверам — 29.09 — правило «ВСЕГДА» в скилле dropship-lessons и в памяти: предупреждаю перед каждой отправкой данных наружу ([vibecoding_community/232171](https://t.me/vibecoding_community/232171))
- Свою систему — из готовой базы, не с нуля — 29.09 — правило «ВСЕГДА» в скилле dropship-lessons и в памяти: предупреждаю перед каждой отправкой данных наружу ([vibecoding_community/231493](https://t.me/vibecoding_community/231493))
- Не запускать чужие ИИ-клиенты в папках с ключами — 29.09 — правило «ВСЕГДА» в скилле dropship-lessons ([vibecoding_tg/3968](https://t.me/vibecoding_tg/3968))
- Три корзины данных: облаку / только ПК / никому — 29.09 — правило «ВСЕГДА» в скилле dropship-lessons и в памяти: предупреждаю перед каждой отправкой данных наружу ([vibecoding_community/225811](https://t.me/vibecoding_community/225811))
- Длинная сессия дорожает — перед большой задачей перезапускать — 29.09 — правило в скилле dropship-lessons и в памяти: перед большой задачей в длинной сессии предупреждаю «перезапусти» ([vibecoding_community/224602](https://t.me/vibecoding_community/224602))
- Наши инструменты — монолит — 29.09 — правило «ВСЕГДА» в скилле dropship-lessons ([python_tg/4011](https://t.me/python_tg/4011))
- Бесплатные роутеры моделей — нет — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Всегда: кому можно отдавать данные» ([PushEnter/13670](https://t.me/PushEnter/13670))
- ИИ-метку на фото не стирать, в Meta помечать — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Всегда: кому можно отдавать данные» ([PushEnter/13640](https://t.me/PushEnter/13640))

### Всегда: лимит Claude и чужие скиллы (12)
- Браузер-агенты — только публичные сайты, не 1688/Taobao — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Всегда: лимит Claude и чужие скиллы» ([vibecoding_tg/3873](https://t.me/vibecoding_tg/3873))
- Граф-курс Google — не усложнять агентами — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Всегда: лимит Claude и чужие скиллы» ([PushEnter/13694](https://t.me/PushEnter/13694))
- Проверка скиллов на лишнюю работу и конфликты — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Всегда: лимит Claude и чужие скиллы» ([PushEnter/13691](https://t.me/PushEnter/13691))
- claude plugin eval — проверочные примеры скиллов — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Всегда: лимит Claude и чужие скиллы» ([vibecoding_tg/3843](https://t.me/vibecoding_tg/3843))
- Курс CMU: мерить, как справляется агент — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Всегда: лимит Claude и чужие скиллы» ([LLMScience/1098](https://t.me/LLMScience/1098))
- Чистить старые инструкции, max не по умолчанию — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Всегда: лимит Claude и чужие скиллы» ([vibecoding_tg/3829](https://t.me/vibecoding_tg/3829))
- Большие файлы читает дешёвый субагент — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Всегда: лимит Claude и чужие скиллы» ([vibecoding_tg/3819](https://t.me/vibecoding_tg/3819))
- Stealth Browser — не под её аккаунтами — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Всегда: лимит Claude и чужие скиллы» ([python2day/8140](https://t.me/python2day/8140))
- Чужие скиллы — только после чтения репозитория — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Всегда: лимит Claude и чужие скиллы» ([python2day/8138](https://t.me/python2day/8138))
- Stanford: скилл каждый раз (pass^k), не мультиагенты — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Всегда: лимит Claude и чужие скиллы» ([LLMScience/1083](https://t.me/LLMScience/1083))
- Гайд Anthropic по промптам Fable 5.1 — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Всегда: лимит Claude и чужие скиллы» ([PushEnter/13633](https://t.me/PushEnter/13633))
- /effort по задаче, max не держать — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Всегда: лимит Claude и чужие скиллы» ([vibecoding_tg/3786](https://t.me/vibecoding_tg/3786))

### Экономика товара и теста (9)
- Учебник микроэкономики — в скилле knowledge-library — 29.09 — выгружено в скилл knowledge-library; напомню, когда задача коснётся темы ([LLMScience/1192](https://t.me/LLMScience/1192))
- Тест товара $150–300, потолок цены покупателя, когда останавливать тест — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «экономика товара и теста» ([shopify_offstudzent/948](https://t.me/shopify_offstudzent/948))
- ROAS ≠ прибыль: считать каждый заказ — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «экономика товара и теста» ([shopify_offstudzent/946](https://t.me/shopify_offstudzent/946))
- Старт с $500: $55 с продажи, ~20 тыс. просмотров на продажу — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «экономика товара и теста» ([tkachevshopify/2881](https://t.me/tkachevshopify/2881))
- Поставщик подведёт: разбор счёта, торг, запасной поставщик — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Экономика товара и теста» ([proecomdmitriy/1184](https://t.me/proecomdmitriy/1184))
- ROAS 4,51 → 35% прибыли (день в США) — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Экономика товара и теста» ([akuliabuhta/1132](https://t.me/akuliabuhta/1132))
- Маржа до рекламы ~66%; продавать образами — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Экономика товара и теста» ([akuliabuhta/1129](https://t.me/akuliabuhta/1129))
- Чек >$80: «купи 2–3», без дешёвого, сезон по полушарию — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Экономика товара и теста» ([akuliabuhta/1120](https://t.me/akuliabuhta/1120))
- Средний чек США $75–120 — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Экономика товара и теста» ([akuliabuhta/1114](https://t.me/akuliabuhta/1114))

### Реклама и креативы (11)
- TrackGleam — довести звук ролика — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Реклама и креативы» ([PushEnter/13767](https://t.me/PushEnter/13767))
- Озвучка роликов — ElevenLabs v4 с тегами эмоций — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Реклама и креативы» ([PushEnter/13765](https://t.me/PushEnter/13765))
- 6 углов подачи на товар вместо 3 роликов — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «реклама и креативы» ([shopify_offstudzent/947](https://t.me/shopify_offstudzent/947))
- Meta: от $50 в день на кампанию — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Реклама и креативы» ([shopify_chat/166511](https://t.me/shopify_chat/166511))
- Google: Performance Max + Shopping на фиде, брендовый поиск — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Реклама и креативы» ([akuliabuhta/1155](https://t.me/akuliabuhta/1155))
- 201 промпт для фото и видео — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Реклама и креативы» ([PushEnter/13672](https://t.me/PushEnter/13672))
- GPT Images 2.5: точечная правка, Sketch — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Реклама и креативы» ([PushEnter/13663](https://t.me/PushEnter/13663))
- GMC: подготовить магазин до подачи, 3 попытки — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Реклама и креативы» ([shopify_chat/165794](https://t.me/shopify_chat/165794))
- Дропы новинок вместо постоянной полки — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Реклама и креативы» ([world_ecom/997](https://t.me/world_ecom/997))
- 10 000+ промптов: карточки и креативы — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Реклама и креативы» ([python2day/8135](https://t.me/python2day/8135))
- 10 000+ промптов: карточки и креативы — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Реклама и креативы» ([PushEnter/13614](https://t.me/PushEnter/13614))

### Платежи, корзина, каналы (15)
- Корзина: доставка видна заранее, без обязательной регистрации, пройти путь с телефона — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Платежи, корзина, каналы» ([proecomdmitriy/1195](https://t.me/proecomdmitriy/1195))
- TikTok Shop США: ИИ вместо англоговорящего сотрудника — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Платежи, корзина, каналы» ([anita_bold/5995](https://t.me/anita_bold/5995))
- Shopify Payments через LLC — иначе +2%; маржа дропшиппинга ~21% — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «платежи, корзина, каналы» ([proecomdmitriy/1192](https://t.me/proecomdmitriy/1192))
- TikTok Shop / Temu — свои цены с учётом комиссии — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «платежи, корзина, каналы» ([world_ecom/1028](https://t.me/world_ecom/1028))
- Средний чек: наборы и допродажа (перенести из ARTMELLIO) — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «платежи, корзина, каналы» ([proecomdmitriy/1191](https://t.me/proecomdmitriy/1191))
- Резервный магазин и копия каталога на случай бана — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Платежи, корзина, каналы» ([shopify_chat/166646](https://t.me/shopify_chat/166646))
- EIN — сразу в пакете регистрации LLC — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Платежи, корзина, каналы» ([shopify_chat/166588](https://t.me/shopify_chat/166588))
- Зачёркнутая цена — только настоящая — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Платежи, корзина, каналы» ([world_ecom/1006](https://t.me/world_ecom/1006))
- Карточки и чекаут — понятные ИИ-агенту — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Платежи, корзина, каналы» ([world_ecom/1004](https://t.me/world_ecom/1004))
- Покупать будут ИИ-агенты (Meta Muse) — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Платежи, корзина, каналы» ([vibecoding_tg/3827](https://t.me/vibecoding_tg/3827))
- ИИ-консультант по размерам — после запуска — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Платежи, корзина, каналы» ([vibecoding_tg/3796](https://t.me/vibecoding_tg/3796))
- Первые выплаты через 1–3 недели — оборотка — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Платежи, корзина, каналы» ([shopify_chat/165596](https://t.me/shopify_chat/165596))
- TikTok Shop США открыт китайским компаниям — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Платежи, корзина, каналы» ([anita_bold/5963](https://t.me/anita_bold/5963))
- Kohl's: ИИ-ассистент в магазине — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Платежи, корзина, каналы» ([world_ecom/996](https://t.me/world_ecom/996))
- ChatGPT-витрина: карточки понятные машине — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Платежи, корзина, каналы» ([world_ecom/995](https://t.me/world_ecom/995))

### После запуска рекламы (6)
- Конверсия ~2%, смотреть воронку корзина → checkout → покупка — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «после запуска рекламы» ([proecomdmitriy/1193](https://t.me/proecomdmitriy/1193))
- 8 email-воронок в Klaviyo (+11% продаж) — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «После запуска рекламы» ([akuliabuhta/1156](https://t.me/akuliabuhta/1156))
- Seel — перепродажа невозвратного, кругозор — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «После запуска рекламы» ([world_ecom/999](https://t.me/world_ecom/999))
- Поддержка и трек-номера — защита платёжки — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «После запуска рекламы» ([akuliabuhta/1127](https://t.me/akuliabuhta/1127))
- Refund no return в политику возвратов — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «После запуска рекламы» ([akuliabuhta/1121](https://t.me/akuliabuhta/1121))
- Своя база email с первого дня (SKIMS) — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «После запуска рекламы» ([proecomdmitriy/1156](https://t.me/proecomdmitriy/1156))

### Страны и доставка (5)
- Landmark Global — кандидат на доставку в США — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «страны и доставка» ([world_ecom/1025](https://t.me/world_ecom/1025))
- Для каждой страны свой оффер, а не перевод — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «страны и доставка» ([proecomdmitriy/1190](https://t.me/proecomdmitriy/1190))
- Запускать рекламу сразу на несколько стран — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «страны и доставка» ([akuliabuhta/1160](https://t.me/akuliabuhta/1160))
- Переводы текстов и картинок через Claude Code — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «страны и доставка» ([proecomdmitriy/1185](https://t.me/proecomdmitriy/1185))
- Платная доставка + порог бесплатной — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Страны и доставка» ([shopify_chat/164850](https://t.me/shopify_chat/164850))

### Когда будет время (инструменты) (30)
- Курс ИИ-агентов CMU 11-768 — 29.09 — записано в скилл dropship-lessons; напомню по одному после «новостей» ([vibecoding_tg/3982](https://t.me/vibecoding_tg/3982))
- Один DESIGN.md на тему магазина (+ 21st.dev) — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню по одному после «новостей» ([vibecoding_tg/3966](https://t.me/vibecoding_tg/3966))
- База материалов Python с нуля — 29.09 — выгружено в скилл knowledge-library; напомню, когда задача коснётся темы ([python_tg/4036](https://t.me/python_tg/4036))
- Рашка: точность модели на этапе ответа — 29.09 — записано в скилл dropship-lessons; напомню по одному после «новостей» ([LLMScience/1189](https://t.me/LLMScience/1189))
- with вместо __del__ — 29.09 — выгружено в скилл knowledge-library; напомню, когда задача коснётся темы ([python_tg/4033](https://t.me/python_tg/4033))
- Курс глубокого обучения де Фрейтаса — 29.09 — записано в скилл dropship-lessons; напомню по одному после «новостей» ([LLMScience/1185](https://t.me/LLMScience/1185))
- Официальный учебник Python — 29.09 — выгружено в скилл knowledge-library; напомню, когда задача коснётся темы ([python_tg/4028](https://t.me/python_tg/4028))
- prompt-audit (повтор совета) — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню по одному после «новостей» ([PushEnter/13752](https://t.me/PushEnter/13752))
- /brag — промо-ролик для наших панелей — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню по одному после «новостей» ([python2day/8182](https://t.me/python2day/8182))
- `/claude-api prompt-audit` — уборка инструкций и скиллов — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню по одному после «новостей» ([PushEnter/13742](https://t.me/PushEnter/13742))
- «Что значит готово» — строка в CLAUDE.md — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню по одному после «новостей» ([PushEnter/13738](https://t.me/PushEnter/13738))
- Jev — скиллы по требованию (сравнить экономию) — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню по одному после «новостей» ([vibecoding_tg/3919](https://t.me/vibecoding_tg/3919))
- Проверка ИНН/ОГРН/СНИЛС для дел — 29.09 — выгружено в скилл knowledge-library; напомню, когда задача коснётся темы ([python_tg/4021](https://t.me/python_tg/4021))
- Туннель Cloudflare — временная ссылка на localhost — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню по одному после «новостей» ([vibecoding_tg/3901](https://t.me/vibecoding_tg/3901))
- Справочник pandas для таблиц — 29.09 — выгружено в скилл knowledge-library; напомню, когда задача коснётся темы ([python_tg/4018](https://t.me/python_tg/4018))
- weakref — кеш без утечек — 29.09 — выгружено в скилл knowledge-library; напомню, когда задача коснётся темы ([python_tg/4016](https://t.me/python_tg/4016))
- Orca — второй агент проверяет первого — 27.09 — записано в скилл dropship-lessons и в GitHub; напомню по одному после «новостей» ([vibecoding_tg/3887](https://t.me/vibecoding_tg/3887))
- Cloudflare security-audit — сравнить на боте «Дела» — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Когда будет время (инструменты)» ([vibecoding_tg/3881](https://t.me/vibecoding_tg/3881))
- Русский справочник Python — 29.09 — выгружено в скилл knowledge-library; напомню, когда задача коснётся темы ([python_tg/4008](https://t.me/python_tg/4008))
- Гайд Google по ИИ-интерфейсам → в DESIGN.md темы — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Когда будет время (инструменты)» ([PushEnter/13707](https://t.me/PushEnter/13707))
- AlphaXiv — авто-ресёрч ниши для радара — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Когда будет время (инструменты)» ([PushEnter/13706](https://t.me/PushEnter/13706))
- OpenDataLoader: PDF → текст для «Дел» и рефератов — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Когда будет время (инструменты)» ([LLMScience/1115](https://t.me/LLMScience/1115))
- Claude Mods — скрытие ключей на экране — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Когда будет время (инструменты)» ([vibecoding_tg/3857](https://t.me/vibecoding_tg/3857))
- Шпаргалка по базовым конструкциям Python — 29.09 — картинка положена в скилл knowledge-library; напомню, когда задача коснётся темы ([python_tg/3998](https://t.me/python_tg/3998))
- asyncio — ускорить сборщики — 29.09 — выгружено в скилл knowledge-library; напомню, когда задача коснётся темы ([python_tg/3996](https://t.me/python_tg/3996))
- M3E Canvas — макет мышкой → ТЗ — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Когда будет время (инструменты)» ([PushEnter/13652](https://t.me/PushEnter/13652))
- M3E Canvas — макет мышкой → ТЗ — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Когда будет время (инструменты)» ([vibecoding_tg/3808](https://t.me/vibecoding_tg/3808))
- youtube-skills — выжимки роликов — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Когда будет время (инструменты)» ([PushEnter/13649](https://t.me/PushEnter/13649))
- Meta Muse Spark 1.3 — кругозор — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Когда будет время (инструменты)» ([vibecoding_tg/3793](https://t.me/vibecoding_tg/3793))
- PyApp — скрипт как программа — 29.09 — записано в скилл dropship-lessons и в GitHub; напомню в момент «Когда будет время (инструменты)» ([python2day/8128](https://t.me/python2day/8128))
