import pytest
from selenium.webdriver.common.by import By

from bruh.pages.login_page import LoginPage
from bruh.pages.products_page import ProductsPage
from bruh.pages.cart_page import CartPage

class TestAddItemToCart:
    def test_add_item_to_cart_and_count(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(driver)

        products_page.open()

        products_page.add_backpack_to_cart()
        assert products_page.get_cart_badge_count() == 1

        products_page.add_bolt_tshirt_to_cart()
        assert products_page.get_cart_badge_count() == 2

        products_page.add_onesie_to_cart()
        assert products_page.get_cart_badge_count() == 3

        products_page.add_bike_lights_to_cart()
        assert products_page.get_cart_badge_count() == 4

        products_page.add_fleece_jacket_to_cart()
        assert products_page.get_cart_badge_count() == 5

        products_page.add_tshirt_red_to_cart()
        assert products_page.get_cart_badge_count() == 6

        products_page.click_shopping_cart_icon()

        cart_page = CartPage(driver)

        cart_page.wait_url_contains("cart")
        assert cart_page.get_cart_items_count() == 6

    def test_add_item_to_cart_and_check_items_in_cart(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        products_page = ProductsPage(driver)
        products_page.open()

        products_page.add_all_items_to_cart()

        products_page.click_shopping_cart_icon()

        cart_page = CartPage(driver)

        cart_page.wait_url_contains("cart")
        item_names = cart_page.get_cart_items_names()
        assert "Sauce Labs Backpack" in item_names
        assert "Sauce Labs Bolt T-Shirt" in item_names
        assert "Sauce Labs Onesie" in item_names
        assert "Sauce Labs Bike Light" in item_names
        assert "Sauce Labs Fleece Jacket" in item_names
        assert "Test.allTheThings() T-Shirt (Red)" in item_names
        