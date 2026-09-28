# Очистка места на C:. По умолчанию — вхолостую (только показывает). Удаляет безвозвратно только с -Apply.
# Пример: powershell -ExecutionPolicy Bypass -File clean.ps1 -Items capcut-cache,npm-cache,temp -Apply
param(
    [Parameter(Mandatory = $true)][string[]]$Items,
    [switch]$Apply
)
$Items = $Items -split '[,\s]+' | Where-Object { $_ }
$L = $env:LOCALAPPDATA; $A = $env:APPDATA

function Get-Targets([string]$key) {
    switch ($key) {
        'capcut-cache'   { @("$L\CapCut\User Data\Cache") }
        'npm-cache'      { @("$L\npm-cache") }
        'pip-cache'      { @("$L\pip\cache") }
        # Temp без рабочей папки Claude Code
        'temp'           { Get-ChildItem -LiteralPath $env:TEMP -Force -ErrorAction SilentlyContinue | Where-Object Name -ne 'claude' | ForEach-Object FullName }
        'chrome-cache'   { Get-ChildItem "$L\Google\Chrome\User Data" -Recurse -Directory -Force -ErrorAction SilentlyContinue | Where-Object { $_.Name -in 'Cache', 'Code Cache', 'GPUCache' } | ForEach-Object FullName }
        'telegram-cache' { @("$A\Telegram Desktop\tdata\user_data\cache", "$A\Telegram Desktop\tdata\user_data\media_cache") }
        'amd'            { @("C:\AMD") }
        'whisper-small'  { Get-ChildItem "$env:USERPROFILE\.cache\huggingface\hub" -Directory -ErrorAction SilentlyContinue | Where-Object Name -match 'faster-whisper-small' | ForEach-Object FullName }
        'old-versions'   {
            foreach ($base in "$L\CapCut\Apps", "$L\Programs\Opera") {
                $v = Get-ChildItem -LiteralPath $base -Directory -ErrorAction SilentlyContinue | Where-Object Name -match '^\d' |
                     Sort-Object { [version]($_.Name -replace '[^\d.]', '') }
                if ($v.Count -gt 1) { $v | Select-Object -SkipLast 1 | ForEach-Object FullName }
            }
            "$A\aliim\Update"; "$A\Tencent\xwechat\update"; "C:\Users\Public\Documents\PDD\FullUpdateFile"
            Get-ChildItem -LiteralPath $L -Directory -Filter '*-updater' -ErrorAction SilentlyContinue | ForEach-Object FullName
        }
        'playwright-unused' { $env:PYTHONIOENCODING = 'utf-8'; python -X utf8 (Join-Path $PSScriptRoot 'pw_unused.py') }
        default { Write-Output "неизвестный ключ: $key"; @() }
    }
}

$guard = @('telegram-cache')  # программа должна быть закрыта
if ($Items -contains 'telegram-cache' -and (Get-Process Telegram -ErrorAction SilentlyContinue)) {
    Write-Output "Telegram запущен — закройте его, иначе кэш не удалится."; $Items = $Items | Where-Object { $_ -notin $guard }
}
if ($Items -contains 'chrome-cache' -and (Get-Process chrome -ErrorAction SilentlyContinue)) {
    Write-Output "Chrome запущен — часть кэша будет занята; лучше закрыть Chrome."
}

$before = (Get-PSDrive C).Free; $total = 0; $small = 0
foreach ($k in $Items) {
    foreach ($p in @(Get-Targets $k)) {
        if (-not $p -or -not (Test-Path -LiteralPath $p)) { continue }
        $size = (Get-ChildItem -LiteralPath $p -Recurse -File -Force -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
        if (-not $size) { $size = (Get-Item -LiteralPath $p -Force).Length }
        $total += $size
        if ($size -ge 5MB) { "{0,8:N0} МБ  [{1}] {2}" -f ($size / 1MB), $k, $p } else { $small++ }
        if ($Apply) {
            if ($k -in 'capcut-cache', 'npm-cache', 'pip-cache', 'telegram-cache') {
                Get-ChildItem -LiteralPath $p -Force -ErrorAction SilentlyContinue | ForEach-Object { try { Remove-Item -LiteralPath $_.FullName -Recurse -Force -Confirm:$false -ErrorAction Stop } catch {} }
            } else {
                try { Remove-Item -LiteralPath $p -Recurse -Force -Confirm:$false -ErrorAction Stop } catch { "   частично (заняты файлы): $p" }
            }
        }
    }
}
if ($small) { "   + ещё $small мелких объектов (меньше 5 МБ)" }
if ($Apply) {
    "освобождено {0:N2} ГБ; свободно на C: {1:N1} ГБ" -f (((Get-PSDrive C).Free - $before) / 1GB), ((Get-PSDrive C).Free / 1GB)
} else {
    "ВХОЛОСТУЮ: будет удалено около {0:N2} ГБ. Запустите с -Apply, чтобы удалить (безвозвратно)." -f ($total / 1GB)
}
