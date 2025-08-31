from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    total_prize = '//span[@class="basket-item-price-current-text"]'
    input_fio = 'ORDER_PROP_1'
    input_phone = '//input[@name="ORDER_PROP_3"]'
    input_comment = '//textarea[@name="ORDER_DESCRIPTION"]'

    # Getters
    def get_total_prize(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.total_prize)))

    def get_input_fio(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.NAME, self.input_fio)))

    def get_input_phone(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.input_phone)))

    def get_input_comments(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.input_comment)))

    # Actions
    def check_total_prize(self):
        val = self.get_total_prize().text
        assert val == '94 500 ₽'
        print('Good total prize')

    def input_name(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_input_fio())
        self.get_input_fio().clear()
        self.get_input_fio().send_keys('Иван Иванов')
        print('Input name')

    def input_telephone(self):
        self.get_input_phone().send_keys('9991234856')
        print('Input phone')

    def input_comments(self):
        self.get_input_comments().send_keys('РОК ЖИВ!!! =)')
        print('Input comment')

    # Method
    def buy_cart(self):
        self.check_total_prize()
        self.get_screenshot()
        self.input_name()
        self.input_telephone()
        self.input_comments()

