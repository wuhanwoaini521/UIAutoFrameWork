from locators import login_locator
from base.baseControl import BaseControl
from util.log_control import MyLogger
import allure


@allure.feature("选择权限页面")
class Authority_Choose_Page:

    def __init__(self, driver):
        self.driver = driver
        self.baseControl = BaseControl(self.driver)

    @allure.step("查看选择权限弹窗是否弹出")
    def show_authority(self):
        get_name = self.baseControl.get_text(*login_locator.authority_choose)
        return get_name


