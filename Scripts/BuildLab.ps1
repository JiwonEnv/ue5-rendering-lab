param(
    [string]$EngineRoot = 'C:\Program Files\Epic Games\UE_5.8'
)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path $PSScriptRoot -Parent
$editor = Join-Path $EngineRoot 'Engine\Binaries\Win64\UnrealEditor-Cmd.exe'
$projectFile = Join-Path $projectRoot 'RenderingLab.uproject'
$buildScript = Join-Path $projectRoot 'Content\Python\build_lab.py'
$logFile = Join-Path $projectRoot 'Saved\Logs\LabBuild.log'
if (-not (Test-Path -LiteralPath $editor)) {
    throw "Unreal Editor was not found at $editor. Set -EngineRoot to the UE 5.8 installation."
}
& $editor $projectFile '-run=pythonscript' "-script=$buildScript" '-unattended' '-nop4' '-nosplash' '-NullRHI' "-abslog=$logFile"
if ($LASTEXITCODE -ne 0) {
    throw "Level generation failed. See $logFile"
}
$success = Select-String -LiteralPath $logFile -Pattern 'LAB_BUILD_OK' -Quiet
if (-not $success) {
    throw "Level generation did not report success. See $logFile"
}
Write-Host "Starter maps verified. Log: $logFile"
