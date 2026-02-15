import pytest
from selenium.webdriver.common.by import By

from bruh.pages.base_page import BasePage

class ProductsPage(BasePage):

    URL = 'https://www.saucedemo.com/inventory.html'

    ADD_BACKPACK_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BOLT_TSHIRT_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    ADD_BIKE_LIGHTS_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")
    ADD_FLEECE_JACKET_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    ADD_TSHIRT_RED_TO_CART_BUTTON = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")

    SHOPPING_CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def open(self):
        self.driver.get(self.URL)

    def add_all_items_to_cart(self):
        self.add_backpack_to_cart()
        self.add_bolt_tshirt_to_cart()
        self.add_onesie_to_cart()
        self.add_bike_lights_to_cart()
        self.add_fleece_jacket_to_cart()
        self.add_tshirt_red_to_cart()

    def add_backpack_to_cart(self):
        self.wait_element_visible(self.ADD_BACKPACK_TO_CART_BUTTON)
        self.click(self.ADD_BACKPACK_TO_CART_BUTTON)
    def add_bolt_tshirt_to_cart(self):
        self.wait_element_visible(self.ADD_BOLT_TSHIRT_TO_CART_BUTTON)
        self.click(self.ADD_BOLT_TSHIRT_TO_CART_BUTTON)
    def add_onesie_to_cart(self):
        self.wait_element_visible(self.ADD_ONESIE_TO_CART_BUTTON)
        self.click(self.ADD_ONESIE_TO_CART_BUTTON)
    def add_bike_lights_to_cart(self):  
        self.wait_element_visible(self.ADD_BIKE_LIGHTS_TO_CART_BUTTON)
        self.click(self.ADD_BIKE_LIGHTS_TO_CART_BUTTON)
    def add_fleece_jacket_to_cart(self):
        self.wait_element_visible(self.ADD_FLEECE_JACKET_TO_CART_BUTTON)
        self.click(self.ADD_FLEECE_JACKET_TO_CART_BUTTON)
    def add_tshirt_red_to_cart(self):
        self.wait_element_visible(self.ADD_TSHIRT_RED_TO_CART_BUTTON)
        self.click(self.ADD_TSHIRT_RED_TO_CART_BUTTON)
    def click_shopping_cart_icon(self):
        self.wait_element_visible(self.SHOPPING_CART_ICON)
        self.click(self.SHOPPING_CART_ICON)
        
    def get_cart_badge_count(self):
        try:
            badge = self.wait_element_visible(self.SHOPPING_CART_BADGE)
            return int(badge.text)
        except:
            return 0
