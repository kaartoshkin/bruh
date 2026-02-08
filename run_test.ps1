param (
    [string]$TestPath
)

python -m pytest $TestPath --alluredir=reports\allure-results

allure serve reports\allure-results
