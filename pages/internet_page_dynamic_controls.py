
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InternetPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_controls"

    CHECKBOX_INPUT = (By.CSS_SELECTOR, "input[type='checkbox']")
    BUTTON = (By.CSS_SELECTOR, "button")
    MESSAGE_TEXT = (By.ID, "message")

    def open(self):
        self.driver.get(self.URL)

    def remove_checkbox(self):
        self.click(self.BUTTON)

    def add_checkbox(self):
        self.click(self.BUTTON)

    def wait_checkbox_visible(self):
        self.wait_element_visible(self.CHECKBOX_INPUT)

    def wait_checkbox_not_visible(self):
        self.wait_element_not_visible(self.CHECKBOX_INPUT)

    def get_message_text(self):
        return self.wait_element_visible(self.MESSAGE_TEXT).text
