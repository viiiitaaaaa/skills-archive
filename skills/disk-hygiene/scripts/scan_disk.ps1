# Сканирует диск программой WizTree и печатает отчёт: крупные папки, файлы, повторы, кэши, старые версии.
# Запуск: powershell -ExecutionPolicy Bypass -File scan_disk.ps1 [-Drive C]
param([string]$Drive = "C")
$wiz = @("C:\Program Files\WizTree\WizTree64.exe", "C:\Program Files (x86)\WizTree\WizTree64.exe") | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $wiz) { Write-Output "WizTree не найден — установите с diskanalyzer.com"; exit 1 }
$dir = Join-Path $env:TEMP "disk-hygiene"; New-Item -ItemType Directory -Force $dir | Out-Null
$csv = Join-Path $dir "wiz_$Drive.csv"; Remove-Item $csv -ErrorAction SilentlyContinue
Start-Process $wiz -ArgumentList "${Drive}:\ /export=`"$csv`" /exportfiles=1 /exportfolders=1 /admin=0" -Wait
Get-PSDrive $Drive | ForEach-Object { "Диск {0}: занято {1:N1} ГБ, свободно {2:N1} ГБ" -f $Drive, ($_.Used/1GB), ($_.Free/1GB) }
$env:PYTHONIOENCODING = "utf-8"
python -X utf8 (Join-Path $PSScriptRoot "report.py") $csv
