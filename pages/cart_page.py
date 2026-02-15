import pytest
from selenium.webdriver.common.by import By

from bruh.pages.base_page import BasePage

class CartPage(BasePage):
    URL = 'https://www.saucedemo.com/cart.html'

    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    REMOVE_BOLT_TSHIRT_BUTTON = (By.ID, "remove-sauce-labs-bolt-t-shirt")
    REMOVE_ONESIE_BUTTON = (By.ID, "remove-sauce-labs-onesie")
    REMOVE_BIKE_LIGHTS_BUTTON = (By.ID, "remove-sauce-labs-bike-light")
    REMOVE_FLEECE_JACKET_BUTTON = (By.ID, "remove-sauce-labs-fleece-jacket")
    REMOVE_TSHIRT_RED_BUTTON = (By.ID, "remove-test.allthethings()-t-shirt-(red)")
    
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    
    def open(self):
        self.driver.get(self.URL)

    def click_checkout_button(self):
        self.wait_element_visible(self.CHECKOUT_BUTTON)
        self.click(self.CHECKOUT_BUTTON)

    def get_cart_items_count(self):
        items = self.find_all(self.CART_ITEM)
        return len(items)
    
    def get_cart_items_names(self):
        items = self.find_all(self.CART_ITEM)
        item_names = [item.find_element(*self.CART_ITEM_NAME).text for item in items]
        return item_names
    
    def remove_backpack_from_cart(self):
        self.wait_element_visible(self.REMOVE_BACKPACK_BUTTON)
        self.click(self.REMOVE_BACKPACK_BUTTON)

    def remove_bolt_tshirt_from_cart(self):
        self.wait_element_visible(self.REMOVE_BOLT_TSHIRT_BUTTON)
        self.click(self.REMOVE_BOLT_TSHIRT_BUTTON)

    def remove_onesie_from_cart(self):
        self.wait_element_visible(self.REMOVE_ONESIE_BUTTON)
        self.click(self.REMOVE_ONESIE_BUTTON)

    def remove_bike_lights_from_cart(self):
        self.wait_element_visible(self.REMOVE_BIKE_LIGHTS_BUTTON)
        self.click(self.REMOVE_BIKE_LIGHTS_BUTTON)

    def remove_fleece_jacket_from_cart(self):
        self.wait_element_visible(self.REMOVE_FLEECE_JACKET_BUTTON)
        self.click(self.REMOVE_FLEECE_JACKET_BUTTON)

    def remove_tshirt_red_from_cart(self):
        self.wait_element_visible(self.REMOVE_TSHIRT_RED_BUTTON)
        self.click(self.REMOVE_TSHIRT_RED_BUTTON)

    def remove_all_items_from_cart(self):
        self.remove_backpack_from_cart()
        self.remove_bolt_tshirt_from_cart()
        self.remove_onesie_from_cart()
        self.remove_bike_lights_from_cart()
        self.remove_fleece_jacket_from_cart()
        self.remove_tshirt_red_from_cart()