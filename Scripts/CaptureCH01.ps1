param([string]$EngineRoot = 'C:\Program Files\Epic Games\UE_5.8')
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path $PSScriptRoot -Parent
$editor = Join-Path $EngineRoot 'Engine\Binaries\Win64\UnrealEditor.exe'
$projectFile = Join-Path $projectRoot 'RenderingLab.uproject'
$captureScript = Join-Path $projectRoot 'Content\Python\capture_ch01.py'
$logFile = Join-Path $projectRoot 'Saved\Logs\CH01Capture.log'
if (-not (Test-Path -LiteralPath $editor)) {
    throw "Unreal Editor was not found. Set -EngineRoot to the UE 5.8 installation."
}
# Use a regular visible editor viewport for diagnostic view-mode screenshots.
$execute = '-ExecCmds=py "' + $captureScript + '"'
$startedAt = [DateTime]::UtcNow
& $editor $projectFile $execute '-nop4' '-nosplash' '-NoSound' '-NoRestoreOpenAssetTabs' "-abslog=$logFile"
if ($LASTEXITCODE -ne 0) {
    throw "CH01 capture failed. See $logFile"
}
$manifestFile = Join-Path $projectRoot 'Docs\Images\CH01\CaptureManifest.json'
if (-not (Test-Path -LiteralPath $manifestFile) -or (Get-Item -LiteralPath $manifestFile).LastWriteTimeUtc -lt $startedAt) {
    throw "The capture session did not write a new manifest. See $logFile"
}
$manifest = Get-Content -Raw -LiteralPath $manifestFile | ConvertFrom-Json
if (-not $manifest.complete) {
    throw "Capture did not complete. See $logFile"
}
Write-Host 'CH01 screenshots saved in Docs/Images/CH01.'
