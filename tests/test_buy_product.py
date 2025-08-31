from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.select_guitar_in_catalog_page import Select_guitar_in_catalog_page
from pages.login_page import Login_page
from pages.setting_filters_page import Setting_filters
from pages.buy_guitar_page import Buy_guitar
from pages.cart_page import Cart_page


def test_buy_product():

    options = Options()
    options.add_argument('--guest')
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options)

    login = Login_page(driver)
    login.authorization()
    sg = Select_guitar_in_catalog_page(driver)
    sg.select_catalog_guitar()
    sf = Setting_filters(driver)
    sf.setting_filters()
    bg = Buy_guitar(driver)
    bg.buy_guitars()
    cp = Cart_page(driver)
    cp.buy_cart()