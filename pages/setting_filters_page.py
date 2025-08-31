import time

from selenium.webdriver import Keys

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Setting_filters(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_guitars = '(//span[@class="sectionColumn"])[1]'
    input_prize = '//input[@id="arrFilter_P1_MAX"]'
    select_body_material = '(//ins[@class="propExpander "])[3]'
    select_material = '//ins[@class="propExpander  expanded"]'
    select_count_of_frets = '(//ins[@class="propExpander"])[4]'
    select_22_frets = '//label[@data-role="label_arrFilter_946_2377366028"]'
    select_guitar = '//span[text()="IBANEZ GSA60-BS"]'
    select_electric_guitars = '//a[text()="Электрогитары"]'

    # Getters
    def get_button_guitars(self):
        return WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.XPATH, self.button_guitars)))

    def get_select_electric_guitars(self):
        return WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.XPATH, self.select_electric_guitars)))

    def get_input_prize(self):
        return WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.XPATH, self.input_prize)))

    def get_select_body_material(self):
        return WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.XPATH, self.select_body_material)))

    def get_select_material(self):
        return WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.XPATH, self.select_material)))

    def get_select_count_of_frets(self):
        return WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.XPATH, self.select_count_of_frets)))

    def get_select_22_frets(self):
        return WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.XPATH, self.select_22_frets)))

    def get_select_guitar(self):
        return WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.XPATH, self.select_guitar)))

    # Actions
    def click_button_guitars(self):
        self.get_button_guitars().click()
        print('Click button_guitars')

    def input_prize_guitar(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_input_prize())
        self.get_input_prize().clear()
        self.get_input_prize().send_keys('50000')
        self.get_input_prize().send_keys(Keys.ENTER)
        print('Input prize guitar')

    def click_select_body_material(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_select_body_material())
        self.get_select_body_material().click()
        print('Click button select body material')

    def click_select_material(self):
        self.get_select_material().click()
        print('Click button select material')

    def click_select_count_of_frets(self):
        self.get_select_count_of_frets().click()
        print('Click button count of frets')

    def click_select_22_frets(self):
        self.get_select_22_frets().click()
        print('Click button 22 frets')

    def click_select_guitar(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_select_guitar())
        self.get_select_guitar().click()
        print('Click select guitar')

    def click_select_electric_guitars(self):
        self.get_select_electric_guitars().click()
        print('Click select electric guitar')

    # Method
    def setting_filters(self):
        self.click_button_guitars()
        self.click_select_electric_guitars()
        self.input_prize_guitar()
        self.click_select_body_material()
        self.click_select_22_frets()
        self.click_select_guitar()

