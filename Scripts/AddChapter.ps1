param(
    [Parameter(Mandatory=$true)][string]$Slug,
    [Parameter(Mandatory=$true)][string]$Title,
    [string]$Part = 'Part06_Extensions',
    [string]$After,
    [string]$EngineRoot = 'C:\Program Files\Epic Games\UE_5.8'
)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path $PSScriptRoot -Parent
$python = Join-Path $EngineRoot 'Engine\Binaries\ThirdParty\Python3\Win64\python.exe'
if (-not (Test-Path -LiteralPath $python)) {
    throw "The Unreal Python runtime was not found. Set -EngineRoot to the UE 5.8 installation."
}
$arguments = @((Join-Path $PSScriptRoot 'manage_chapters.py'), '--slug', $Slug, '--title', $Title, '--part', $Part)
if ($After) {
    $arguments += @('--after', $After)
}
& $python @arguments
if ($LASTEXITCODE -ne 0) {
    throw 'Could not add the chapter. Inspect the reported error before retrying.'
}
& (Join-Path $PSScriptRoot 'BuildLab.ps1') -EngineRoot $EngineRoot
