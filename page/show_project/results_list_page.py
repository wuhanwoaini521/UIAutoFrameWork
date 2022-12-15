from locators.results import results_list_locator
from base.baseControl import BaseControl
from util.log_control import MyLogger
from tests.common import Common
import allure

logger = MyLogger()


@allure.epic("项目 - 结果tab页")
class Results_List_Page:
    """
    项目 - 结果tab页
    """

    def __init__(self, driver):
        self.driver = driver
        self.baseControl = BaseControl(self.driver)
        self.common = Common()

    @allure.step("点击结果列表的第一个结果checkbox")
    def click_first_check_box_button(self):
        """点击结果列表的第一个结果checkbox"""
        locator_method, locator = results_list_locator.first_check_box
        elements = self.baseControl.find_element(locator_method, locator)
        elements.click()
        logger.info("点击结果列表的第一个结果checkbox")

    @allure.step("点击出版报告按钮")
    def click_report_result_button(self):
        """点击出版报告按钮"""
        locator_method, locator = results_list_locator.report_result
        self.baseControl.click(locator_method, locator)
        logger.info("点击出版报告按钮")

    @allure.step("点击第一个出版报告")
    def click_first_report_button(self):
        """点击第一个出版报告"""
        locator_method, locator = results_list_locator.first_report
        self.baseControl.click(locator_method, locator)
        logger.info("点击第一个出版报告")

    @allure.step("点击某个出版报告")
    def click_all_report_name_button(self, name):
        """点击某个出版报告"""
        locator_method, locator = results_list_locator.all_report_name
        self.baseControl.click(locator_method, locator % name)
        logger.info("点击 %s 出版报告" % name)

    @allure.step("点击某个结果 - 根据名称")
    def click_all_report_name_button(self, name):
        """点击某个结果 - 根据名称"""
        locator_method, locator = results_list_locator.all_report_name
        self.baseControl.click(locator_method, locator % name)
        logger.info("点击 %s 结果" % name)

    @allure.step("点击某个结果")
    def click_some_result(self, index):
        """点击某个结果"""
        locator_method, locator = results_list_locator.result_name_lists
        elements = self.baseControl.find_elements(locator_method, locator)
        ele = []
        for i in elements:
            ele.append(i)
        ele[index].click()

