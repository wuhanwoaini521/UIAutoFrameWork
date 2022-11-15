from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import util.settings as settings
from util.log_control import MyLogger
import datetime
import time


class BaseControl:
    """
    封装元素的操作方式
    """
    url = ''
    base_url = settings.WEB_TEST_BASE_URL

    def __init__(self, driver):
        self.driver = driver

    def open_url(self):
        """
        打开浏览器
        :param url:
        :return:
        """
        if not self.base_url:
            raise "请传入url！"
        self.driver.get(self.base_url)

    def back(self):
        """
        浏览器后退按钮
        :return:
        """
        self.driver.back()

    def forward(self):
        """
        浏览器前进按钮
        :return:
        """
        self.driver.forward()

    def quit_browser(self):
        """
        关闭并停止浏览器服务
        :return:
        """
        self.driver.quit()



