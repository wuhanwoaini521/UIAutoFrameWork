import time
import traceback

import allure
from selenium.common import NoSuchElementException, TimeoutException

from base.baseControl import BaseControl
from util.log_control import MyLogger


logger = MyLogger()

class Assert_Control:

    def __init__(self, driver):
        self.driver = driver
        self.baseControl = BaseControl(self.driver)

    # def assert_equal(actualResult, expected):
    #     assert actualResult == expected, "实际结果为:{0}, 预期结果为:{1}".format(actualResult, expected)
    #
    # def assert_not_equal(actualResult, expected):
    #     assert actualResult != expected, "实际结果为:{0}, 预期结果为:{1}".format(actualResult, expected)
    #
    #
    # def assert_in(actualResult, expected):
    #     assert actualResult in expected, "实际结果为:{0}, 预期结果为:{1}".format(actualResult, expected)

    def assert_isExists(self, locator_method, locator):
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

