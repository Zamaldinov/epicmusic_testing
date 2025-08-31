from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Select_guitar_in_catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_menu_guitar = '(//span[@class="tx"])[1]'

    # Getters
    def get_button_menu_guitar(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_menu_guitar)))

    # Actions
    def click_button_menu_guitar(self):
        self.get_button_menu_guitar().click()
        print('Click button menu guitar')

    # Method
    def select_catalog_guitar(self):
        self.click_button_menu_guitar()
