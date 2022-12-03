from locators.methods import new_deal_with_locator
from base.baseControl import BaseControl
from util.log_control import MyLogger
import allure

logger = MyLogger()


class New_Method_Page:

    def __init__(self, driver):
        self.driver = driver
        self.baseControl = BaseControl(self.driver)

    @allure.step("点击保存按钮")
    def click_new_method_save_button(self):
        """保存按钮"""
        self.baseControl.click(*new_deal_with_locator.new_method_save)
        logger.info("点击保存按钮")

    @allure.step("输入仪器方法的名称")
    def input_alert_save_deal_with_method_input(self, name):
        """输入仪器方法的名称"""
        self.baseControl.input_text(*new_deal_with_locator.alert_save_deal_with_method_input, name)
        logger.info("输入仪器方法的名称")

    @allure.step("点击确认按钮")
    def click_alert_save_deal_with_method_confirm_button(self):
        """保存按钮"""
        self.baseControl.click(*new_deal_with_locator.alert_save_deal_with_method_confirm_button)
        logger.info("点击确认按钮")

    @allure.step("点击取消按钮")
    def click_alert_save_deal_with_method_cancel_button(self):
        """保存按钮"""
        self.baseControl.click(*new_deal_with_locator.alert_save_deal_with_method_cancel_button)
        logger.info("点击取消按钮")

    @allure.step("输入峰宽")
    def input_peak_width(self, name):
        """输入仪器方法的名称"""
        self.baseControl.input_text(*new_deal_with_locator.peak_width, name)
        logger.info("输入峰宽")

    @allure.step("输入斜率")
    def input_slope(self, name):
        """输入仪器方法的名称"""
        self.baseControl.input_text(*new_deal_with_locator.slope, name)
        logger.info("输入斜率")

    @allure.step("点击添加积分事件按钮")
    def click_add_integral_event_button(self):
        """保存按钮"""
        self.baseControl.click(*new_deal_with_locator.new_method_save)
        logger.info("点击添加积分事件按钮")

    @allure.step("点击添加分段积分参数按钮")
    def click_add_second_order_integralevent_button(self):
        """保存按钮"""
        self.baseControl.click(*new_deal_with_locator.add_second_order_integralevent)
        logger.info("点击添加分段积分参数按钮")