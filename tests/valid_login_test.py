import pytest

from bruh.pages.login_page import LoginPage

class TestValidLogin:
    @pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"),
                                                    ("locked_out_user", "secret_sauce"),
                                                    ("problem_user", "secret_sauce"),
                                                    ("performance_glitch_user", "secret_sauce"),
                                                    ("error_user", "secret_sauce"),
                                                    ("problem_user", "secret_sauce")])
    def test_valid_login(self, driver, username, password):
        login_page = LoginPage(driver)
        login_page.login(username, password)
        login_page.wait_url_contains("inventory")