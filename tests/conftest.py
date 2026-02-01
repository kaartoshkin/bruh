import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    d = webdriver.Firefox()
    yield d
    d.quit()
