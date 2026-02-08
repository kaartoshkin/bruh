param (
    [string]$TestPath
)

Remove-Item -Recurse -Force reports\allure-results -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force reports\allure-report -ErrorAction SilentlyContinue

python -m pytest $TestPath --alluredir=reports\allure-results

allure generate reports\allure-results -o reports\allure-report --clean
allure open reports\allure-report
