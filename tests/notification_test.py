import pytest
import allure
from pages.internet_page_notification import InternetPage

class TestNotificationMessage:
    @pytest.mark.smoke
    def test_notification_message(self, driver):
        with allure.step("Open the notification message page"):
            page = InternetPage(driver)
            page.open()

        with allure.step("Click the 'Click here' link and get the flash message"):
            flash_message = page.get_new_message()

        with allure.step("Verify that the flash message is one of the expected messages"):
            expected_messages = [
                "Action successful",
                "Action unsuccessful, please try again",
                "Action unsuccesful, please try again" # Note: The actual message have a mistake in "unsuccessful"
            ]
            assert flash_message in expected_messages, f"Unexpected flash message: '{flash_message}'"