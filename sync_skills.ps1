# Синхронизация скиллов в архивную папку.
# Запуск: powershell -ExecutionPolicy Bypass -File "C:\Users\User\skills-archive\sync_skills.ps1"
# Архив — git-репозиторий viiiitaaaaa/skills-archive (приватный); после синхронизации изменения сами уходят на GitHub.

$src  = "C:\Users\User\.claude\skills"
$dst  = $PSScriptRoot
$pack = Join-Path $dst "skills"
$prom = Join-Path $dst "promty"

foreach ($d in @($pack, $prom)) {
    if (Test-Path $d) { Remove-Item $d -Recurse -Force }
    New-Item -ItemType Directory -Path $d -Force | Out-Null
}

# 1. Полная копия всех скиллов
Copy-Item -Path (Join-Path $src "*") -Destination $pack -Recurse -Force
# вложенные git-репозитории скиллов в архив не берём (у них свои репозитории)
Get-ChildItem $pack -Recurse -Directory -Force -Filter .git | Remove-Item -Recurse -Force

# 2. Отдельно вытащить файлы с промтами и рецептами
$promptFiles = @(
    @{ from = "site-mockups\prompts.md";                  to = "site-mockups__prompts.md" },
    @{ from = "site-mockups\design_system.md";            to = "site-mockups__design_system.md" },
    @{ from = "site-mockups\comfy_api.md";                to = "site-mockups__comfy_api.md" },
    @{ from = "room-scenes\run_comfy.md";                 to = "room-scenes__run_comfy.md" },
    @{ from = "style-collections\стили-2025-2026-промты.pdf"; to = "style-collections__стили-2025-2026-промты.pdf" }
)
foreach ($p in $promptFiles) {
    $f = Join-Path $src $p.from
    if (Test-Path $f) { Copy-Item $f (Join-Path $prom $p.to) -Force }
}

# 3. Промты, вшитые в тело скилла — копируем SKILL.md целиком
foreach ($s in @("product-scenes", "shopify-collections", "site-mockups", "room-scenes")) {
    $f = Join-Path $src "$s\SKILL.md"
    if (Test-Path $f) { Copy-Item $f (Join-Path $prom "${s}__SKILL.md") -Force }
}

# 3б. Память Claude (её решения) и общий CLAUDE.md — без них новая сессия не помнит договорённостей
$mem = Join-Path $dst "memory"
if (Test-Path $mem) { Remove-Item $mem -Recurse -Force }
New-Item -ItemType Directory -Path $mem -Force | Out-Null
Copy-Item "C:\Users\User\.claude\projects\C--Users-User\memory\*.md" $mem -Force
Copy-Item "C:\Users\User\.claude\CLAUDE.md" (Join-Path $dst "CLAUDE_global.md") -Force

# 3д. Память каждого проекта (с 14.10 у каждой папки своя) — memory_proektov\<папка>\*.md; временные scratch-папки пропускаем
# Выключатели: включены 15.10.2026 по её слову («все включаем настройки, все абсолютно»)
$vklMemProektov = $true
$vklNastroyki   = $true
$memP = Join-Path $dst "memory_proektov"
if ($vklMemProektov) {
if (Test-Path $memP) { Remove-Item $memP -Recurse -Force }
Get-ChildItem "C:\Users\User\.claude\projects" -Directory | Where-Object { $_.Name -ne "C--Users-User" -and $_.Name -notlike "*scratch*" -and $_.Name -notlike "*zdorovie*" } | ForEach-Object {
    # zdorovie — данные о здоровье: в GitHub нельзя (правило zdorovie\CLAUDE.md), исключено 18.10
    $m = Join-Path $_.FullName "memory"
    if ((Test-Path $m) -and (Get-ChildItem $m -Filter *.md)) {
        $to = Join-Path $memP ($_.Name -replace '^C--Users-User-', '')
        New-Item -ItemType Directory -Path $to -Force | Out-Null
        Copy-Item (Join-Path $m "*.md") $to -Force
    }
}
}

# 3е. Настройки Claude Code для восстановления на новом ПК. settings.local.json НЕ берём — в нём ключ бота.
$cfg = Join-Path $dst "nastroyki_claude"
if ($vklNastroyki) {
if (Test-Path $cfg) { Remove-Item $cfg -Recurse -Force }
New-Item -ItemType Directory -Path $cfg -Force | Out-Null
foreach ($f in @("settings.json", "statusline.py", "agent_status.py")) {
    $p = Join-Path "C:\Users\User\.claude" $f
    if (Test-Path $p) { Copy-Item $p $cfg -Force }
}
foreach ($d in @("agents", "sounds")) {
    $p = Join-Path "C:\Users\User\.claude" $d
    if (Test-Path $p) { Copy-Item $p (Join-Path $cfg $d) -Recurse -Force }
}
if (Test-Path "C:\Users\User\komputer\CLAUDE.md") { Copy-Item "C:\Users\User\komputer\CLAUDE.md" (Join-Path $cfg "komputer_CLAUDE.md") -Force }
# список MCP-подключений: ключи вырезаются скриптом (нашёл ключ — файл не пишется)
python -I "C:\Users\User\komputer\rezerv\eksport_mcp.py" (Join-Path $cfg "mcp_servers.json")
}

# 3г. Файлы для проектов Claude Desktop (правила веток + «Что мы умеем и знаем.md») — копия с рабочего стола
$cd  = "C:\Users\User\Desktop\Файлы для проектов Claude"
$cdA = Join-Path $dst "proekty_claude_desktop"
if (Test-Path $cd) {
    if (Test-Path $cdA) { Remove-Item $cdA -Recurse -Force }
    New-Item -ItemType Directory -Path $cdA -Force | Out-Null
    Copy-Item (Join-Path $cd "*") $cdA -Force
}

# 3в. База новостей (20+ МБ, в git не кладём) — копия на Google Диск, если изменилась
$db = "C:\Users\User\tg_monitor\tg_monitor.db"
$dbDir = "G:\Мой диск\Программы и ярлыки (с рабочего стола)\Резерв — база новостей"
if ((Test-Path $db) -and (Test-Path "G:\Мой диск")) {
    New-Item -ItemType Directory -Path $dbDir -Force | Out-Null
    $copy = Join-Path $dbDir "tg_monitor.db"
    if (-not (Test-Path $copy) -or (Get-Item $db).LastWriteTime -gt (Get-Item $copy).LastWriteTime) {
        Copy-Item $db $copy -Force
        Write-Output "База новостей скопирована на Google Диск"
    }
}

$stamp = Get-Date -Format "yyyy-MM-dd HH:mm"
$count = (Get-ChildItem $pack -Directory).Count
$files = (Get-ChildItem $pack -Recurse -File).Count
"Синхронизировано: $count скиллов, $files файлов. $stamp" | Out-File (Join-Path $dst "last_sync.txt") -Encoding utf8
Write-Output "OK: $count скиллов, $files файлов -> $dst"

# 4. Отправить изменения на GitHub
Push-Location $dst
git add -A
# проверка на ключи перед выгрузкой (её правило 15.10: ключи — только на ПК); нашёл — не отправляем
python -I "C:\Users\User\komputer\rezerv\proverka_klyuchey.py" --staged
if ($LASTEXITCODE -ne 0) { git reset -q; Pop-Location; Write-Output "НЕ ОТПРАВЛЕНО: найден похожий на ключ текст"; exit 1 }
if (git status --porcelain) {
    git -c user.name="viiiitaaaaa" -c user.email="tehrez21@gmail.com" commit -q -m "Синхронизация скиллов $stamp"
    git push -q
    Write-Output "Отправлено на GitHub: viiiitaaaaa/skills-archive"
} else { Write-Output "Изменений нет, на GitHub отправлять нечего" }
Pop-Location

# 5. Полная проверка всех папок и истории git на ключи + что все хранилища на GitHub закрытые
python -I "C:\Users\User\komputer\rezerv\proverka_klyuchey.py"
