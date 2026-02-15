import pytest
import allure
from pages.internet_page_login import InternetPage
from selenium.webdriver.support import expected_conditions as EC


# Test for invalid login credentials

@pytest.mark.parametrize(
        "username, password, expected_message",
        [
            ("wrong", "wrong", "Your username is invalid!"),
            ("tomsmith", "wrong", "Your password is invalid!"),
            ("", "", "Your username is invalid!"),
        ]
)

@pytest.mark.smoke
def test_login_invalid_credentials(driver, username, password, expected_message):

    with allure.step("Open the login page"):
        page = InternetPage(driver)
        page.open()

    with allure.step(f"Login with username: '{username}' and password: '{password}'"):
        page.login(username, password)

    with allure.step("Verify the flash message"):
        flash_message = page.get_flash_message()
        assert expected_message in flash_message
    
    with allure.step("Verify the URL"):
        page.wait_url_contains("/login")
        assert "/login" in driver.current_url
