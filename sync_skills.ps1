# Синхронизация скиллов в архивную папку.
# Запуск: powershell -ExecutionPolicy Bypass -File "C:\Users\User\ARTMELLIO_SKILLS\sync_skills.ps1"
# Архив — git-репозиторий viiiitaaaaa/artmellio-skills (приватный); после синхронизации изменения сами уходят на GitHub.

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

$stamp = Get-Date -Format "yyyy-MM-dd HH:mm"
$count = (Get-ChildItem $pack -Directory).Count
$files = (Get-ChildItem $pack -Recurse -File).Count
"Синхронизировано: $count скиллов, $files файлов. $stamp" | Out-File (Join-Path $dst "last_sync.txt") -Encoding utf8
Write-Output "OK: $count скиллов, $files файлов -> $dst"

# 4. Отправить изменения на GitHub
Push-Location $dst
git add -A
if (git status --porcelain) {
    git -c user.name="viiiitaaaaa" -c user.email="tehrez21@gmail.com" commit -q -m "Синхронизация скиллов $stamp"
    git push -q
    Write-Output "Отправлено на GitHub: viiiitaaaaa/artmellio-skills"
} else { Write-Output "Изменений нет, на GitHub отправлять нечего" }
Pop-Location
