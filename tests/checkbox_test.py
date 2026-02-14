import pytest
import allure
from pages.internet_page_dynamic_controls import InternetPage

# Test for adding and removing a checkbox

class TestCheckbox:
    @pytest.mark.smoke
    def test_add_and_remove_checkbox(self, driver):
        with allure.step("Open the Internet Page"):
            page = InternetPage(driver)
            page.open()

        with allure.step("Remove the checkbox"):
            page.remove_checkbox()

        with allure.step("Wait for the checkbox to be removed"):
            page.wait_checkbox_not_visible()

        with allure.step("Verify the message text"):
            assert page.get_message_text() == "It's gone!"
        
        with allure.step("Add the checkbox"):
            page.add_checkbox()

        with allure.step("Wait for the checkbox to be visible"):
            page.wait_checkbox_visible()

        with allure.step("Verify the message text"):
            assert "It's back!" in page.get_message_text()  