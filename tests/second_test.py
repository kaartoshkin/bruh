import pytest
from pages.base_page import BasePage
from pages.internet_page import InternetPage
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_login_invalid_credentials(driver):
    page = InternetPage(driver)
    page.open()

    page.login("wrong", "wrong")

    flash_message = page.get_flash_message()
    assert "Your username is invalid!" in flash_message
    
    page.wait_url_contains("/login")
    assert "/login" in driver.current_url