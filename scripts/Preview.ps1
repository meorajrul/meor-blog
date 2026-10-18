param([int]$Port = 1314, [switch]$IncludeDrafts, [switch]$InstallOnly)
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true
$blogRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $blogRoot
$blogVersion = (Get-Content -LiteralPath 'site/dependencies.json' -Raw | ConvertFrom-Json).hugo
$blogTool = Join-Path $blogRoot '.tools/hugo/hugo.exe'
if (-not (Test-Path -LiteralPath $blogTool)) {
    if (-not [Environment]::Is64BitOperatingSystem) { throw 'This helper requires Windows x64. Install the pinned Hugo version for your platform manually.' }
    New-Item -ItemType Directory -Path '.tools/hugo' -Force | Out-Null
    $blogAsset = "hugo_${blogVersion}_windows-amd64.zip"
    $blogRelease = "https://github.com/gohugoio/hugo/releases/download/v$blogVersion"
    Invoke-WebRequest "$blogRelease/$blogAsset" -OutFile '.tools/hugo.zip'
    Invoke-WebRequest "$blogRelease/hugo_${blogVersion}_checksums.txt" -OutFile '.tools/hugo-checksums.txt'
    $blogActual = (Get-FileHash '.tools/hugo.zip' -Algorithm SHA256).Hash.ToLower()
    $blogPattern = '^([a-f0-9]+)\s+' + [regex]::Escape($blogAsset) + '$'
    $blogExpected = (Select-String -Path '.tools/hugo-checksums.txt' -Pattern $blogPattern).Matches.Groups[1].Value
    if (-not $blogExpected -or $blogActual -ne $blogExpected) { throw 'Hugo checksum verification failed.' }
    Expand-Archive -LiteralPath '.tools/hugo.zip' -DestinationPath '.tools/hugo' -Force
}
$blogVersionText = & $blogTool version
if ($blogVersionText -notlike "hugo v$blogVersion-*") { throw "Expected Hugo $blogVersion; found $blogVersionText" }
Write-Output $blogVersionText
if ($InstallOnly) { return }
$blogArgs = @('server', '--source', 'site', '--environment', 'development', '--bind', '127.0.0.1', '--port', "$Port", '--baseURL', "http://localhost:$Port/", '--appendPort=false', '--disableFastRender', '--renderToMemory', '--poll', '700ms')
if ($IncludeDrafts) { $blogArgs += '--buildDrafts' }
Write-Output 'Preview only. Stop with Ctrl+C. This does not publish.'
& $blogTool @blogArgs
