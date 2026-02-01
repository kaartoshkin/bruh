$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

$py = Join-Path $root ".venv\Scripts\python.exe"
$results = Join-Path $root "reports\allure-results"

Remove-Item -Recurse -Force $results -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Force -Path $results | Out-Null

& $py -m pytest --alluredir=$results -q
allure serve $results
