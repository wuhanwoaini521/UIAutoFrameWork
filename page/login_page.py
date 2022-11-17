from locators import login_locator
from base.baseControl import BaseControl
from util.log_control import MyLogger
import allure

logger = MyLogger()


class Login_Page:
    """
    登录页
    """

    def __init__(self, driver):
        self.driver = driver
        self.baseControl = BaseControl(self.driver)

    @allure.step("输入用户名")
    def username_text(self, user_name):
        """姓名输入框"""
        self.baseControl.input_text(*login_locator.username_text, user_name)
        logger.info("输入姓名: %s" % user_name)

    @allure.step("输入密码")
    def password_text(self, password):
        """密码输入框"""
        self.baseControl.input_text(*login_locator.password_text, password)
        logger.info("输入密码: %s" % password)

    @allure.step("点击登录按钮")
    def click_login_button(self):
        """登录按钮"""
        self.baseControl.click(*login_locator.login_button)
        logger.info("点击登录按钮")
