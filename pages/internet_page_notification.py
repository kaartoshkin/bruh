
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InternetPage(BasePage):
    URL = "https://the-internet.herokuapp.com/notification_message_rendered"

    CLICK_HERE_LINK = (By.CSS_SELECTOR, ".example > p:nth-child(2) > a:nth-child(5)")
    FLASH_MESSAGE = (By.ID, "flash")


    FLASH_MESSAGES = [
        "Action successful",
        "Action unsuccesful, please try again ",
        ""]

    def open(self):
        self.driver.get(self.URL)

    def get_flash_message(self) -> str:
        flash_element = self.wait_element_visible(self.FLASH_MESSAGE)
        return flash_element.text.replace("×", "").strip()

    def get_new_message(self) -> str:
        self.click(self.CLICK_HERE_LINK)
        return self.get_flash_message()
    
