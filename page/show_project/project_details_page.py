from locators import show_project_locator
from base.baseControl import BaseControl
from util.log_control import MyLogger
import allure

logger = MyLogger()


class Project_Details_Page:
    """
    项目详情页
    """

    def __init__(self, driver):
        self.driver = driver
        self.baseControl = BaseControl(self.driver)

    @allure.step("点击tab序列")
    def click_tab_sequence_button(self):
        """点击tab序列"""
        self.baseControl.click(*show_project_locator.tab_sequence)
        logger.info("点击tab序列")

    @allure.step("点击tab进样")
    def click_tab_injection_button(self):
        """点击tab进样"""
        self.baseControl.click(*show_project_locator.tab_injection)
        logger.info("点击tab进样")

    @allure.step("点击tab原始数据")
    def click_tab_data_button(self):
        """点击tab原始数据"""
        self.baseControl.click(*show_project_locator.tab_data)
        logger.info("点击tab原始数据")

    @allure.step("点击tab方法")
    def click_tab_method_button(self):
        """点击tab方法"""
        self.baseControl.click(*show_project_locator.tab_method)
        logger.info("点击tab方法")

    @allure.step("点击tab曲线")
    def click_tab_curve_button(self):
        """点击tab曲线"""
        self.baseControl.click(*show_project_locator.tab_curve)
        logger.info("点击tab曲线")

    @allure.step("点击tab结果组")
    def click_tab_resultGroup_button(self):
        """点击tab结果组"""
        self.baseControl.click(*show_project_locator.tab_resultGroup)
        logger.info("点击tab结果组")

    @allure.step("点击tab结果")
    def click_tab_result_button(self):
        """点击tab结果"""
        self.baseControl.click(*show_project_locator.tab_result)
        logger.info("点击tab结果")

    ######################################################################
    ######################################################################

    # 序列tab
    @allure.step("点击tab序列 - 锁定设置")
    def click_tab_sequence_lock_button(self):
        """点击tab序列"""
        self.click_tab_sequence_button()
        self.baseControl.click(*show_project_locator.tab_sequence_lock)
        logger.info("点击tab序列 - 锁定设置")

    @allure.step("点击tab序列 - 删除")
    def click_tab_sequence_delete_button(self):
        """点击tab序列"""
        self.click_tab_sequence_button()
        self.baseControl.click(*show_project_locator.tab_sequence_delete)
        logger.info("点击tab序列 - 删除")

    ######################################################################

    # 进样tab
    @allure.step("点击tab进样 - 锁定设置")
    def click_tab_injection_lock_button(self):
        """点击tab序列"""
        self.click_tab_injection_button()
        self.baseControl.click(*show_project_locator.tab_injection_lock)
        logger.info("点击tab进样 - 锁定设置")

    @allure.step("点击tab进样 - 删除")
    def click_tab_injection_delete_button(self):
        """点击tab序列"""
        self.click_tab_injection_button()
        self.baseControl.click(*show_project_locator.tab_injection_delete)
        logger.info("点击tab进样 - 删除")

    ######################################################################

    # 原始数据tab
    @allure.step("点击tab原始数据 - 序列")
    def click_tab_data_sequence_button(self):
        """点击tab序列"""
        self.click_tab_data_button()
        self.baseControl.click(*show_project_locator.tab_data_sequence)
        logger.info("点击tab原始数据 - 序列")

    @allure.step("点击tab原始数据 - 处理")
    def click_tab_data_deal_with_button(self):
        """点击tab序列"""
        self.click_tab_data_button()
        self.baseControl.click(*show_project_locator.tab_data_deal_with)
        logger.info("点击tab原始数据 - 处理")

    @allure.step("点击tab原始数据 - 对比")
    def click_tab_data_compare_button(self):
        """点击tab序列"""
        self.click_tab_data_button()
        self.baseControl.click(*show_project_locator.tab_data_compare)
        logger.info("点击tab原始数据 - 对比")

    @allure.step("点击tab原始数据 - 修改样品类型")
    def click_tab_data_update_sample_type_button(self):
        """点击tab序列"""
        self.click_tab_data_button()
        self.baseControl.click(*show_project_locator.tab_data_update_sample_type)
        logger.info("点击tab原始数据 - 修改样品类型")

    @allure.step("点击tab原始数据 - 导出")
    def click_tab_data_export_button(self):
        """点击tab序列"""
        self.click_tab_data_button()
        self.baseControl.click(*show_project_locator.tab_data_export)
        logger.info("点击tab原始数据 - 导出")

    @allure.step("点击tab原始数据 - 锁定设置")
    def click_tab_data_lock_button(self):
        """点击tab序列"""
        self.click_tab_data_button()
        self.baseControl.click(*show_project_locator.tab_data_lock)
        logger.info("点击tab原始数据 - 锁定设置")

    @allure.step("点击tab原始数据 - 提取2D")
    def click_tab_data_extract_button(self):
        """点击tab序列"""
        self.click_tab_data_button()
        self.baseControl.click(*show_project_locator.tab_data_extract)
        logger.info("点击tab原始数据 - 提取2D")

    @allure.step("点击tab原始数据 - 删除")
    def click_tab_data_delete_button(self):
        """点击tab序列"""
        self.click_tab_data_button()
        self.baseControl.click(*show_project_locator.tab_data_delete)
        logger.info("点击tab原始数据 - 删除")

    ######################################################################

    # 方法tab
    @allure.step("点击tab方法 - 上传至用户方法库")
    def click_tab_method_upload_button(self):
        """点击tab序列"""
        self.click_tab_method_button()
        self.baseControl.click(*show_project_locator.tab_method_upload)
        logger.info("点击tab方法 - 上传至用户方法库")

    @allure.step("点击tab方法 - 序列")
    def click_tab_method_sequence_button(self):
        """点击tab序列"""
        self.click_tab_method_button()
        self.baseControl.click(*show_project_locator.tab_method_sequence)
        logger.info("点击tab方法 - 序列")

    @allure.step("点击tab方法 - 新建方法")
    def click_tab_method_create_method_button(self):
        """点击tab序列"""
        self.click_tab_method_button()
        self.baseControl.click(*show_project_locator.tab_method_create_method)
        logger.info("点击tab方法 - 新建方法")

    @allure.step("点击tab方法 - 导出")
    def click_tab_method_export_button(self):
        """点击tab序列"""
        self.click_tab_method_button()
        self.baseControl.click(*show_project_locator.tab_method_export)
        logger.info("点击tab方法 - 导出")

    @allure.step("点击tab方法 - 锁定设置")
    def click_tab_method_lock_button(self):
        """点击tab序列"""
        self.click_tab_method_button()
        self.baseControl.click(*show_project_locator.tab_method_lock)
        logger.info("点击tab方法 - 锁定设置")

    @allure.step("点击tab方法 - 删除")
    def click_tab_method_delete_button(self):
        """点击tab序列"""
        self.click_tab_method_button()
        self.baseControl.click(*show_project_locator.tab_method_delete)
        logger.info("点击tab方法 - 删除")

    @allure.step("点击tab方法 - 新建方法 - 处理方法")
    def click_tab_method_create_method_deal_with_method_button(self):
        """点击tab序列"""
        self.click_tab_method_button()
        self.click_tab_method_create_method_button()
        self.baseControl.click(*show_project_locator.tab_method_create_method_deal_with_method)
        logger.info("点击tab方法 - 处理方法")

    @allure.step("点击tab方法 - 新建方法 - 仪器方法")
    def click_tab_method_create_method_instrument_method_button(self):
        """点击tab序列"""
        self.click_tab_method_button()
        self.click_tab_method_create_method_button()
        self.baseControl.click(*show_project_locator.tab_method_create_method_instrument_method)
        logger.info("点击tab方法 - 仪器方法")

    @allure.step("点击tab方法 - 新建方法 - 报告方法")
    def click_tab_method_create_method_report_method_button(self):
        """点击tab序列"""
        self.click_tab_method_button()
        self.click_tab_method_create_method_button()
        self.baseControl.click(*show_project_locator.tab_method_create_method_report_method)
        logger.info("点击tab方法 - 报告方法")

    @allure.step("点击tab方法 - 方法列表某一方法名称")
    def show_method_list_name_button(self, method_name):
        """点击tab序列"""
        located_method, locator = show_project_locator.method_list_name
        self.baseControl.get_text(located_method, locator % method_name)
        logger.info("点击tab方法 - 方法列表某一方法名称")

    @allure.step("点击tab方法 - 获取方法列表内所有方法的名称")
    def show_all_method_list_name_button(self):
        """点击tab序列"""
        located_method, locator = show_project_locator.tab_method_list_name
        method_list = self.baseControl.find_elements(located_method, locator)
        logger.info("点击tab方法 - 获取方法列表内所有方法的名称")
        return method_list

    ######################################################################

    # 曲线tab
    @allure.step("点击tab曲线 - 序列")
    def click_tab_curve_sequence_button(self):
        """点击tab序列"""
        self.click_tab_curve_button()
        self.baseControl.click(*show_project_locator.tab_curve_sequence)
        logger.info("点击tab曲线 - 序列")

    @allure.step("点击tab曲线 - 导出")
    def click_tab_curve_export_button(self):
        """点击tab序列"""
        self.click_tab_curve_button()
        self.baseControl.click(*show_project_locator.tab_curve_export)
        logger.info("点击tab曲线 - 导出")

    @allure.step("点击tab曲线 - 删除")
    def click_tab_curve_delete_button(self):
        """点击tab序列"""
        self.click_tab_curve_button()
        self.baseControl.click(*show_project_locator.tab_curve_delete)
        logger.info("点击tab曲线 - 删除")

    ######################################################################

    # 结果组tab
    @allure.step("点击tab结果组 - 序列")
    def click_tab_resultGroup_sequence_button(self):
        """点击tab序列"""
        self.click_tab_resultGroup_button()
        self.baseControl.click(*show_project_locator.tab_resultGroup_sequence)
        logger.info("点击tab结果组 - 序列")

    @allure.step("点击tab结果组 - 锁定设置")
    def click_tab_resultGroup_lock_button(self):
        """点击tab序列"""
        self.click_tab_resultGroup_button()
        self.baseControl.click(*show_project_locator.tab_resultGroup_lock)
        logger.info("点击tab结果组 - 锁定设置")

    @allure.step("点击tab结果组 - 删除")
    def click_tab_resultGroup_delete_button(self):
        """点击tab序列"""
        self.click_tab_resultGroup_button()
        self.baseControl.click(*show_project_locator.tab_resultGroup_delete)
        logger.info("点击tab结果组 - 删除")

    ######################################################################

    # 结果tab
    @allure.step("点击tab结果 - 序列")
    def click_tab_result_sequence_button(self):
        """点击tab序列"""
        self.click_tab_result_button()
        self.baseControl.click(*show_project_locator.tab_result_sequence)
        logger.info("点击tab结果 - 序列")

    @allure.step("点击tab结果 - 删除")
    def click_tab_result_compare_button(self):
        """点击tab序列"""
        self.click_tab_result_button()
        self.baseControl.click(*show_project_locator.tab_result_compare)
        logger.info("点击tab结果 - 删除")

    @allure.step("点击tab结果 - 删除")
    def click_tab_result_publish_button(self):
        """点击tab序列"""
        self.click_tab_result_button()
        self.baseControl.click(*show_project_locator.tab_result_publish)
        logger.info("点击tab结果 - 删除")

    @allure.step("点击tab结果 - 删除")
    def click_tab_result_export_button(self):
        """点击tab序列"""
        self.click_tab_result_button()
        self.baseControl.click(*show_project_locator.tab_result_export)
        logger.info("点击tab结果 - 删除")

    @allure.step("点击tab结果 - 删除")
    def click_tab_result_lock_button(self):
        """点击tab序列"""
        self.click_tab_result_button()
        self.baseControl.click(*show_project_locator.tab_result_lock)
        logger.info("点击tab结果 - 删除")

    @allure.step("点击tab结果 - 删除")
    def click_tab_result_delete_button(self):
        """点击tab序列"""
        self.click_tab_result_button()
        self.baseControl.click(*show_project_locator.tab_result_delete)
        logger.info("点击tab结果 - 删除")

    ######################################################################


