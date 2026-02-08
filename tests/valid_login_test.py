import pytest
import allure
from pages.internet_page import InternetPage

# Test for valid login credentials
@pytest.mark.smoke
def test_login_valid_credentials(driver):

    with allure.step("Open the login page"):
        page = InternetPage(driver)
        page.open()

    with allure.step(f"Login with username: 'tomsmith' and password: 'SuperSecretPassword!'"):
        page.login_with_valid_credentials()

    with allure.step("Verify the flash message"):
        flash_message = page.get_flash_message()
        assert 'You logged into a secure area!' in flash_message
    
    with allure.step("Verify the URL"):
        page.wait_url_contains("/secure")
        assert "/secure" in driver.current_url

# Test for logout functionality
@pytest.mark.smoke
def test_login_and_logout(driver):

    with allure.step("Open the login page"):
        page = InternetPage(driver)
        page.open()

    with allure.step(f"Login with username: 'tomsmith' and password: 'SuperSecretPassword!'"):
        page.login_with_valid_credentials()

    with allure.step("Logout"):
        page.logout()

    with allure.step("Verify the flash message"):
        flash_message = page.get_flash_message()
        assert 'You logged out of the secure area!' in flash_message
    
    with allure.step("Verify the URL"):
        page.wait_url_contains("/login")
        assert "/login" in driver.current_url