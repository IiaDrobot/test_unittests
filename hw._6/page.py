from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Dict
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_tag_by_t(self, by_par: str, by_name: By = By.ID) -> WebElement:
        return self.wait.until(EC.presence_of_element_located((by_name, by_par)))

    def click_element(self, locator_value: str, by: By = By.ID) -> bool:
        try:
            self.get_tag_by_t(locator_value, by).click()
            time.sleep(2)
            return True
        except Exception as e:
            print(f"Error clicking element: {e}")
            return False

    def enter_text(self, locator_value: str, text: str, by: By = By.ID) -> None:
        input_field = self.get_tag_by_t(locator_value, by)
        input_field.clear()
        input_field.send_keys(text)

    def fill_form(self, fields: Dict[str, str], by: By = By.ID) -> None:
        for locator, value in fields.items():
            self.enter_text(locator, value, by)

    def click_and_get_url(self, locator_value: str, by: By = By.ID) -> str | None:
        try:
            self.click_element(locator_value, by)
            return self.driver.current_url
        except Exception as e:
            print(f"Error getting URL: {e}")
            return None

class LoginPage(BasePage):
    def success_login(self, authorization_data: Dict[str, str], id_tag_button: str, by_name: By = By.ID) -> None:
        self.fill_form(authorization_data, by_name)
        self.click_element(id_tag_button, by_name)

class InventoryPage(BasePage):
    def add_product(self, locator_value: str, by: By = By.ID) -> bool:
        return self.click_element(locator_value, by)

    def open_page_via_element(self, locator_value: str, by: By = By.ID) -> str | None:
        return self.click_and_get_url(locator_value, by)

    def submit_product_form(self, fields: Dict[str, str], button_id: str, by: By = By.ID) -> str | None:
        self.fill_form(fields, by)
        return self.click_and_get_url(button_id, by)

    def check_total(self, locator_value: str, by: By = By.ID) -> WebElement:
        time.sleep(2)
        return self.get_tag_by_t(locator_value, by)