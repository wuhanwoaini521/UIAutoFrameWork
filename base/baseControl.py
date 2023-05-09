from functools import wraps

import allure
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
            "xpath": By.XPATH,
            "class": By.CLASS_NAME,
            "css": By.CSS_SELECTOR,
            "tag": By.TAG_NAME
        }

    def open_url(self, url=None):
        """
        打开浏览器
        :param url:
        :return:
        """
        if not self.base_url:
            raise "请传入url！"
        if url:
            self.base_url = url
        self.driver.get(self.base_url)  # 进入路径
        self.driver.maximize_window()  # 窗口最大化

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
                (EC.visibility_of_element_located((self.locate_method[locate_method]
                                                   , locator)))
            return element
        except TimeoutException:
            # traceback.print_exc()
            allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
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
        elemets_list = []
        try:
            elements = WebDriverWait(self.driver, timeout=times, poll_frequency=poll_frequency).until \
                (EC.visibility_of_all_elements_located((self.locate_method[locate_method]
                                                        , locator)))
            # elements = WebDriverWait(self.driver, timeout=times, poll_frequency=poll_frequency).until \
            #         (lambda x: x.find_elements(self.locate_method[locate_method]
            #                                                     , locator))
            return elements
        except TimeoutException:
            traceback.print_exc()
            # allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
            raise TimeoutException(msg="元素未找到，超时！")

    def clear_text(self, locate_method, locator):
        """
        清空输入框内容
        :param locate_method:
        :param locator:
        :return:
        """
        self.find_element(locate_method, locator).clear()

    def input_text(self, locate_method, locator, text):
        """
        输入框输入内容
        :param locate_method:
        :param locator:
        :param text:
        :return:
        """
        self.clear_text(locate_method, locator)
        self.find_element(locate_method, locator).send_keys(text)

    def click(self, locate_method, locator):
        """
        点击内容
        :param locate_method:
        :param locator:
        :return:
        """
        # self.click_element(locate_method, locator).click()
        element = self.click_element(locate_method, locator)
        self.driver.execute_script("arguments[0].click()", element)

    def click_text(self, locate_method, locator):
        """
        点击内容
        :param locate_method:
        :param locator:
        :return:
        """
        # self.click_element(locate_method, locator).click()
        element = self.click_element(locate_method, locator)
        self.driver.execute_script("arguments[0].click()", element)

    def alert(self):
        """
        点击页面弹窗
        :return:
        """
        pass

    def switch_window(self):
        """
        切换页面句柄
        :return:
        """
        pass

    def get_text(self, locate_method, locator):
        """
        获取元素的text值
        """
        text = self.find_element(locate_method, locator).text
        return text

    def scroll_window(self, locate_method, locator):
        """
        元素滚动到页面
        :param locate_method:
        :param locator:
        :return:
        """
        element = self.find_element(locate_method, locator)
        js_element = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js_element, element)

    def get_current_url(self):
        """
        获取当前页面url
        :return:
        """
        current_url = self.driver.current_url
        return current_url

    def click_element(self, locate_method, locator, times=times, poll_frequency=poll_frequency):
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
                (EC.element_to_be_clickable((self.locate_method[locate_method]
                                                   , locator)))
            return element
        except TimeoutException:
            traceback.print_exc()
            allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
            raise TimeoutException(msg="元素未找到，超时！")
