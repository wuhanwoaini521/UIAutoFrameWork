from selenium.common import NoSuchElementException

from locators import show_project_locator
from locators.raw_data_locator import raw_data_list_locator
from base.baseControl import BaseControl
from util.log_control import MyLogger
import allure

logger = MyLogger()


class Raw_Data_Tab_Page:
    """
    原始数据tab页
    """

    def __init__(self, driver):
        self.driver = driver
        self.baseControl = BaseControl(self.driver)

    @allure.step("点击积分结果表 -> 保存按钮")
    def click_confirm(self):
        """点击积分结果表 -> 确定按钮"""
        self.baseControl.click(*raw_data_list_locator.view_the_integral_result_save)
        logger.info("点击积分结果表 -> 保存按钮")

    @allure.step("原始数据列表页 -> 原始数据列表，名称列表")
    def click_raw_data_list_names(self, param):
        """原始数据列表页 -> 原始数据列表，名称列表"""
        locator_method, locator = raw_data_list_locator.raw_data_list_names
        ele = []
        element = self.baseControl.find_elements(locator_method, locator)
        for i in element:
            ele.append(i)
        ele[param].click()
        logger.info("原始数据列表页 -> 原始数据列表，名称列表")
