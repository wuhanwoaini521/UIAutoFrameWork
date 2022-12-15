from locators.methods import new_deal_with_locator
from base.baseControl import BaseControl
from util.log_control import MyLogger
import allure

logger = MyLogger()


@allure.epic("方法页 - 新建处理方法")
class New_Method_Page:
    """
    方法页新建处理方法
    """

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
        logger.info("输入仪器方法的名称: %s" % name)

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

    @allure.step("点击组分tab")
    def click_open_constituent_tab(self):
        """保存按钮"""
        self.baseControl.click(*new_deal_with_locator.open_constituent)
        logger.info("点击组分tab")

    @allure.step("点击开启系统适应性按钮")
    def click_open_system_adaptation_button(self):
        """保存按钮"""
        self.baseControl.click(*new_deal_with_locator.open_system_adaptation)
        logger.info("点击开启系统适应性按钮")

    @allure.step("点击关闭系统适应性按钮")
    def click_close_system_adaptation_button(self):
        """保存按钮"""
        self.baseControl.click(*new_deal_with_locator.close_system_adaptation)
        logger.info("点击关闭系统适应性按钮")

    @allure.step("点击开启pda按钮")
    def click_open_pda_button(self):
        """保存按钮"""
        self.baseControl.click(*new_deal_with_locator.open_pda)
        logger.info("点击开启pda按钮")

    @allure.step("点击关闭pda按钮")
    def click_close_pda_button(self):
        """保存按钮"""
        self.baseControl.click(*new_deal_with_locator.close_pda)
        logger.info("点击关闭pda按钮")

    @allure.step("输入峰宽")
    def input_peak_width(self, name):
        """输入仪器方法的名称"""
        self.baseControl.input_text(*new_deal_with_locator.peak_width, name)
        logger.info("输入峰宽: %s" % name)

    @allure.step("输入斜率")
    def input_slope(self, name):
        """输入仪器方法的名称"""
        self.baseControl.input_text(*new_deal_with_locator.slope, name)
        logger.info("输入斜率: %s" % name)

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

    ######积分事件参数####################################################################

    @allure.step("输入开始时间")
    def input_integral_event_start_time(self, param):
        """输入开始时间"""
        self.baseControl.input_text(*new_deal_with_locator.integral_event_start_time, param)
        logger.info("输入开始时间: %s" % param)

    @allure.step("输入结束时间")
    def input_integral_event_end_time(self, param):
        """输入结束时间"""
        self.baseControl.input_text(*new_deal_with_locator.integral_event_end_time, param)
        logger.info("输入结束时间: %s" % param)

    @allure.step("点击事件类型")
    def input_integral_event_type(self):
        """点击事件类型"""
        self.baseControl.click(*new_deal_with_locator.integral_event_type)
        logger.info("点击事件类型")

    @allure.step("选中事件类型")
    def input_integral_event_type(self, param):
        """点击事件类型"""
        locator_method, locator = new_deal_with_locator.integral_event_type_section
        self.baseControl.click(locator_method, locator % param)
        logger.info("选中事件类型")

    @allure.step("输入事件参数")
    def input_integral_event_param(self, param):
        """输入事件参数"""
        self.baseControl.input_text(*new_deal_with_locator.integral_event_param, param)
        logger.info("输入事件参数: %s" % param)

    ######分段积分参数#########################################################################

    @allure.step("点击添加分段积分参数按钮")
    def click_add_second_order_integralevent_button(self):
        """点击添加分段积分参数按钮"""
        locator_method, locator = new_deal_with_locator.add_second_order_integralevent
        self.baseControl.click(locator_method, locator)
        logger.info("点击添加分段积分参数按钮")

    @allure.step("分段积分-开始时间")
    def input_subsection_order_start_time_param(self, param):
        """分段积分-开始时间"""
        self.baseControl.input_text(*new_deal_with_locator.subsection_order_start_time, param)
        logger.info("分段积分-开始时间: %s" % param)

    @allure.step("分段积分-结束时间")
    def input_subsection_order_end_time_param(self, param):
        """分段积分-结束时间"""
        self.baseControl.input_text(*new_deal_with_locator.subsection_order_end_time, param)
        logger.info("分段积分-结束时间: %s" % param)

    @allure.step("分段积分-峰宽")
    def input_subsection_order_peak_width_param(self, param):
        """分段积分-峰宽"""
        self.baseControl.input_text(*new_deal_with_locator.subsection_order_peak_width, param)
        logger.info("分段积分-峰宽: %s" % param)

    @allure.step("分段积分-斜率")
    def input_subsection_order_slope_param(self, param):
        """分段积分-斜率"""
        self.baseControl.input_text(*new_deal_with_locator.subsection_order_slope, param)
        logger.info("分段积分-斜率: %s" % param)

    ######组分tab####################################################################

    @allure.step("点击添加组分参数按钮")
    def click_open_constituent_add_button_button(self):
        """点击添加组分参数按钮"""
        locator_method, locator = new_deal_with_locator.open_constituent_add_button
        # elements = self.baseControl.find_elements(locator_method, locator)
        # element = elements[0]
        # element.click()
        self.baseControl.click(locator_method, locator)
        logger.info("点击添加组分参数按钮")

    @allure.step("组分名称")
    def input_open_constituent_name_param(self, param):
        """组分名称"""
        self.baseControl.input_text(*new_deal_with_locator.open_constituent_name, param)
        logger.info("组分名称: %s" % param)

    @allure.step("匹配类型")
    def input_open_constituent_type_param(self):
        """匹配类型"""
        self.baseControl.click(*new_deal_with_locator.open_constituent_type)
        logger.info("匹配类型")

    @allure.step("匹配值")
    def input_open_constituent_param(self, param):
        """匹配值"""
        self.baseControl.input_text(*new_deal_with_locator.open_constituent_param, param)
        logger.info("匹配值: %s" % param)

    @allure.step("匹配窗口")
    def input_open_constituent_time_param(self, param):
        """匹配窗口"""
        self.baseControl.input_text(*new_deal_with_locator.open_constituent_time, param)
        logger.info("匹配窗口: %s" % param)

    @allure.step("拟合类型")
    def input_open_constituent_fitting_type_param(self):
        """拟合类型"""
        self.baseControl.click(*new_deal_with_locator.open_constituent_fitting_type)
        logger.info("拟合类型")

    @allure.step("X轴")
    def input_open_constituent_x_param(self):
        """X轴"""
        self.baseControl.click(*new_deal_with_locator.open_constituent_x)
        logger.info("X轴")

    @allure.step("Y轴")
    def input_open_constituent_y_param(self):
        """Y轴"""
        self.baseControl.click(*new_deal_with_locator.open_constituent_y)
        logger.info("Y轴")

    @allure.step("下拉框自定义选择内容")
    def input_open_constituent_y_param(self, param):
        """下拉框自定义选择内容"""
        locator_method, locator = new_deal_with_locator.open_constituent_y
        self.baseControl.click(locator_method, locator % param)
        logger.info("下拉框自定义选择内容" % param )

    ######系统适应性tab####################################################################

    @allure.step("空体积时间")
    def input_open_system_adaptation_empty_volume_time_param(self, param):
        """空体积时间"""
        self.baseControl.input_text(*new_deal_with_locator.open_system_adaptation_empty_volume_time, param)
        logger.info("空体积时间: %s" % param)

    @allure.step("色谱柱长度")
    def input_open_system_adaptation_suitparams_column_length_param(self, param):
        """色谱柱长度"""
        self.baseControl.input_text(*new_deal_with_locator.open_system_adaptation_suitparams_column_length, param)
        logger.info("色谱柱长度: %s" % param)

    @allure.step("最大允许噪音")
    def input_open_system_adaptation_baseline_noise_max_param(self, param):
        """最大允许噪音"""
        self.baseControl.input_text(*new_deal_with_locator.open_system_adaptation_baseline_noise_max, param)
        logger.info("最大允许噪音: %s" % param)

    @allure.step("最大允许漂移")
    def input_open_system_adaptation_baseline_drift_max_param(self, param):
        """最大允许漂移"""
        self.baseControl.input_text(*new_deal_with_locator.open_system_adaptation_baseline_drift_max, param)
        logger.info("最大允许漂移: %s" % param)

    @allure.step("平均运行时间")
    def input_open_system_adaptation_baseline_running_time_param(self, param):
        """平均运行时间"""
        self.baseControl.input_text(*new_deal_with_locator.open_system_adaptation_baseline_running_time, param)
        logger.info("平均运行时间: %s" % param)

    @allure.step("基线开始时间")
    def input_open_system_adaptation_baseline_start_time_param(self, param):
        """基线开始时间"""
        self.baseControl.input_text(*new_deal_with_locator.open_system_adaptation_baseline_start_time, param)
        logger.info("基线开始时间: %s" % param)

    @allure.step("基线结束时间")
    def input_open_system_adaptation_baseline_end_time_param(self, param):
        """基线结束时间"""
        self.baseControl.input_text(*new_deal_with_locator.open_system_adaptation_baseline_end_time, param)
        logger.info("基线结束时间: %s" % param)

    @allure.step("计算检测器噪音和漂移基线开始时间")
    def input_open_system_adaptation_computer_baseline_start_time_param(self, param):
        """计算检测器噪音和漂移基线开始时间"""
        self.baseControl.input_text(*new_deal_with_locator.open_system_adaptation_computer_baseline_start_time, param)
        logger.info("计算检测器噪音和漂移基线开始时间: %s" % param)

    @allure.step("计算检测器噪音和漂移基线结束时间")
    def input_open_system_adaptation_computer_baseline_end_time_param(self, param):
        """计算检测器噪音和漂移基线结束时间"""
        self.baseControl.input_text(*new_deal_with_locator.open_system_adaptation_computer_baseline_end_time, param)
        logger.info("计算检测器噪音和漂移基线结束时间: %s" % param)

    @allure.step("切片宽度")
    def input_open_system_adaptation_pda_slice_width_param(self, param):
        """切片宽度"""
        self.baseControl.input_text(*new_deal_with_locator.open_system_adaptation_pda_slice_width, param)
        logger.info("切片宽度: %s" % param)

    ######PDAtab####################################################################

    @allure.step("波长")
    def input_open_pda_wavelength_param(self, param):
        """波长"""
        self.baseControl.input_text(*new_deal_with_locator.open_pda_wavelength, param)
        logger.info("波长: %s" % param)

    @allure.step("波长范围开始点")
    def input_open_pda_wavelength_start_param(self, param):
        """波长范围开始点"""
        self.baseControl.input_text(*new_deal_with_locator.open_pda_wavelength_start, param)
        logger.info("波长范围开始点: %s" % param)

    @allure.step("波长范围结束点")
    def input_open_pda_wavelength_end_param(self, param):
        """波长范围结束点"""
        self.baseControl.input_text(*new_deal_with_locator.open_pda_wavelength_end, param)
        logger.info("波长范围结束点: %s" % param)

    @allure.step("光谱库")
    def input_open_pda_spectral_library_param(self):
        """切片宽度"""
        self.baseControl.click(*new_deal_with_locator.open_pda_spectral_library)
        logger.info("光谱库")

    @allure.step("点击光谱库名称")
    def click_open_pda_spectral_library_name(self, param):
        """点击光谱库名称"""
        locator_method, locator = new_deal_with_locator.open_pda_spectral_library_name
        self.baseControl.click(locator_method, locator % param)
        logger.info("点击光谱库名称: %s" % param)
