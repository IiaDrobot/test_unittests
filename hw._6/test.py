import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from ha_6.page import LoginPage, InventoryPage


class TestInventory:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        authorization_data = {
            "user-name": "standard_user",
            "password": "secret_sauce"
        }

        LoginPage(driver).success_login(authorization_data=authorization_data, id_tag_button="login-button")
        yield driver
        driver.quit()

    @pytest.fixture
    def inventory_page(self, driver):
        return InventoryPage(driver)

    def test_add_product(self, inventory_page):
        id_products = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]

        for id_product in id_products:
            assert inventory_page.add_product(By.ID, id_product)

    def test_click_shopping_cart(self, inventory_page):
        assert inventory_page.click_tag(By.CLASS_NAME, "shopping_cart_link") == "https://www.saucedemo.com/cart.html"
        result_url = inventory_page.open_page_via_element(locator_value="shopping_cart_link", by=By.CLASS_NAME)
        assert result_url == "https://www.saucedemo.com/cart.html"

    def test_click_checkout(self, inventory_page):
        assert inventory_page.click_tag(By.ID, "checkout") == "https://www.saucedemo.com/checkout-step-one.html"
        result_url = inventory_page.open_page_via_element(locator_value="checkout", by=By.ID)
        assert result_url == "https://www.saucedemo.com/checkout-step-one.html"

    def test_enter_information(self, inventory_page):
        info = {
            "first-name": "Iia",
            "last-name": "Drobot",
            "postal-code": "12345"
        }
        assert inventory_page.enter_information(info, "continue") == "https://www.saucedemo.com/checkout-step-two.html"
        result_url = inventory_page.submit_product_form(fields=info, button_id="continue")
        assert result_url == "https://www.saucedemo.com/checkout-step-two.html"

    def test_check_total(self, inventory_page):
        assert "58.29" in inventory_page.check_total(By.CLASS_NAME, "summary_total_label").text
        total_text = inventory_page.check_total(locator_value="summary_total_label", by=By.CLASS_NAME).text
        assert "58.29" in total_text