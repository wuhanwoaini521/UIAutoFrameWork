"""浏览器驱动选择器 🌐.

根据配置的浏览器名称返回对应的 Selenium WebDriver 实例。
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService

from util import settings


class Choose_Driver:
    """根据名称选择并创建浏览器驱动。"""

    def __init__(self, driver_name):
        self.driver_name = driver_name
        self.driver = None

    def choose_driver(self):
        """选择并返回对应浏览器的 WebDriver 实例。"""
        if self.driver_name == "chrome":
            driver_path = settings.CHROMEDRIVER
            service = Service(driver_path)
            self.driver = webdriver.Chrome(service=service)
        elif self.driver_name == "firefox":
            driver_path = settings.FIREFOXDRIVER
            service = FirefoxService(driver_path)
            self.driver = webdriver.Firefox(service=service)
        else:
            raise ValueError("不支持的浏览器类型: %s" % self.driver_name)
        return self.driver
