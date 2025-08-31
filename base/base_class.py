import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    '''Method current url'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url' + get_url)

    '''Method screenshot'''

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
        name_screenshot = f'Screenshot {now_date}.png'
        self.driver.save_screenshot('C:\\Питон\\Тестирование\\onlinetrade_project\\screen\\' + name_screenshot)
