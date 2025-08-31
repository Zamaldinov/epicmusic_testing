from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv


class Login_page(Base):

    url = 'https://epimusic.ru/'
    load_dotenv()
    login_env = os.getenv('LOGIN')
    password_env = os.getenv('PASSWORD')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_profile = '//li[@class="top-auth-login"]'
    login = '//input[@name="USER_LOGIN"]'
    password = '//input[@name="USER_PASSWORD"]'
    button_submit_login = '//input[@name="Login"]'

    # Getters
    def get_button_profile(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_profile)))

    def get_login(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_submit_login(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_submit_login)))

    # Actions
    def click_button_profile(self):
        self.get_button_profile().click()
        print('Click button profile')

    def input_login(self, login):
        self.get_login().send_keys(login)
        print('Input login')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input password')

    def click_button_submit_login(self):
        self.get_button_submit_login().click()
        print('Click button submit login')

    # Method
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_button_profile()
        self.input_login(self.login_env)
        self.input_password(self.password_env)
        self.click_button_submit_login()
