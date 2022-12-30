from time import sleep

from selenium.common import NoSuchElementException

from locators import show_project_locator
from locators.methods import methods_list_locator
from base.baseControl import BaseControl
from util.log_control import MyLogger
import allure

logger = MyLogger()


class Method_Tab_Page:
    """
    方法tab页
    """

    def __init__(self, driver):
        self.driver = driver
        self.baseControl = BaseControl(self.driver)

    @allure.step("方法页 -> 点击曲线拟合")
    def click_img_fit_of_curve(self):
        """方法页 -> 点击曲线拟合"""
        locator_method, locator = methods_list_locator.img_fit_of_curve
        ele = []
        element = self.baseControl.find_elements(locator_method, locator)
        for i in element:
            ele.append(i)
        ele[0].click()
        logger.info("方法页 -> 点击曲线拟合")

    @allure.step("方法页 -> 选择处理类型")
    def click_img_fit_of_curve_alert_choose(self):
        """方法页 -> 选择处理类型"""
        self.baseControl.click(*methods_list_locator.img_fit_of_curve_alert_choose)
        logger.info("方法页 -> 选择处理类型")

    @allure.step("方法页 -> 确定按钮")
    def click_img_fit_of_curve_alert_confirm(self):
        """方法页 -> 确定按钮"""
        self.baseControl.click(*methods_list_locator.img_fit_of_curve_alert_confirm)
        logger.info("方法页 -> 确定按钮")

    @allure.step("方法页 -> 取消按钮")
    def click_img_fit_of_curve_alert_cancel(self):
        """方法页 -> 取消按钮"""
        self.baseControl.click(*methods_list_locator.img_fit_of_curve_alert_cancel)
        logger.info("方法页 -> 取消按钮")

    @allure.step("方法页 -> 匹配加拟合")
    def click_img_fit_of_curve_match_and_fit(self):
        """方法页 -> 匹配加拟合"""
        self.baseControl.click(*methods_list_locator.img_fit_of_curve_match_and_fit)
        logger.info("方法页 -> 匹配加拟合")

    @allure.step("方法页 -> 分步拟合")
    def click_img_fit_of_curve_step_fit(self):
        """方法页 -> 分步拟合"""
        self.baseControl.click(*methods_list_locator.img_fit_of_curve_step_fit)
        logger.info("方法页 -> 分步拟合")

    #########

    @allure.step("方法页 -> 选择原始数据弹窗 -> 第一个原始数据")
    def click_choose_first_raw_data(self):
        """方法页 -> 选择原始数据弹窗 -> 第一个原始数据"""
        sleep(2)
        self.baseControl.click(*methods_list_locator.choose_first_raw_data)
        logger.info("方法页 -> 选择原始数据弹窗 -> 第一个原始数据")

    @allure.step("方法页 -> 选择原始数据弹窗 -> 确定按钮")
    def click_choose_raw_data_confirm(self):
        """方法页 -> 选择原始数据弹窗 -> 第一个原始数据"""
        self.baseControl.click(*methods_list_locator.choose_raw_data_confirm)
        logger.info("方法页 -> 选择原始数据弹窗 -> 确定按钮")

    @allure.step("方法页 -> 选择原始数据弹窗 -> 取消按钮")
    def click_choose_raw_data_cancel(self):
        """方法页 -> 选择原始数据弹窗 -> 取消按钮"""
        self.baseControl.click(*methods_list_locator.choose_raw_data_cancel)
        logger.info("方法页 -> 选择原始数据弹窗 -> 取消按钮")

    @allure.step("方法页 -> 建立标曲 -> 组分切换")
    def click_choose_raw_data_cancel(self):
        """方法页 -> 建立标曲 -> 组分切换"""
        self.baseControl.click(*methods_list_locator.choose_raw_data_cancel)
        logger.info("方法页 -> 建立标曲 -> 组分切换")

    @allure.step("方法页 -> 建立标曲 -> 级别")
    def click_level(self):
        """方法页 -> 建立标曲 -> 级别"""
        self.baseControl.click(*methods_list_locator.level)
        logger.info("方法页 -> 建立标曲 -> 级别")

    @allure.step("方法页 -> 建立标曲 -> 级别的下拉框")
    def click_level_select(self):
        """方法页 -> 建立标曲 -> 级别的下拉框"""
        # self.baseControl.click(*methods_list_locator.level_select)
        ele = []
        element = self.baseControl.find_elements(*methods_list_locator.level_select)
        for i in element:
            ele.append(i)
        ele[0].click()
        logger.info("方法页 -> 建立标曲 -> 级别的下拉框")

    @allure.step("方法页 -> 建立标曲 -> x值")
    def input_create_curve_x(self, param):
        """方法页 -> 建立标曲 -> x值"""
        locator_method, locator = methods_list_locator.create_curve_x
        self.baseControl.input_text(locator_method, locator, param)
        logger.info("方法页 -> 建立标曲 -> x值: %s" % param)

    @allure.step("方法页 -> 建立标曲 -> 单位")
    def input_create_curve_unit(self, param):
        """方法页 -> 建立标曲 -> 单位"""
        locator_method, locator = methods_list_locator.create_curve_unit
        self.baseControl.input_text(locator_method, locator, param)
        logger.info("方法页 -> 建立标曲 -> 单位: %s" % param)

    @allure.step("方法页 -> 建立标曲 -> 确定")
    def click_create_curve_confirm(self):
        """方法页 -> 建立标曲 -> 确定"""
        self.baseControl.click(*methods_list_locator.create_curve_confirm)
        logger.info("方法页 -> 建立标曲 -> 确定")

    @allure.step("方法页 -> 建立标曲 -> 取消")
    def click_create_curve_cancel(self):
        """方法页 -> 建立标曲 -> 取消"""
        self.baseControl.click(*methods_list_locator.create_curve_cancel)
        logger.info("方法页 -> 建立标曲 -> 取消")
