# Дымовой тест связки n8n -> Shopify.
#
# Гоняет воркфлоу 00-selftest-token: выпускает токен по client credentials и
# спрашивает у Admin API имя магазина и число товаров.
# Ожидаемый ответ: ARTMELLIO / PLN / 131.
#
#   .\n8n\selftest.ps1

$ErrorActionPreference = 'Stop'

$creds = 'C:\Users\User\Desktop\Новая папка (4)\shopy api.txt'
$lines = Get-Content $creds | Where-Object { $_.Trim() -ne '' }
$env:SHOPIFY_CLIENT_ID     = $lines[0].Trim()
$env:SHOPIFY_CLIENT_SECRET = $lines[1].Trim()
$env:N8N_BLOCK_ENV_ACCESS_IN_NODE = 'false'

# Если основной n8n уже поднят, он занимает 5678 и брокер 5679 -
# для разовой прогонки уводим на свободные порты.
$env:N8N_PORT               = '5691'
$env:N8N_RUNNERS_BROKER_PORT = '5690'

n8n execute --id=artmSelfTest001 --rawOutput 2>&1 |
    Select-String -Pattern 'связь|магазин|валюта|товаров|status'
