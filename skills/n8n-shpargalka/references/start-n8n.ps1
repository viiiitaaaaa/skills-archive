# Запуск n8n с ключами магазина.
#
# Ключи НЕ хранятся в репозитории: скрипт читает их из файла на рабочем столе
# (тот же, что использует scripts/shop_api.py) и кладёт в переменные окружения
# текущего процесса. Воркфлоу обращаются к ним как {{ $env.SHOPIFY_CLIENT_ID }}.
#
#   .\n8n\start-n8n.ps1

$ErrorActionPreference = 'Stop'

$creds = 'C:\Users\User\Desktop\Новая папка (4)\shopy api.txt'
if (-not (Test-Path $creds)) {
    throw "Не нашёл файл с ключами: $creds"
}

$lines = Get-Content $creds | Where-Object { $_.Trim() -ne '' }
if ($lines.Count -lt 2) {
    throw 'В файле с ключами меньше двух непустых строк: ожидаю client_id и client_secret'
}

$env:SHOPIFY_CLIENT_ID     = $lines[0].Trim()
$env:SHOPIFY_CLIENT_SECRET = $lines[1].Trim()
$env:SHOPIFY_SHOP          = 'kmfmxn-r4.myshopify.com'

# Telegram-бот для уведомлений (необязательно). Файл рядом с ключами Shopify:
# строка 1 - токен от @BotFather, строка 2 - chat_id (см. scripts/telegram/setup_telegram.py).
# Если файла нет, воркфлоу просто пропускают ветку "В Telegram".
$tg = 'C:\Users\User\Desktop\Новая папка (4)\telegram bot.txt'
if (Test-Path $tg) {
    $tgLines = Get-Content $tg | Where-Object { $_.Trim() -ne '' }
    if ($tgLines.Count -ge 2) {
        $env:TELEGRAM_BOT_TOKEN = $tgLines[0].Trim()
        $env:TELEGRAM_CHAT_ID   = $tgLines[1].Trim()
        Write-Output 'telegram: ключи подставлены'
    } else {
        Write-Warning "telegram: в файле нет chat_id, запустите python scripts\telegram\setup_telegram.py"
    }
} else {
    Write-Output 'telegram: файла с ключами нет, уведомления только в панель'
}

# Без этого узлы не видят переменные окружения и падают с
# "access to env vars denied" - в n8n 2.x доступ закрыт по умолчанию.
$env:N8N_BLOCK_ENV_ACCESS_IN_NODE = 'false'

# Code-узлам разрешаем require('fs'): сценарий «сбой сценария» читает имена из panel/registry.json.
$env:NODE_FUNCTION_ALLOW_BUILTIN = 'fs'

# В n8n 2.x узел Execute Command выключен по умолчанию (NODES_EXCLUDE). Он нужен
# проверке поставщиков: запускает scripts/suppliers/check_suppliers.py.
$env:NODES_EXCLUDE = '[]'

# Execute Command запускает наши python-скрипты: пусть печатают в utf-8, иначе русские буквы ломаются.
$env:PYTHONIOENCODING = 'utf-8'
$env:PYTHONUTF8 = '1'

# телеметрия наружу не нужна
$env:N8N_DIAGNOSTICS_ENABLED = 'false'

Write-Output 'ключи подставлены, поднимаю n8n -> http://localhost:5678'
n8n start
