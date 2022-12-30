from time import sleep

from selenium.common import NoSuchElementException

from locators import show_project_locator
from locators.raw_data_locator import raw_data_detail_locator
from base.baseControl import BaseControl
from util.log_control import MyLogger
import allure

logger = MyLogger()


class Raw_Data_Detail_Page:
    """
    原始数据详情页
    """

    def __init__(self, driver):
        self.driver = driver
        self.baseControl = BaseControl(self.driver)

    @allure.step("原始数据详情界面 -> 选择处理办法下拉框")
    def click_choose_deal_with_method(self):
        """原始数据详情界面 -> 选择处理办法下拉框"""
        self.baseControl.click(*raw_data_detail_locator.choose_deal_with_method)
        logger.info("原始数据详情界面 -> 选择处理办法下拉框")

    @allure.step("原始数据详情界面 -> 根据名称选择处理办法")
    def input_choose_deal_with(self, param):
        """原始数据详情界面 -> 根据名称选择处理办法"""
        locator_method, locator = raw_data_detail_locator.choose_deal_with
        self.baseControl.input_text(locator_method, locator, param)
        logger.info("原始数据详情界面 -> 根据名称选择处理办法: %s " % param)

    @allure.step("原始数据详情界面 -> 处理按钮")
    def click_deal_with_button(self):
        """原始数据详情界面 -> 处理按钮"""
        self.baseControl.click(*raw_data_detail_locator.deal_with_button)
        logger.info("原始数据详情界面 -> 处理按钮")

    @allure.step("原始数据详情界面 -> 编辑处理方法按钮")
    def click_edit_deal_with_method_button(self):
        """原始数据详情界面 -> 编辑处理方法按钮"""
        self.baseControl.click(*raw_data_detail_locator.edit_deal_with_method_button)
        logger.info("原始数据详情界面 -> 编辑处理方法按钮")

    @allure.step("原始数据详情界面 -> 新建处理方法按钮")
    def click_new_deal_with_method_button(self):
        """原始数据详情界面 -> 新建处理方法按钮"""
        self.baseControl.click(*raw_data_detail_locator.new_deal_with_method_button)
        logger.info("原始数据详情界面 -> 编辑处理方法按钮")

    @allure.step("原始数据详情界面 -> 显示处理方法")
    def click_show_deal_with_method_button(self):
        """原始数据详情界面 -> 显示处理方法"""
        self.baseControl.click(*raw_data_detail_locator.show_deal_with_method_button)
        logger.info("原始数据详情界面 -> 显示处理方法")

    @allure.step("原始数据详情界面 -> 开启系统适应性")
    def click_show_system_adaptability_button(self):
        """原始数据详情界面 -> 开启系统适应性"""
        self.baseControl.click(*raw_data_detail_locator.show_system_adaptability_button)
        logger.info("原始数据详情界面 -> 开启系统适应性")

    @allure.step("原始数据详情界面 -> 自动组分")
    def click_automatic_component_button(self):
        """原始数据详情界面 -> 自动组分"""
        self.baseControl.click(*raw_data_detail_locator.automatic_component_button)
        logger.info("原始数据详情界面 -> 自动组分")

    @allure.step("原始数据详情界面 -> 预处理")
    def click_pretreatment_button(self):
        """原始数据详情界面 -> 预处理"""
        self.baseControl.click(*raw_data_detail_locator.pretreatment_button)
        logger.info("原始数据详情界面 -> 预处理")

    @allure.step("原始数据详情界面 -> 保存按钮")
    def click_save_button(self):
        """原始数据详情界面 -> 保存按钮"""
        self.baseControl.click(*raw_data_detail_locator.save_button)
        logger.info("原始数据详情界面 -> 保存按钮")

    @allure.step("原始数据详情界面 -> 保存方法弹窗 -> 保存方法名称")
    def input_save_method_result_name(self, param):
        """原始数据详情界面 -> 保存方法弹窗 -> 保存方法名称"""
        locator_method, locator = raw_data_detail_locator.save_method_result_name
        self.baseControl.input_text(locator_method, locator, param)
        logger.info("原始数据详情界面 -> 保存方法弹窗 -> 保存方法名称")

    @allure.step("原始数据详情界面 -> 保存方法弹窗 -> 确定按钮")
    def click_save_method_result_confirm(self):
        """原始数据详情界面 -> 保存方法弹窗 -> 确定按钮"""
        self.baseControl.click(*raw_data_detail_locator.save_method_result_confirm)
        logger.info("原始数据详情界面 -> 保存方法弹窗 -> 确定按钮")

    @allure.step("原始数据详情界面 -> 保存方法弹窗 -> 选择保存类型下拉框")
    def click_save_method_result_type(self):
        """原始数据详情界面 -> 保存方法弹窗 -> 选择保存类型下拉框"""
        self.baseControl.click(*raw_data_detail_locator.save_method_result_type)
        logger.info("原始数据详情界面 -> 保存方法弹窗 -> 选择保存类型下拉框")

    @allure.step("原始数据详情界面 -> 保存方法弹窗 -> 选择保存类型")
    def click_choose_type_name(self, param):
        """原始数据详情界面 -> 保存方法弹窗 -> 选择保存类型"""
        locator_method, locator = raw_data_detail_locator.choose_type_name
        self.baseControl.click(locator_method, locator % param)
        logger.info("原始数据详情界面 -> 保存方法弹窗 -> 选择保存类型")

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 一阶积分")
    def click_integral_first_order(self):
        """原始数据详情界面 -> 显示处理方法 -> 一阶积分"""
        self.baseControl.click(*raw_data_detail_locator.integral_first_order)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 一阶积分")

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 二阶积分")
    def click_integral_two_order(self):
        """原始数据详情界面 -> 显示处理方法 -> 二阶积分"""
        self.baseControl.click(*raw_data_detail_locator.integral_two_order)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 二阶积分")

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 分段积分")
    def click_integral_subsection_order(self):
        """原始数据详情界面 -> 显示处理方法 -> 分段积分"""
        self.baseControl.click(*raw_data_detail_locator.integral_subsection_order)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 分段积分")

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 全局积分")
    def click_integral_overall_ordere(self):
        """原始数据详情界面 -> 显示处理方法 -> 全局积分"""
        self.baseControl.click(*raw_data_detail_locator.integral_overall_order)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 全局积分")

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 全局积分-峰宽")
    def input_order_peak_width(self, param):
        """原始数据详情界面 -> 显示处理方法 -> 全局积分-峰宽"""
        locator_method, locator = raw_data_detail_locator.order_peak_width
        self.baseControl.input_text(locator_method, locator, param)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 全局积分-峰宽: %s " % param)

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 全局积分-斜率")
    def input_order_slope(self, param):
        """原始数据详情界面 -> 保存方法弹窗 -> 全局积分-斜率"""
        locator_method, locator = raw_data_detail_locator.order_slope
        self.baseControl.input_text(locator_method, locator, param)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 全局积分-斜率: %s " % param)

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 添加积分事件")
    def click_event_subsection_order_none(self):
        """原始数据详情界面 -> 显示处理方法 -> 添加积分事件"""
        self.baseControl.click(*raw_data_detail_locator.event_subsection_order_none)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 添加积分事件")

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 积分事件-开始时间")
    def input_event_start_time(self, param):
        """原始数据详情界面 -> 显示处理方法 -> 积分事件-开始时间"""
        locator_method, locator = raw_data_detail_locator.event_start_time
        self.baseControl.input_text(locator_method, locator, param)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 积分事件-开始时间: %s " % param)

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 积分事件-结束时间")
    def input_event_end_time(self, param):
        """原始数据详情界面 -> 显示处理方法 -> 积分事件-结束时间"""
        locator_method, locator = raw_data_detail_locator.event_end_time
        self.baseControl.input_text(locator_method, locator, param)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 积分事件-结束时间: %s " % param)

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 积分事件-事件参数")
    def input_order_event_value(self, param):
        """原始数据详情界面 -> 显示处理方法 -> 积分事件-事件参数"""
        sleep(2)
        locator_method, locator = raw_data_detail_locator.order_event_value
        self.baseControl.input_text(locator_method, locator, param)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 积分事件-事件参数: %s " % param)

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 积分事件-事件类型")
    def click_order_event_type(self):
        """原始数据详情界面 -> 显示处理方法 -> 积分事件-事件类型"""
        self.baseControl.click(*raw_data_detail_locator.order_event_type)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 积分事件-事件类型")

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 积分事件-选择事件类型")
    def input_choose_event_name(self, param):
        """原始数据详情界面 -> 显示处理方法 -> 积分事件-选择事件类型"""
        locator_method, locator = raw_data_detail_locator.choose_type_name
        self.baseControl.click(locator_method, locator % param)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 积分事件-选择事件类型: %s " % param)

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 分段积分-添加积分事件")
    def click_subsection_order_none(self):
        """原始数据详情界面 -> 显示处理方法 -> 积段积分-添加积分事件"""
        self.baseControl.click(*raw_data_detail_locator.subsection_order_none)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 段积分-添加积分事件")

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 分段积分-开始时间")
    def input_subsection_order_start_time(self, param):
        """原始数据详情界面 -> 显示处理方法 -> 分段积分-开始时间"""
        locator_method, locator = raw_data_detail_locator.subsection_order_start_time
        self.baseControl.input_text(locator_method, locator, param)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 分段积分-开始时间: %s " % param)

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 分段积分-结束时间")
    def input_subsection_order_end_time(self, param):
        """原始数据详情界面 -> 显示处理方法 -> 分段积分-结束时间"""
        locator_method, locator = raw_data_detail_locator.subsection_order_end_time
        self.baseControl.input_text(locator_method, locator, param)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 分段积分-结束时间: %s " % param)

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 分段积分-峰宽")
    def input_subsection_order_peak_width(self, param):
        """原始数据详情界面 -> 显示处理方法 -> 分段积分-峰宽"""
        locator_method, locator = raw_data_detail_locator.subsection_order_peak_width
        self.baseControl.input_text(locator_method, locator, param)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 分段积分-峰宽: %s " % param)

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 分段积分-斜率")
    def input_subsection_order_slope(self, param):
        """原始数据详情界面 -> 显示处理方法 -> 分段积分-斜率"""
        locator_method, locator = raw_data_detail_locator.subsection_order_slope
        self.baseControl.input_text(locator_method, locator, param)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 分段积分-斜率: %s " % param)

    ### 组分tab
    @allure.step("原始数据详情界面 -> 显示处理方法 -> 点击组分tab")
    def click_constituent_tab(self):
        """原始数据详情界面 -> 显示处理方法 -> 点击组分tab"""
        self.baseControl.click(*raw_data_detail_locator.constituent_tab)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 点击组分tab")

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 组分-添加组分参数")
    def click_component_order_none(self):
        """原始数据详情界面 -> 显示处理方法 -> 组分-添加组分参数"""
        self.baseControl.click(*raw_data_detail_locator.component_order_none)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 组分-添加组分参数")

    @allure.step("原始数据详情界面 -> 显示处理方法 -> 组分-匹配类型")
    def input_accumulate_match_type(self, param):
        """原始数据详情界面 -> 显示处理方法 -> 组分-匹配类型"""
        locator_method, locator = raw_data_detail_locator.accumulate_fit_type
        self.baseControl.input_text(locator_method, locator, param)
        logger.info("原始数据详情界面 -> 显示处理方法 -> 组分-匹配类型: %s " % param)
