# Give Hermes a task to execute autonomously on GPT (ChatGPT subscription) and save its report.
# Usage:
#   .\hermes-task.ps1 -BodyFile .\task.md -Tier fast -Dir "C:\path\to\project"
#   .\hermes-task.ps1 -BodyFile .\task.md -Tier std  -Dir "C:\path" -Report .\reports\task1.md
# Tiers: fast = simple/mechanical, std = normal work (default), deep = hard, use rarely.
# Run several copies in the background for independent tasks (different -Dir or different files).
param(
    [Parameter(Mandatory = $true)][string]$BodyFile,
    [ValidateSet('fast', 'std', 'deep')][string]$Tier = 'std',
    [string]$Dir = '',
    [string]$Report = ''
)

# The single place where tiers map to models. Change here when the model list changes.
$Models = @{
    fast = 'gpt-6-luna'
    std  = 'gpt-6.1-terra'
    deep = 'gpt-6.1-sol'
}

$hermes = Join-Path $env:LOCALAPPDATA 'hermes\bin\hermes.exe'
$body = Get-Content (Resolve-Path $BodyFile).Path -Raw -Encoding UTF8
# PowerShell 5.1 passes embedded double quotes to native programs unescaped, which splits the
# card into stray arguments. Escape them the way the C runtime parses a command line.
$body = [regex]::Replace($body, '(\\*)"', { param($m) ($m.Groups[1].Value * 2) + '\"' })
$body = [regex]::Replace($body, '(\\+)$', { param($m) $m.Groups[1].Value * 2 })
$cmd = @('-z', $body, '--provider', 'openai-codex', '-m', $Models[$Tier], '--skills', 'claude-executor')
if ($Dir) { $cmd += @('--in', (Resolve-Path $Dir).Path) }

$out = & $hermes @cmd
$code = $LASTEXITCODE
if ($Report) {
    $header = "<!-- tier=$Tier model=$($Models[$Tier]) exit=$code -->"
    [System.IO.File]::WriteAllLines($Report, @($header) + @($out), (New-Object System.Text.UTF8Encoding($false)))
}
$out
exit $code
