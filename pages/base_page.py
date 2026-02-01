
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type_text(self, locator, text, timeout=10, clear=True):
        el = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        if clear:
            el.clear()
        el.send_keys(text)
        return el

    def find_all(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.find_elements(*locator)

    def wait_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def wait_title_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.title_contains(text))

    def wait_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    