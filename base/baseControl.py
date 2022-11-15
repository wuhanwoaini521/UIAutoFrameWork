from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import traceback
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
    poll_frequency = settings.POLL_FREQUENCY
    times = settings.TIMES

    def __init__(self, driver):
        self.driver = driver
        self.locate_method = {
            "id": By.ID,
            "name": By.NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "xpath": By.XPATH
        }

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

    def refresh(self):
        """
        浏览器刷新按钮
        :return:
        """
        self.driver.refresh()

    def quit_browser(self):
        """
        关闭并停止浏览器服务
        :return:
        """
        self.driver.quit()


    def find_element(self, locate_method, locator, times=times, poll_frequency=poll_frequency):
        """
        查找元素
        :param locate_method:
        :param locator:
        :param times:
        :param poll_frequency:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout=times, poll_frequency=poll_frequency).until \
                (lambda x: x.find_element(self.locate_method[locate_method]
                                          , locator))
            return element
        except TimeoutException:
            traceback.print_exc()
            raise TimeoutException(msg="元素未找到，超时！")

    def find_elements(self, locate_method, locator, times=times, poll_frequency=poll_frequency):
        """
        查找元素列表
        :param locate_method:
        :param locator:
        :param times:
        :param poll_frequency:
        :return:
        """
        try:
            elements = WebDriverWait(self.driver, timeout=times, poll_frequency=poll_frequency).until \
                (lambda x: x.find_elements(self.locate_method[locate_method]
                                           , locator))
            return elements
        except TimeoutException:
            traceback.print_exc()
            raise TimeoutException(msg="元素未找到，超时！")

    def input_text(self, locate_method, locator, text):
        self.find_element(locate_method, locator).send_keys(text)

    def click(self, locate_method, locator):
        self.find_element(locate_method, locator).click()
    
    def alert(self):
        pass
    
    def switch_windoww(self):
        pass