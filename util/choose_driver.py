from util import settings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Choose_Driver:

    def __init__(self, driver_name):
        self.driver_name = driver_name
        self.driver = None

    def choose_driver(self):
        if self.driver_name == "chrome":
            driver_path = settings.CHROMEDRIVER
            service = Service(driver_path)
            self.driver = webdriver.Chrome(service=service)
        if self.driver_name == "firefox":
            driver_path = settings.FIREFOXDRIVER
            service = Service(driver_path)
            self.driver = webdriver.Firefox(service=service)
        return self.driver
