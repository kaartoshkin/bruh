
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InternetPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_controls"

    CHECKBOX_INPUT = (By.CSS_SELECTOR, "input[type='checkbox']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "#checkbox-example > button:nth-child(2)")
    ADD_BUTTON = (By.CSS_SELECTOR, "#checkbox-example > button:nth-child(1)")
    MESSAGE_TEXT = (By.ID, "message")

    def open(self):
        self.driver.get(self.URL)

    def remove_checkbox(self):
        self.click(self.REMOVE_BUTTON)

    def add_checkbox(self):
        self.click(self.ADD_BUTTON)

    def get_message_text(self):
        return self.wait_element_visible(self.MESSAGE_TEXT).text
