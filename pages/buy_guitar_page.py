from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Buy_guitar(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_add_guitar = '(//a[@class="plus"])[2]'
    button_buy = '(//a[@data-id="81055"])[6]'
    button_cart = '//span[text()="Перейти в корзину"]'

    # Getters
    def get_button_add_guitar(self):
        return WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.XPATH, self.button_add_guitar)))

    def get_button_buy(self):
        return WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.XPATH, self.button_buy)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    # Actions
    def click_button_add_guitar(self):
        self.get_button_add_guitar().click()
        print('Click button add guitar')

    def click_button_buy(self):
        self.get_button_buy().click()
        print('Click button buy')

    def click_button_cart(self):
        self.get_button_cart().click()
        print('Click button cart')

    # Method
    def buy_guitars(self):
        self.click_button_add_guitar()
        self.click_button_add_guitar()
        self.click_button_buy()
        # self.click_button_cart()
