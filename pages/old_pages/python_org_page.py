
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PythonOrgPage(BasePage):
    URL = "https://www.python.org"

    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.ID, "submit")

    RESULTS_ITEMS = (By.CSS_SELECTOR, ".list-recent-events li")

    def open(self):
        self.driver.get(self.URL)

    def search(self, query: str):
        self.type_text(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)

    def results_texts(self):
        items = self.find_all(self.RESULTS_ITEMS)
        return [item.text for item in items]
    
       