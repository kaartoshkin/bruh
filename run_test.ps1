param (
    [string]$TestPath
)

Remove-Item -Recurse -Force reports\allure-results -ErrorAction SilentlyContinue

python -m pytest $TestPath --alluredir=reports\allure-results

allure serve reports\allure-results
