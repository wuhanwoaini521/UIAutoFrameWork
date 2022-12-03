from locators import login_locator
from base.baseControl import BaseControl
from util.log_control import MyLogger
import allure

logger = MyLogger()


@allure.feature("选择权限页面")
class Authority_Choose_Page:

    def __init__(self, driver):
        self.driver = driver
        self.baseControl = BaseControl(self.driver)

    @allure.step("查看选择权限弹窗是否弹出")
    def show_authority(self):
        get_name = self.baseControl.get_text(*login_locator.authority_choose)
        return get_name

    @allure.step("点击系统管理员")
    def click_system_role(self):
        self.baseControl.click(*login_locator.system_administrator)
        logger.info("点击系统管理员")

    @allure.step("点击安全管理员")
    def click_safe_administrator(self):
        self.baseControl.click(*login_locator.safe_administrator)
        logger.info("点击安全管理员")

    @allure.step("点击审计管理员")
    def click_aduit_administrator(self):
        self.baseControl.click(*login_locator.aduit_administrator)
        logger.info("点击审计管理员")

    @allure.step("点击普通用户")
    def click_ordinary_user(self):
        self.baseControl.click(*login_locator.ordinary_user)
        logger.info("点击普通用户")

    @allure.step("点击自选用户")
    def click_custom_role_user(self, user_name):
        self.baseControl.click(*login_locator.custom_role % user_name)
        logger.info("点击自选用户")
