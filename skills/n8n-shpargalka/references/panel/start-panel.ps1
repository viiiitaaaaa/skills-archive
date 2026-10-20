# Операционная панель ARTMELLIO — http://localhost:8787
#
# Панель сама ничего не считает: она показывает сценарии из registry.json,
# читает состояние из базы n8n и запускает воркфлоу через вебхуки.
# Чтобы кнопки работали, n8n должен быть поднят: .\n8n\start-n8n.ps1
#
#   .\panel\start-panel.ps1

$ErrorActionPreference = 'Stop'
$env:PANEL_OPERATOR = $env:USERNAME
Set-Location (Split-Path $PSScriptRoot -Parent)
python panel\server.py
