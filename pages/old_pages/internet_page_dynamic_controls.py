
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InternetPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_controls"

    CHECKBOX_FIELD = (By.CSS_SELECTOR, "input[type='checkbox']")
    CHECKBOX_BUTTON = (By.XPATH, "//button[@onclick='swapCheckbox()']")
    INPUT_BUTTON = (By.XPATH, "//button[@onclick='swapInput()']")
    INPUT_FIELD = (By.CSS_SELECTOR, "input[type='text']")
    MESSAGE_TEXT = (By.ID, "message")
    

    def open(self):
        self.driver.get(self.URL)

    def remove_checkbox(self):
        self.click(self.CHECKBOX_BUTTON)

    def add_checkbox(self):
        self.click(self.CHECKBOX_BUTTON)

    def disable_input(self):
        self.click(self.INPUT_BUTTON)

    def enable_input(self):
        self.click(self.INPUT_BUTTON)   

    def wait_checkbox_visible(self):
        self.wait_element_visible(self.CHECKBOX_FIELD)

    def wait_checkbox_not_visible(self):
        self.wait_element_not_visible(self.CHECKBOX_FIELD)

    def wait_input_enabled(self):
        self.wait_element_visible(self.INPUT_FIELD)
        EC.element_to_be_clickable(self.INPUT_FIELD)
    
    def wait_input_disabled(self):
        self.wait_element_visible(self.INPUT_FIELD)
        EC.invisibility_of_element_located(self.INPUT_FIELD)
        
    def get_message_text(self):
        return self.wait_element_visible(self.MESSAGE_TEXT).text
