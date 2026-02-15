import pytest
import allure
from pages.internet_page_dynamic_loading import InternetPage

class TestDynamicLoading:
    @pytest.mark.smoke
    def test_dynamic_loading_1(self, driver):
        with allure.step("Open the first dynamic loading page"):
            page = InternetPage(driver)
            page.open_first()

        with allure.step("Click the Start button"):
            page.click_start()

        with allure.step("Wait for the loading indicator to disappear"):
            page.wait_loading_indicator_not_visible()

        with allure.step("Verify the finish text is displayed"):
            assert page.get_finish_text() == "Hello World!"

    @pytest.mark.smoke
    def test_dynamic_loading_2(self, driver):
        with allure.step("Open the second dynamic loading page"):
            page = InternetPage(driver)
            page.open_second()

        with allure.step("Click the Start button"):
            page.click_start()

        with allure.step("Wait for the loading indicator to disappear"):
            page.wait_loading_indicator_not_visible()

        with allure.step("Verify the finish text is displayed"):
            assert page.get_finish_text() == "Hello World!"