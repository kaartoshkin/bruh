import pytest
from pages.base_page import BasePage
from pages.python_org_page import PythonOrgPage
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    d = webdriver.Firefox()
    yield d
    d.quit()

def test_python_org_search_decorators(driver):
    page = PythonOrgPage(driver)
    page.open()

    page.search("decorators")

    page.wait_url_contains("search")

    page.wait_element_visible(page.RESULTS_ITEMS)

    assert 'search' in driver.current_url.lower()
    assert len(page.results_texts()) > 0