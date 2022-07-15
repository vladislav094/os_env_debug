import time

from selenium.webdriver.common.by import By
from framework.utils import SeleniumBase

class ToolsQaElements:
    def __init__(self, driver):
        self.driver = driver

    @property
    def selenium(self):
        return SeleniumBase(driver=self.driver)

    @property
    def drop_list(self):
        return SeleniumBase(driver=self.driver, locator=(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/span[2]/select'))



class Tools:
    def __init__(self, driver):
        self.element = ToolsQaElements(driver=driver)

    def open_site(self):
        self.element.selenium.go_to_url('https://demoqa.com/webtables')
        self.element.drop_list.select_in_dropdown(0)
        time.sleep(5)
