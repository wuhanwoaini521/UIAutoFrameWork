"""断言 / 校验控制 🧪.

提供元素存在性等校验能力，校验失败时自动截图并抛出超时异常。
"""

import traceback

import allure
from selenium.common import TimeoutException

from base.baseControl import BaseControl
from util.log_control import MyLogger

logger = MyLogger()


class Assert_Control:
    """UI 断言控制类。"""

    def __init__(self, driver):
        self.driver = driver
        self.baseControl = BaseControl(self.driver)

    def assert_isExists(self, locator_method, locator):
        """轮询判断元素是否存在，不存在则截图并抛异常。"""
        while True:
            try:
                if self.baseControl.find_element(locator_method, locator):
                    logger.info("◆◆◆元素存在！校验通过！◆◆◆")
                    break
            except Exception:
                traceback.print_exc()
                allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
                logger.info("◇◇◇元素不存在！校验失败◇◇◇")
                raise TimeoutException(msg="元素未找到，超时！")
