
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InternetPage(BasePage):
    URL_1 = "https://the-internet.herokuapp.com/dynamic_loading/1"
    URL_2 = "https://the-internet.herokuapp.com/dynamic_loading/2"

    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    LOADING_INDICATOR = (By.ID, "loading")
    FINISH_TEXT = (By.ID, "finish")

    def open_first(self):
        self.driver.get(self.URL_1)

    def open_second(self):
        self.driver.get(self.URL_2)

    def click_start(self):
        self.click(self.START_BUTTON)

    def wait_loading_indicator_not_visible(self):
        self.wait_element_not_visible(self.LOADING_INDICATOR)

    def get_finish_text(self) -> str:
        finish_element = self.wait_element_visible(self.FINISH_TEXT)
        return finish_element.text.strip()
    

