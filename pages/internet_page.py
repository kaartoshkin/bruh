
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InternetPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def login_with_valid_credentials(self):
        self.login("tomsmith", "SuperSecretPassword!")

    def logout(self):
        self.click(self.LOGOUT_BUTTON)

    def get_flash_message(self) -> str:
        flash_element = self.wait_element_visible(self.FLASH_MESSAGE)
        return flash_element.text.replace("×", "").strip()


    
       