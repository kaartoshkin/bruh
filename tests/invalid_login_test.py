import pytest
from selenium.webdriver.common.by import By


from bruh.pages.login_page import LoginPage

class TestInvalidLogin:
    @pytest.mark.parametrize("username, password", [("standard_user", "wrong_password"),
                                                    ("locked_out_user", ""),
                                                    ("", "secret_sauce")])

    def test_invalid_login(self, driver, username, password):
        login_page = LoginPage(driver)
        login_page.login(username, password)
        error_message = login_page.wait_element_visible((By.CSS_SELECTOR, "h3[data-test='error']"))
        assert error_message.is_displayed()