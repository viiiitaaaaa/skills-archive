<#
  pc_check.ps1 — проверка компьютера на вредоносные программы, майнеры, шпионов.
  Ничего не удаляет. Только собирает факты и пишет отчёт.

  Запуск:  powershell -NoProfile -ExecutionPolicy Bypass -File pc_check.ps1 [-Scan quick|full] [-Seconds 8]
  Отчёт:   C:\Users\User\pc_check\reports\pc_check_<дата>.md  (+ .json с сырыми данными)
  Лучше запускать от администратора — тогда видны исключения антивируса и все задачи.
#>
param(
    [ValidateSet('none','quick','full')] [string]$Scan = 'none',
    [int]$Seconds = 8,
    [string]$OutDir = 'C:\Users\User\pc_check\reports'
)
$ErrorActionPreference = 'SilentlyContinue'
[Console]::OutputEncoding = [Text.Encoding]::UTF8
New-Item -ItemType Directory -Force $OutDir | Out-Null
$stamp = Get-Date -Format 'yyyyMMdd_HHmm'
$md = Join-Path $OutDir "pc_check_$stamp.md"
$jsonPath = Join-Path $OutDir "pc_check_$stamp.json"
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

$findings = New-Object System.Collections.Generic.List[object]   # level: RED / YELLOW / INFO
function Add-Finding($level, $area, $what, $why, $action) {
    $findings.Add([PSCustomObject]@{ level=$level; area=$area; what=$what; why=$why; action=$action })
}

# --- справочники --------------------------------------------------------------
$userDirs = @("$env:TEMP", "$env:LOCALAPPDATA\Temp", "$env:APPDATA", "$env:LOCALAPPDATA", "$env:USERPROFILE\Downloads",
              'C:\ProgramData', 'C:\Users\Public', "$env:USERPROFILE\Desktop", 'C:\Windows\Temp', 'C:\$Recycle.Bin')
$knownBadNames = 'xmrig|minerd|cpuminer|nicehash|kryptex|nbminer|phoenixminer|t-rex|lolminer|gminer|ethminer|claymore|coinhive|srbminer|xmr-stak|ccminer|bfgminer|cgminer|wannamine|photominer'
$minerPorts = 3333,4444,5555,7777,8888,9999,14433,14444,45700,45560,3334,3335,3336,4445,5556,8008,8080,8899,45500
$lolbins = 'powershell|pwsh|cmd\.exe|wscript|cscript|mshta|rundll32|regsvr32|certutil|bitsadmin|msiexec|schtasks|wmic|forfiles|installutil|regasm|msbuild'
$suspArgs = '-enc|-encodedcommand|-e [A-Za-z0-9+/=]{20,}|-w hidden|-windowstyle hidden|bypass|downloadstring|invoke-expression|iex |frombase64|hidden|-nop |vbs|\.hta|javascript:'
$whitelistPublishers = 'Microsoft|Google|Anthropic|Mozilla|Opera|Telegram|Dropbox|Adobe|NVIDIA|Intel|Apple|Kensington|Yandex|Zoom|GitHub|Python Software|Dolphin|Windscribe|FlyFrog|Seagull|Discord|Spotify'

$exclNames = 'claude|python|pythonw|node|chrome|msedgewebview2|GoogleDriveFS|OneDrive|Taskmgr|powershell|conhost'  # наши и обычные, по CPU не паникуем

function In-UserDir($path) { if (-not $path) { return $false }; foreach ($d in $userDirs) { if ($path -like "$d*") { return $true } }; return $false }
function Sig($path) {
    if (-not $path -or -not (Test-Path $path)) { return 'нет файла' }
    $s = Get-AuthenticodeSignature $path
    if ($s.Status -eq 'Valid') { return "подписан: " + ($s.SignerCertificate.Subject -replace '^CN=([^,]+).*','$1') }
    return "НЕ подписан ($($s.Status))"
}
function Hash($path) { if ($path -and (Test-Path $path)) { (Get-FileHash $path -Algorithm SHA256).Hash } }

$report = [ordered]@{}
Write-Host "Проверка компьютера. Администратор: $isAdmin. Отчёт: $md"

# --- 1. Защитник Windows ------------------------------------------------------
Write-Host "1/10 Защитник Windows..."
$mp = Get-MpComputerStatus
$threats = Get-MpThreatDetection | Sort-Object InitialDetectionTime -Descending | Select-Object -First 20
$report.defender = [ordered]@{
    enabled = $mp.AntivirusEnabled; realtime = $mp.RealTimeProtectionEnabled; tamper = $mp.IsTamperProtected
    signatures = $mp.AntivirusSignatureLastUpdated; quickScan = $mp.QuickScanEndTime; fullScan = $mp.FullScanEndTime
    threats = @($threats | ForEach-Object { [ordered]@{ time=$_.InitialDetectionTime; id=$_.ThreatID; resources=($_.Resources -join '; '); action=$_.ActionSuccess } })
}
if (-not $mp.AntivirusEnabled) { Add-Finding RED 'Защитник' 'Антивирус выключен' 'Без антивируса любой файл запускается без проверки' 'Включить Защитник Windows или другой антивирус' }
elseif (-not $mp.RealTimeProtectionEnabled) { Add-Finding RED 'Защитник' 'Защита в реальном времени выключена' 'Вирус отключает её первым делом' 'Включить: Безопасность Windows → Защита от вирусов → Параметры' }
if ($mp.AntivirusSignatureLastUpdated -lt (Get-Date).AddDays(-7)) { Add-Finding YELLOW 'Защитник' "Базы старше недели ($($mp.AntivirusSignatureLastUpdated))" 'Новые вирусы не распознаются' 'Обновить базы: Безопасность Windows → Обновления защиты' }
if ($Scan -ne 'full' -and (-not $mp.FullScanEndTime -or $mp.FullScanEndTime -lt (Get-Date).AddDays(-30))) { Add-Finding YELLOW 'Защитник' 'Полная проверка не делалась больше месяца' 'Быстрая проверка смотрит только типовые места' 'Запустить: pc_check.ps1 -Scan full (1–3 часа)' }
foreach ($t in $threats) { Add-Finding YELLOW 'Защитник' "Ранее найдена угроза: $($t.Resources -join '; ')" "Обнаружено $($t.InitialDetectionTime)" 'Проверить в Безопасность Windows → Журнал защиты, что угроза удалена/в карантине' }
$exclusions = @($mp.ExclusionPath) + @($mp.ExclusionProcess) | Where-Object { $_ }
if (-not $exclusions) { $prefs = Get-MpPreference; $exclusions = @($prefs.ExclusionPath) + @($prefs.ExclusionProcess) + @($prefs.ExclusionExtension) | Where-Object { $_ } }
$exclusions = @($exclusions | Where-Object { $_ -notlike 'N/A*' })
if (-not $isAdmin) { Add-Finding INFO 'Защитник' 'Исключения антивируса не проверены' 'Список исключений виден только администратору' 'Запустить проверку с правами администратора' }
$report.defender.exclusions = @($exclusions)
foreach ($e in $exclusions) {
    if ($e -match 'SppExtComObjHook') { Add-Finding YELLOW 'Активатор' "Исключение антивируса для $e" 'Это файл KMS-активатора: им «бесплатно» активируют Windows или Office без покупки лицензии. Сам он не шпион, но его прячут от антивируса, а сборки активаторов из интернета часто бывают с вирусами внутри' 'Если активировали Windows/Office сами — знать об этом. Надёжнее купить ключ; файл и исключение тогда убрать'; continue }
    Add-Finding YELLOW 'Защитник' "Исключение из проверки: $e" 'Майнеры и шпионы часто добавляют свою папку в исключения, чтобы их не видели' 'Если вы этого не добавляли — убрать исключение' }

if ($Scan -ne 'none') {
    Write-Host "   Запуск проверки Защитником ($Scan)... это долго"
    Start-MpScan -ScanType $(if ($Scan -eq 'full') { 'FullScan' } else { 'QuickScan' })
    # состояние читали до проверки — перечитать, иначе в отчёте старые даты
    $mp = Get-MpComputerStatus
    $report.defender.quickScan = $mp.QuickScanEndTime; $report.defender.fullScan = $mp.FullScanEndTime
    $new = Get-MpThreatDetection | Where-Object { $_.InitialDetectionTime -gt (Get-Date).AddHours(-3) }
    foreach ($t in $new) { Add-Finding RED 'Защитник' "Найдено при проверке: $($t.Resources -join '; ')" 'Свежая находка антивируса' 'Открыть Безопасность Windows → Журнал защиты и удалить' }
}

# --- 2. Процессы: подпись, место, нагрузка ------------------------------------
Write-Host "2/10 Процессы (замер нагрузки $Seconds с)..."
$p1 = Get-Process | Select-Object Id, Name, Path, CPU, WorkingSet64, StartTime
Start-Sleep -Seconds $Seconds
$p2 = Get-Process | Select-Object Id, CPU
$cores = (Get-CimInstance Win32_ComputerSystem).NumberOfLogicalProcessors
$procs = foreach ($p in $p1) {
    $after = $p2 | Where-Object Id -eq $p.Id
    $cpuPct = if ($after -and $p.CPU -ne $null) { [math]::Round((($after.CPU - $p.CPU) / $Seconds / $cores) * 100, 1) } else { 0 }
    $cmd = (Get-CimInstance Win32_Process -Filter "ProcessId=$($p.Id)").CommandLine
    [PSCustomObject]@{ Id=$p.Id; Name=$p.Name; Path=$p.Path; CpuPct=$cpuPct; MemMB=[math]::Round($p.WorkingSet64/1MB); Cmd=$cmd; Sig=$null; UserDir=(In-UserDir $p.Path) }
}
foreach ($p in $procs) {
    if ($p.Name -match $knownBadNames -or $p.Cmd -match $knownBadNames -or $p.Cmd -match 'stratum\+tcp|--donate-level|--algo|-o pool\.') {
        Add-Finding RED 'Майнер' "Процесс $($p.Name) (PID $($p.Id)): $($p.Path)" 'Имя или параметры запуска как у криптомайнера' 'Завершить процесс, найти откуда запускается (раздел Автозагрузка), удалить файл' }
    if ($p.UserDir) {
        $p.Sig = Sig $p.Path
        if ($p.Sig -like 'НЕ подписан*' -or $p.Sig -eq 'нет файла') {
            Add-Finding YELLOW 'Процессы' "Неподписанный процесс из пользовательской папки: $($p.Name) → $($p.Path)" 'Вирусы живут в Temp/AppData/ProgramData, потому что туда можно писать без прав администратора. Подписи у них нет.' 'Проверить, что это за программа; хэш файла проверить на virustotal.com' }
    }
    if ($p.CpuPct -ge 25 -and $p.Name -notmatch $exclNames) {
        Add-Finding YELLOW 'Нагрузка' "Процесс $($p.Name) грузит процессор на $($p.CpuPct)% ($($p.Path))" 'Постоянная высокая нагрузка в простое — признак майнера' 'Если программа не должна сейчас работать — разобраться; майнер часто маскируется под svchost/explorer из чужой папки' }
    if ($p.Name -match '^(svchost|explorer|csrss|lsass|winlogon|services|smss|dwm)$' -and $p.Path -and $p.Path -notlike 'C:\Windows\*') {
        Add-Finding RED 'Маскировка' "Системное имя, но чужая папка: $($p.Name) → $($p.Path)" 'Настоящие системные процессы лежат только в C:\Windows' 'Это почти наверняка вредонос: завершить, удалить файл, проверить автозагрузку' }
    if ($p.Cmd -match $suspArgs -and $p.Name -match $lolbins -and $p.Cmd -notmatch 'pc_check\.ps1|CLAUDE_CODE|\\\.claude\\') {
        Add-Finding YELLOW 'Процессы' "Подозрительная команда: $($p.Name) $($p.Cmd.Substring(0,[math]::Min(200,$p.Cmd.Length)))" 'Скрытое окно, закодированная команда, загрузка из сети — типичные приёмы вирусов' 'Посмотреть, кто это запустил (родительский процесс, задача планировщика)' }
}
$report.processes = @($procs | Sort-Object CpuPct -Descending | Select-Object -First 40)
$report.cpuTop = @($procs | Sort-Object CpuPct -Descending | Select-Object -First 10 Name, CpuPct, MemMB, Path)
$report.memTop = @($procs | Group-Object Name | ForEach-Object { [PSCustomObject]@{ Name=$_.Name; Count=$_.Count; MemMB=($_.Group | Measure-Object MemMB -Sum).Sum } } | Sort-Object MemMB -Descending | Select-Object -First 10)

# --- 3. Сеть ------------------------------------------------------------------
Write-Host "3/10 Сетевые соединения..."
$conns = Get-NetTCPConnection -State Established | Where-Object { $_.RemoteAddress -notmatch '^(127\.|::1|0\.0\.0\.0|10\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.)' }
$connRows = foreach ($c in $conns) {
    $pr = $procs | Where-Object Id -eq $c.OwningProcess
    [PSCustomObject]@{ Proc=$pr.Name; Pid=$c.OwningProcess; Remote="$($c.RemoteAddress):$($c.RemotePort)"; Path=$pr.Path }
}
foreach ($r in $connRows) {
    $port = [int]($r.Remote -split ':')[-1]
    if ($port -in $minerPorts -and $r.Proc -notmatch 'chrome|opera|msedge|firefox|xray|Happ|Windscribe') {
        Add-Finding RED 'Сеть' "$($r.Proc) (PID $($r.Pid)) держит соединение $($r.Remote)" 'Порт типичен для пулов криптомайнинга' 'Проверить процесс; если не узнаёте — завершить и удалить' }
    if ($r.Path -and (In-UserDir $r.Path) -and $r.Proc -notmatch 'Telegram|Discord|Spotify|Zoom|claude|Code|cursor|python|node|opera|Whimsical|JDownloader|uTorrent|Comfy|GitHub') {
        Add-Finding YELLOW 'Сеть' "В интернет ходит программа из пользовательской папки: $($r.Proc) → $($r.Remote) ($($r.Path))" 'Шпионы отправляют данные наружу именно так' 'Понять, что за программа; незнакомую — удалить' }
}
$report.connections = @($connRows | Group-Object Proc | ForEach-Object { [PSCustomObject]@{ Proc=$_.Name; Count=$_.Count; Remotes=(($_.Group.Remote | Select-Object -Unique -First 5) -join ', ') } })
$listen = Get-NetTCPConnection -State Listen | Where-Object { $_.LocalAddress -notmatch '^(127\.|::1)' } | ForEach-Object { $pr = $procs | Where-Object Id -eq $_.OwningProcess; [PSCustomObject]@{ Port=$_.LocalPort; Proc=$pr.Name; Path=$pr.Path } } | Sort-Object Port -Unique
$report.listening = @($listen)
$serverSeen = @{}
foreach ($l in $listen) {
    if ($l.Path -and $l.Path -notlike 'C:\Windows\*' -and -not (In-UserDir $l.Path) -and -not $serverSeen[$l.Path]) {
        $serverSeen[$l.Path] = $true
        $ports = ($listen | Where-Object Path -eq $l.Path | ForEach-Object Port) -join ', '
        Add-Finding YELLOW 'Сеть' "Программа принимает подключения из сети: $($l.Proc) ($($l.Path)), порты $ports" 'Это сервер: к компьютеру можно подключиться снаружи. Нормально, только если вы его сами ставили и он вам нужен' 'Если не знаете, что это, — остановить службу и удалить программу' }
}
foreach ($l in $listen) { if ($l.Path -and (In-UserDir $l.Path)) { Add-Finding YELLOW 'Сеть' "Программа из пользовательской папки слушает порт $($l.Port): $($l.Proc) ($($l.Path))" 'Открытый порт = кто-то может подключиться снаружи (бэкдор, удалённый доступ)' 'Если это не ваш сервер/скрипт — завершить и удалить' } }

# --- 4. Автозагрузка и закрепление --------------------------------------------
Write-Host "4/10 Автозагрузка, задачи, службы, WMI..."
$auto = New-Object System.Collections.Generic.List[object]
foreach ($k in 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run','HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce','HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run','HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run','HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce') {
    $v = Get-ItemProperty $k; if ($v) { $v.PSObject.Properties | Where-Object { $_.Name -notlike 'PS*' } | ForEach-Object { $auto.Add([PSCustomObject]@{ Place="Реестр $k"; Name=$_.Name; Cmd=$_.Value }) } }
}
foreach ($d in "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup","$env:ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp") {
    Get-ChildItem $d -File | ForEach-Object {
        $target = $_.FullName
        if ($_.Extension -eq '.lnk') { $target = (New-Object -ComObject WScript.Shell).CreateShortcut($_.FullName).TargetPath }
        $auto.Add([PSCustomObject]@{ Place='Папка Автозагрузка'; Name=$_.Name; Cmd=$target }) }
}
# Winlogon / Image File Execution Options — классические места закрепления
$wl = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon'
if ($wl.Shell -and $wl.Shell -ne 'explorer.exe') { Add-Finding RED 'Закрепление' "Winlogon Shell подменён: $($wl.Shell)" 'Вместо рабочего стола Windows запускает чужую программу' 'Вернуть значение explorer.exe' }
if ($wl.Userinit -and $wl.Userinit -notmatch '^C:\\Windows\\system32\\userinit\.exe,?$') { Add-Finding RED 'Закрепление' "Winlogon Userinit подменён: $($wl.Userinit)" 'Запускается при каждом входе до всего остального' 'Вернуть C:\Windows\system32\userinit.exe,' }
Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options' | ForEach-Object { $dbg = (Get-ItemProperty $_.PSPath).Debugger; if ($dbg) { Add-Finding RED 'Закрепление' "Перехват запуска $($_.PSChildName) → $dbg" 'Вместо программы запускается другая' 'Удалить параметр Debugger' } }

$tasks = Get-ScheduledTask | Where-Object { $_.State -ne 'Disabled' } | ForEach-Object {
    $t = $_; foreach ($a in $t.Actions) { if ($a.Execute) { [PSCustomObject]@{ Place="Задача $($t.TaskPath)$($t.TaskName)"; Name=$t.TaskName; Cmd=("$($a.Execute) $($a.Arguments)").Trim(); Author=$t.Author } } }
}
$tasks | ForEach-Object { $auto.Add($_) }
$svcs = Get-CimInstance Win32_Service | Where-Object { $_.PathName -and $_.PathName -notlike 'C:\Windows\*' -and $_.PathName -notlike '"C:\Windows\*' }
$svcs | ForEach-Object { $auto.Add([PSCustomObject]@{ Place="Служба $($_.Name) ($($_.StartMode))"; Name=$_.DisplayName; Cmd=$_.PathName }) }
$report.autostart = $auto.ToArray()

foreach ($a in $auto) {
    $exe = ($a.Cmd -replace '^"([^"]+)".*','$1' -replace '^(\S+\.exe).*','$1')
    $exe = [Environment]::ExpandEnvironmentVariables($exe)
    if ($a.Cmd -match $knownBadNames) { Add-Finding RED 'Автозагрузка' "$($a.Place): $($a.Cmd)" 'Имя майнера' 'Удалить запись и файл' ; continue }
    if ($a.Cmd -match $suspArgs -and $a.Cmd -match $lolbins) { Add-Finding RED 'Автозагрузка' "$($a.Place): $($a.Cmd.Substring(0,[math]::Min(220,$a.Cmd.Length)))" 'Скрытая/закодированная команда при старте — так закрепляются вирусы' 'Раскодировать команду, удалить запись'; continue }
    if ((In-UserDir $exe) -and $exe -match '\.(exe|dll|vbs|js|bat|cmd|ps1|hta|scr)$') {
        $sig = Sig $exe
        if ($sig -like 'НЕ подписан*') { Add-Finding YELLOW 'Автозагрузка' "$($a.Place): $exe — $sig" 'Неподписанная программа из пользовательской папки стартует сама' 'Узнать, что это; незнакомое — отключить и удалить' }
        elseif ($sig -eq 'нет файла') { Add-Finding INFO 'Автозагрузка' "$($a.Place): файла уже нет ($exe)" 'Мёртвая запись' 'Удалить запись, чтобы не мусорила' }
    }
    if ($a.Place -like 'Задача*' -and $a.Cmd -match '\.(vbs|js|hta|bat|cmd|ps1)( |$)' -and $a.Author -notmatch 'Microsoft') { Add-Finding YELLOW 'Автозагрузка' "$($a.Place): $($a.Cmd)" 'Задача планировщика запускает скрипт' 'Открыть файл скрипта и посмотреть, что он делает' }
}
# WMI-подписки — скрытый способ автозапуска, обычным людям не нужен
$wmi = Get-CimInstance -Namespace root\subscription -ClassName __EventConsumer | Where-Object { $_.CommandLineTemplate -or $_.ScriptText }
foreach ($w in $wmi) { Add-Finding RED 'Закрепление' "WMI-подписка $($w.Name): $($w.CommandLineTemplate)$($w.ScriptText)" 'Невидимый автозапуск через WMI — почти всегда вредонос' 'Удалить подписку (Remove-CimInstance), проверить что она запускала' }
$report.wmi = @($wmi | Select-Object Name, CommandLineTemplate, ScriptText)

# --- 5. hosts, DNS, прокси ----------------------------------------------------
Write-Host "5/10 hosts, DNS, прокси..."
$hosts = Get-Content C:\Windows\System32\drivers\etc\hosts | Where-Object { $_ -match '^\s*[0-9a-fA-F:.]+\s+\S' -and $_ -notmatch '^\s*#' }
$report.hosts = [ordered]@{ count = @($hosts).Count; first = (@($hosts) | Select-Object -First 30) -join "`n" }
$hostsReal = @($hosts | Where-Object { $_ -notmatch 'localhost' })
$hostsAdobe = @($hostsReal | Where-Object { $_ -match '^\s*(0\.0\.0\.0|127\.0\.0\.1)\s+\S*(adobe|demdex|omtrdc|licensingstack|adobejanus)' })
$hostsBlock = @($hostsReal | Where-Object { $_ -match '^\s*(0\.0\.0\.0|127\.0\.0\.1)\s' -and $_ -notin $hostsAdobe })
$hostsRedirect = @($hostsReal | Where-Object { $_ -notmatch '^\s*(0\.0\.0\.0|127\.0\.0\.1|::1?)\s' })
if ($hostsAdobe.Count) { Add-Finding INFO 'Сеть' "В hosts заблокировано $($hostsAdobe.Count) адресов Adobe" 'Так делают «активаторы» нелицензионных Photoshop/Acrobat, чтобы программа не проверяла лицензию. Сам файл безвреден, но такие активаторы — частый источник вирусов и майнеров' 'Если ставили взломанный Adobe — запустить полную проверку Защитником (-Scan full)' }
if ($hostsBlock.Count) { Add-Finding YELLOW 'Сеть' "В hosts заблокировано ещё $($hostsBlock.Count) адресов: $(($hostsBlock | Select-Object -First 5) -join '; ')" 'Вирусы так блокируют сайты антивирусов и обновления Windows' 'Посмотреть список в C:\Windows\System32\drivers\etc\hosts; незнакомое удалить' }
foreach ($h in $hostsRedirect) { Add-Finding RED 'Сеть' "hosts перенаправляет сайт на другой адрес: $h" 'Так подменяют банк, почту или соцсеть на поддельную страницу' 'Удалить строку из hosts, сменить пароли от этого сайта' }
$dns = Get-DnsClientServerAddress -AddressFamily IPv4 | Where-Object { $_.ServerAddresses } | ForEach-Object { "$($_.InterfaceAlias): $($_.ServerAddresses -join ', ')" }
$report.dns = @($dns)
$proxy = Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings'
$report.proxy = [ordered]@{ enabled=$proxy.ProxyEnable; server=$proxy.ProxyServer; autoconfig=$proxy.AutoConfigURL }
if ($proxy.ProxyEnable -eq 1 -and $proxy.ProxyServer -notmatch '127\.0\.0\.1|localhost') { Add-Finding YELLOW 'Сеть' "Включён системный прокси: $($proxy.ProxyServer)" 'Весь трафик идёт через чужой сервер — так перехватывают пароли' 'Если это не ваш VPN — отключить: Параметры → Сеть → Прокси' }
if ($proxy.AutoConfigURL) { Add-Finding YELLOW 'Сеть' "Автонастройка прокси (PAC): $($proxy.AutoConfigURL)" 'Скрипт может перенаправлять часть сайтов' 'Если не ваш — убрать' }

# --- 6. Расширения Chrome -----------------------------------------------------
Write-Host "6/10 Расширения браузеров..."
$ext = foreach ($prof in (Get-ChildItem "$env:LOCALAPPDATA\Google\Chrome\User Data" -Directory | Where-Object { $_.Name -match '^(Default|Profile \d+)$' })) {
    foreach ($e in (Get-ChildItem "$($prof.FullName)\Extensions" -Directory)) {
        $ver = Get-ChildItem $e.FullName -Directory | Select-Object -First 1
        $m = Get-Content "$($ver.FullName)\manifest.json" -Raw -Encoding UTF8 | ConvertFrom-Json
        $name = $m.name
        if ($name -like '__MSG_*') {
            $key = $name -replace '__MSG_(.+)__','$1'
            foreach ($lang in @('ru', $m.default_locale, 'en', 'en_US')) {
                if (-not $lang) { continue }
                $f = "$($ver.FullName)\_locales\$lang\messages.json"
                if (Test-Path $f) { $loc = Get-Content $f -Raw -Encoding UTF8 | ConvertFrom-Json; $hit = $loc.PSObject.Properties | Where-Object { $_.Name -ieq $key } | Select-Object -First 1; if ($hit) { $name = $hit.Value.message; break } }
            }
            if ($name -like '__MSG_*') { $name = "без названия (id $($e.Name))" }
        }
        [PSCustomObject]@{ Profile=$prof.Name; Id=$e.Name; Name=$name; Perms=(($m.permissions | Where-Object { $_ -is [string] }) -join ', ') }
    }
}
$report.chromeExtensions = @($ext)
$vpnExt = @($ext | Where-Object { $_.Perms -match '(^|, )proxy(,|$)' } | Group-Object Name)
foreach ($g in $vpnExt) { Add-Finding YELLOW 'Браузер' "VPN-расширение «$($g.Name)»" 'Бесплатный VPN в браузере пропускает через свои серверы все сайты, которые вы открываете, и может их читать. Многие бесплатные VPN зарабатывают продажей этих данных' 'Оставить одно, которому доверяете, остальные удалить в chrome://extensions' }
$ext = @($ext | Where-Object { $_.Perms -notmatch '(^|, )proxy(,|$)' })
foreach ($e in $ext) { if ($e.Perms -match '<all_urls>|webRequest|clipboardRead|nativeMessaging|debugger' -and $e.Name -notmatch 'Google|Docs|Sheets|Slides|Claude|uBlock|AdGuard|Translate|LastPass|Bitwarden|1Password') {
    Add-Finding INFO 'Браузер' "Расширение «$($e.Name)» ($($e.Profile)) с широкими правами: $($e.Perms)" 'Расширения с доступом ко всем сайтам видят пароли и переписку' 'Оставить только те, которыми пользуетесь: chrome://extensions' } }

# --- 7. Свежие исполняемые файлы в пользовательских папках -------------------
Write-Host "7/10 Свежие exe/dll в Temp, AppData, ProgramData..."
$recent = foreach ($d in @("$env:TEMP","$env:APPDATA","$env:LOCALAPPDATA",'C:\ProgramData','C:\Users\Public','C:\Windows\Temp')) {
    Get-ChildItem $d -Recurse -File -Include *.exe,*.dll,*.scr,*.vbs,*.hta,*.bat,*.ps1 -Depth 3 | Where-Object { $_.LastWriteTime -gt (Get-Date).AddDays(-7) -and $_.FullName -notmatch '\\(Google|Microsoft|Anthropic|Claude|Python|node_modules|venv|\.venv|pip|npm|Programs\\(cursor|whimsical|Comfy)|Package Cache|dolphin_anty|JetBrains|Telegram|Discord|Zoom|Yandex|Opera|Mozilla|NVIDIA|Intel|GitHub|stealth-browser|claude_widget|Temp\\claude)\\' }
}
$report.recentExecutables = @($recent | Select-Object FullName, LastWriteTime, Length | Sort-Object LastWriteTime -Descending | Select-Object -First 40)
$unsignedRecent = $recent | Where-Object { $_.Extension -in '.exe','.dll','.scr' } | Where-Object { (Sig $_.FullName) -like 'НЕ подписан*' } | Select-Object -First 15
foreach ($f in $unsignedRecent) { Add-Finding INFO 'Файлы' "Свежий неподписанный файл: $($f.FullName) ($($f.LastWriteTime))" 'Появился за последнюю неделю в папке, куда вирусы любят ставиться' 'Если не узнаёте — проверить хэш на virustotal.com (SHA256 в json-отчёте)' }

# --- 8. Прочее: UAC, RDP, скрытые пользователи, удалённый доступ ---------------
Write-Host "8/10 UAC, удалённый доступ, пользователи..."
$uac = (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System').EnableLUA
if ($uac -ne 1) { Add-Finding RED 'Система' 'Контроль учётных записей (UAC) выключен' 'Любая программа получает права администратора без вопроса' 'Включить UAC: Панель управления → Учётные записи → Изменить параметры контроля' }
$rdp = (Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server').fDenyTSConnections
if ($rdp -eq 0) { Add-Finding YELLOW 'Система' 'Включён удалённый рабочий стол (RDP)' 'Снаружи можно подключиться по паролю' 'Если не пользуетесь — выключить: Параметры → Система → Удалённый рабочий стол' }
Write-Host "   пользователи..."
$users = Get-LocalUser | Where-Object Enabled | Select-Object Name, @{n='LastLogon';e={"$($_.LastLogon)"}}
Write-Host "   программы удалённого доступа..."
$report.users = @($users)
foreach ($u in $users) { if ($u.Name -notin 'User' -and $u.Name -notmatch 'Администратор|Administrator|Гость|Guest|DefaultAccount|WDAGUtilityAccount') { Add-Finding YELLOW 'Система' "Дополнительный включённый пользователь: $($u.Name)" 'Лишняя учётная запись = чужой вход' 'Если не создавали — отключить' } }
$remoteTools = Get-Process | Where-Object { $_.Name -match 'anydesk|teamviewer|rustdesk|rudesktop|ammyy|radmin|ultraviewer|supremo|aeroadmin|litemanager|getscreen|vnc' }
foreach ($r in $remoteTools) { Add-Finding YELLOW 'Удалённый доступ' "Запущена программа удалённого доступа: $($r.Name) ($($r.Path))" 'Через неё компьютером можно управлять со стороны' 'Если сейчас никому доступ не давали — закрыть и удалить' }
$remoteInstalled = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*','HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*','HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*' | Where-Object { $_.DisplayName -match 'anydesk|teamviewer|rustdesk|rudesktop|ammyy|radmin|ultraviewer|supremo|aeroadmin|litemanager|vnc' } | Select-Object -ExpandProperty DisplayName
foreach ($r in $remoteInstalled) { Add-Finding INFO 'Удалённый доступ' "Установлена программа удалённого доступа: $r" 'Сама по себе не вредна, но это дверь в компьютер' 'Держать только если нужна' }

# --- 9. Папки скиллов и плагинов Claude (12.10: троян пережил переустановку внутри SKILL.md из бэкапа) -----
Write-Host "9/10 Скиллы и плагины Claude..."
$claudeDir = "$env:USERPROFILE\.claude"; $skillsDir = "$claudeDir\skills"; $pluginsDir = "$claudeDir\plugins"
$mirror = "$env:USERPROFILE\skills-archive"   # git-копия скиллов (viiiitaaaaa/skills-archive), её делает sync_skills.ps1
$git = (Get-Command git -ErrorAction SilentlyContinue).Source
$skillFiles = @(Get-ChildItem $skillsDir -Recurse -File -Force | Where-Object { $_.FullName -notmatch '\\\.git\\' })
$report.skills = [ordered]@{ files = $skillFiles.Count }
# a) бинарники в скиллах и плагинах — скиллу они не нужны
$bin = @(Get-ChildItem $skillsDir, $pluginsDir -Recurse -File -Force -Include *.exe,*.dll,*.scr,*.com,*.msi,*.hta,*.vbs,*.lnk,*.jar,*.node | Where-Object { $_.FullName -notmatch '\\\.git\\' })
foreach ($b in $bin) { Add-Finding YELLOW 'Скиллы Claude' "Исполняемый файл в папке скиллов/плагинов: $($b.FullName)" 'Скиллу нужны только тексты и скрипты; программа внутри скилла — способ спрятать вредонос, который Claude запустит сам' 'Узнать, откуда он; хэш проверить на virustotal.com. Ничего не удалять без её слова' }
# b) сверка с GitHub-копией: что изменилось или появилось после последней синхронизации
if ($git -and (Test-Path "$mirror\.git")) {
    # копия = рабочая папка claude-skills\skills; сначала убедиться, что она совпадает с тем, что ушло на GitHub
    $dirty = @(& $git -c safe.directory=* -C $mirror status --porcelain -- skills 2>$null)
    if ($dirty.Count) { Add-Finding YELLOW 'Скиллы Claude' "Копия скиллов claude-skills отличается от последнего коммита: $($dirty.Count) файлов" 'Сверять не с чем: копию правили мимо sync_skills.ps1' 'Посмотреть git status в claude-skills' }
    # побайтно (SHA256): git-хэш файла вне репозитория не учитывает перевод строк CRLF и даёт ложные «изменён»
    $changed = New-Object System.Collections.Generic.List[object]
    foreach ($f in $skillFiles) {
        $rel = 'skills\' + $f.FullName.Substring($skillsDir.Length + 1)
        $copy = Join-Path $mirror $rel
        $state = if (-not (Test-Path -LiteralPath $copy)) { 'новый' } elseif ((Get-FileHash -LiteralPath $f.FullName).Hash -ne (Get-FileHash -LiteralPath $copy).Hash) { 'изменён' } else { $null }
        if ($state) { $changed.Add([PSCustomObject]@{ File=$rel; State=$state; Time=$f.LastWriteTime }) }
    }
    $report.skills.changedVsGitHub = $changed.ToArray()
    $scr = @($changed | Where-Object { $_.File -match '\.(ps1|bat|cmd|sh|py|js|mjs|vbs)$' })
    foreach ($c in ($scr | Select-Object -First 15)) { Add-Finding YELLOW 'Скиллы Claude' "Скрипт скилла $($c.State) после последней синхронизации: $($c.File) ($($c.Time))" 'Скрипт скилла Claude запускает сам. Если правили не мы — это подмена' 'Если правку делали мы — запустить sync_skills.ps1; если нет — сравнить с GitHub-копией (git diff в claude-skills)' }
    if ($scr.Count -gt 15) { Add-Finding YELLOW 'Скиллы Claude' "Ещё изменённых скриптов скиллов: $($scr.Count - 15) (список в json)" 'См. выше' 'См. выше' }
    $txt = @($changed | Where-Object { $_.File -notmatch '\.(ps1|bat|cmd|sh|py|js|mjs|vbs)$' })
    if ($txt.Count) { Add-Finding INFO 'Скиллы Claude' "Тексты скиллов, изменённые/новые после синхронизации: $($txt.Count) (например: $((($txt | Select-Object -First 5).File) -join '; '))" 'Обычно это наши свежие правки' 'Запустить sync_skills.ps1; незнакомое — сверить с GitHub-копией' }
} else { Add-Finding INFO 'Скиллы Claude' 'Сверка с GitHub-копией не сделана' "Нет git или папки $mirror" 'Проверить установку git и копию скиллов' }
# c) закладки в скриптах скиллов: скачать-и-запустить, закодированные команды, длинные base64-куски
$payload = '(iwr|Invoke-WebRequest|curl|wget|DownloadString)[^|\r\n]{0,200}\|\s*(iex|bash|sh|powershell|pwsh)\b|-enc(odedcommand)?\s+[A-Za-z0-9+/=]{40,}|[A-Za-z0-9+/]{400,}={0,2}'
foreach ($f in ($skillFiles | Where-Object { $_.Extension -match '^\.(ps1|bat|cmd|sh|py|js|mjs|vbs)$' -or $_.Name -eq 'SKILL.md' })) {
    $hit = Select-String -Path $f.FullName -Pattern $payload -List
    if ($hit -and -not ($f.Name -eq 'SKILL.md' -and $hit.Line -match '`[^`]*(iwr|curl|wget)[^`]*`')) {
        Add-Finding YELLOW 'Скиллы Claude' "Подозрительная строка в $($f.FullName):$($hit.LineNumber): $($hit.Line.Trim().Substring(0, [math]::Min(150, $hit.Line.Trim().Length)))" 'Так прячут команду «скачать и запустить» или зашифрованную программу' 'Прочитать строку: если это не наш код — сверить с GitHub-копией' }
}
# d) плагины: какие стоят и у каких есть хуки (хук запускается сам при событиях Claude Code)
$plug = Get-Content "$pluginsDir\installed_plugins.json" -Raw -Encoding UTF8 | ConvertFrom-Json
$plugNames = @($plug.plugins.PSObject.Properties.Name)
$hooks = @(Get-ChildItem "$pluginsDir\cache" -Recurse -File -Filter hooks.json | ForEach-Object { $_.FullName.Substring($pluginsDir.Length + 1) })
$report.skills.plugins = $plugNames; $report.skills.pluginHooks = $hooks
if ($plugNames) { Add-Finding INFO 'Скиллы Claude' "Плагины Claude Code: $($plugNames -join ', '); файлы хуков: $(if ($hooks) { $hooks -join '; ' } else { 'нет' })" 'Хук плагина запускает команды сам, без вопроса' 'Держать только плагины, которые она одобрила' }

# --- 10. Ключи в истории наших git-репозиториев (12.10: украденный .env, ключи в старых коммитах) -----
Write-Host "10/10 Ключи в истории git-репозиториев..."
$keyPat = 'sk-ant-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9]{32,}|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{35}|xox[abprs]-[A-Za-z0-9-]{10,}|[0-9]{8,10}:AA[A-Za-z0-9_-]{30,}|apify_api_[A-Za-z0-9]{20,}|shp(at|ss|ca|pa)_[a-fA-F0-9]{32}|-----BEGIN [A-Z ]*PRIVATE KEY'
$repoDirs = @(Get-ChildItem $env:USERPROFILE, "$env:USERPROFILE\AppData\Local", $skillsDir -Directory -Force | Where-Object { Test-Path "$($_.FullName)\.git" } | ForEach-Object FullName)
$repoRows = New-Object System.Collections.Generic.List[object]
if ($git) {
    foreach ($r in $repoDirs) {
        $origin = & $git -c safe.directory=* -C $r remote get-url origin 2>$null
        if ($origin -notmatch 'viiiitaaaaa') { continue }   # только наши репозитории
        $log = & $git -c safe.directory=* -C $r log --all -p -E -G $keyPat --format='@@@%h %ad' --date=short 2>$null
        $commit = ''; $hits = @{}
        foreach ($line in $log) {
            if ($line -like '@@@*') { $commit = $line.Substring(3); continue }
            if ($line -match '^\+' -and $line -match $keyPat) { $k = $matches[0]; $mask = $k.Substring(0, [math]::Min(6, $k.Length)) + '***'; if (-not $hits[$mask]) { $hits[$mask] = $commit } }
        }
        $envs = @(& $git -c safe.directory=* -C $r log --all --name-only --format= 2>$null | Where-Object { $_ -match '(^|/)\.env(\.|$)' -and $_ -notmatch 'example|sample|template' } | Sort-Object -Unique)
        $repoRows.Add([PSCustomObject]@{ Repo=$r; Origin=$origin; Keys=@($hits.Keys); Env=$envs })
        foreach ($m in $hits.Keys) { Add-Finding RED 'Ключи в git' "В истории $r ($origin) есть ключ $m (коммит $($hits[$m]))" 'Ключ из старого коммита виден всем, у кого есть доступ к репозиторию, даже если в файле его уже нет' 'Перевыпустить (отозвать) этот ключ у сервиса; историю git без её слова не переписывать' }
        foreach ($e in $envs) { Add-Finding YELLOW 'Ключи в git' "Файл $e когда-то попал в git: $r" 'В .env лежат ключи; если он был в коммите — ключи могли утечь' 'Посмотреть, какие ключи там были, и перевыпустить их; .env — в .gitignore' }
    }
} else { Add-Finding INFO 'Ключи в git' 'Поиск ключей в git не сделан' 'git не найден' 'Установить git или запустить из Git Bash' }
$report.gitSecrets = $repoRows.ToArray()

# --- Отчёт ----------------------------------------------------------------------
$red = @($findings | Where-Object level -eq 'RED'); $yel = @($findings | Where-Object level -eq 'YELLOW'); $inf = @($findings | Where-Object level -eq 'INFO')
$verdict = if ($red.Count) { '🔴 Есть признаки заражения — нужно разбираться' } elseif ($yel.Count) { '🟡 Явного вредоноса нет, но есть что проверить' } else { '🟢 Чисто' }
$report.findings = $findings.ToArray(); $report.verdict = $verdict; $report.isAdmin = $isAdmin; $report.time = (Get-Date).ToString('s')
Write-Host "Сохраняю отчёт..."
foreach ($k in @($report.Keys)) { $t0 = Get-Date; $null = $report[$k] | ConvertTo-Json -Depth 4 -Compress; $dt = ((Get-Date) - $t0).TotalSeconds; if ($dt -gt 2) { Write-Host "   медленный раздел json: $k ($([math]::Round($dt)) с)" } }
$report | ConvertTo-Json -Depth 4 | Set-Content $jsonPath -Encoding UTF8
Write-Host "json готов"

$sb = New-Object Text.StringBuilder
[void]$sb.AppendLine("# Проверка компьютера — $(Get-Date -Format 'dd.MM.yyyy HH:mm')")
[void]$sb.AppendLine("`n**Вердикт: $verdict**`n")
[void]$sb.AppendLine("Красных: $($red.Count) · Жёлтых: $($yel.Count) · Для сведения: $($inf.Count) · Права администратора: $isAdmin`n")
foreach ($lvl in @(@('RED','🔴 Красное — вероятный вредонос'), @('YELLOW','🟡 Жёлтое — проверить'), @('INFO','⚪ Для сведения'))) {
    $items = $findings | Where-Object level -eq $lvl[0]
    if ($items) { [void]$sb.AppendLine("## $($lvl[1])`n"); foreach ($f in $items) { [void]$sb.AppendLine("- **[$($f.area)]** $($f.what)`n  - Почему важно: $($f.why)`n  - Что делать: $($f.action)") }; [void]$sb.AppendLine() }
}
[void]$sb.AppendLine("## Защитник Windows`n- Включён: $($mp.AntivirusEnabled), реальное время: $($mp.RealTimeProtectionEnabled), защита от отключения: $($mp.IsTamperProtected)`n- Базы: $($mp.AntivirusSignatureLastUpdated); быстрая проверка: $($mp.QuickScanEndTime); полная: $($mp.FullScanEndTime)`n")
[void]$sb.AppendLine("## Нагрузка на процессор за $Seconds с (топ)`n| Процесс | CPU % | Память МБ | Путь |`n|---|---|---|---|")
foreach ($p in $report.cpuTop) { [void]$sb.AppendLine("| $($p.Name) | $($p.CpuPct) | $($p.MemMB) | $($p.Path) |") }
[void]$sb.AppendLine("`n## Память (топ по программам)`n| Программа | Процессов | МБ |`n|---|---|---|")
foreach ($p in $report.memTop) { [void]$sb.AppendLine("| $($p.Name) | $($p.Count) | $($p.MemMB) |") }
[void]$sb.AppendLine("`n## Кто ходит в интернет`n| Программа | Соединений | Куда (примеры) |`n|---|---|---|")
foreach ($c in $report.connections) { [void]$sb.AppendLine("| $($c.Proc) | $($c.Count) | $($c.Remotes) |") }
[void]$sb.AppendLine("`n## Открытые порты (слушают снаружи)`n| Порт | Программа | Путь |`n|---|---|---|")
foreach ($l in $report.listening) { [void]$sb.AppendLine("| $($l.Port) | $($l.Proc) | $($l.Path) |") }
[void]$sb.AppendLine("`n## Автозагрузка (всё, что стартует само)`n| Где | Имя | Команда |`n|---|---|---|")
foreach ($a in $report.autostart | Where-Object { $_.Place -notlike 'Задача \Microsoft*' }) { [void]$sb.AppendLine("| $($a.Place) | $($a.Name) | $("$($a.Cmd)" -replace '\|','/' -replace '^(.{120}).+$','$1…') |") }
[void]$sb.AppendLine("`n## Расширения Chrome`n| Профиль | Название | Права |`n|---|---|---|")
foreach ($e in $report.chromeExtensions) { [void]$sb.AppendLine("| $($e.Profile) | $($e.Name) | $($e.Perms) |") }
[void]$sb.AppendLine("`n## hosts / DNS / прокси`n- hosts: $(if ($hosts) { "$(@($hosts).Count) строк (подробности выше)" } else { 'пусто (норма)' })`n- DNS: $($dns -join '; ')`n- Прокси: $(if ($proxy.ProxyEnable -eq 1) { $proxy.ProxyServer } else { 'выключен' })")
[void]$sb.AppendLine("`nСырые данные: $jsonPath")
$sb.ToString() | Set-Content $md -Encoding UTF8

Write-Host "`n$verdict"
Write-Host "Красных: $($red.Count), жёлтых: $($yel.Count), для сведения: $($inf.Count)"
foreach ($f in $red) { Write-Host "  🔴 [$($f.area)] $($f.what)" }
foreach ($f in $yel) { Write-Host "  🟡 [$($f.area)] $($f.what)" }
Write-Host "Отчёт: $md"
