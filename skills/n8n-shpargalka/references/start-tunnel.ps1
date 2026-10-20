# Публичный адрес для n8n через бесплатный туннель Cloudflare + перевод
# вебхуков Shopify на этот адрес.
#
# Без аккаунта и без домена: cloudflared выдаёт случайный адрес вида
#   https://xxxx-xxxx.trycloudflare.com
# Адрес МЕНЯЕТСЯ при каждом запуске, поэтому скрипт сам перерегистрирует
# вебхуки в Shopify (scripts/webhooks/register_shopify_webhooks.py).
# Работает, пока запущен этот скрипт и включён компьютер. Заказы при этом
# не теряются — они лежат в Shopify, панель просто увидит их позже.
#
# Порядок:
#   .\n8n\start-n8n.ps1        # окно 1: сам n8n
#   .\n8n\start-tunnel.ps1     # окно 2: туннель + вебхуки
#   .\panel\start-panel.ps1    # окно 3: панель
#
# Какие темы регистрировать — переменная $Topics ниже. Регистрировать только
# те, чьи воркфлоу ВКЛЮЧЕНЫ в n8n: на выключенный n8n отвечает 404, и Shopify
# после серии неудач подписку удаляет.

param(
    [string]$Topics = 'ORDERS_CREATE,PRODUCTS_UPDATE',
    [int]$N8nPort = 5678
)

$ErrorActionPreference = 'Stop'
$repo = Split-Path $PSScriptRoot -Parent

$cf = Get-Command cloudflared -ErrorAction SilentlyContinue
if (-not $cf) {
    $cand = 'C:\Program Files (x86)\cloudflared\cloudflared.exe', 'C:\Program Files\cloudflared\cloudflared.exe'
    $cf = $cand | Where-Object { Test-Path $_ } | Select-Object -First 1
    if (-not $cf) { throw 'cloudflared не найден. Установка: winget install --id Cloudflare.cloudflared -e' }
} else { $cf = $cf.Source }

try { Invoke-WebRequest -UseBasicParsing "http://localhost:$N8nPort/healthz" -TimeoutSec 3 | Out-Null }
catch { Write-Warning "n8n на порту $N8nPort не отвечает. Сначала .\n8n\start-n8n.ps1 — туннель всё равно подниму." }

$log = Join-Path $env:TEMP 'cloudflared-n8n.log'
if (Test-Path $log) { Remove-Item $log -Force }

Write-Output 'поднимаю туннель Cloudflare...'
$proc = Start-Process -FilePath $cf -ArgumentList "tunnel --url http://localhost:$N8nPort --no-autoupdate" `
    -RedirectStandardError $log -NoNewWindow -PassThru

$url = $null
for ($i = 0; $i -lt 60 -and -not $url; $i++) {
    Start-Sleep 1
    if (Test-Path $log) {
        $m = Select-String -Path $log -Pattern 'https://[a-z0-9-]+\.trycloudflare\.com' | Select-Object -First 1
        if ($m) { $url = $m.Matches[0].Value }
    }
}
if (-not $url) { Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue; throw "адрес туннеля не появился за минуту, лог: $log" }

Write-Output "публичный адрес: $url"
Write-Output "перевожу вебхуки Shopify ($Topics) на этот адрес..."
python (Join-Path $repo 'scripts\webhooks\register_shopify_webhooks.py') --url $url --topics $Topics

Write-Output ''
Write-Output "готово. Туннель живёт, пока открыто это окно. Закрыть — Ctrl+C."
try { Wait-Process -Id $proc.Id }
finally { Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue }
