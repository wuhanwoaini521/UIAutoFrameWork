import time

from locators import login_locator
from base.baseControl import BaseControl
from util.log_control import MyLogger
import allure

logger = MyLogger()


class Navigate_Menu_Page:
    """
        页面左侧导航
    """

    def __init__(self, driver):
        self.driver = driver
        self.baseControl = BaseControl(self.driver)

    @allure.step("点击抽屉按钮")
    def click_drawer_button(self):
        self.baseControl.click(*login_locator.drawer_switch)
        logger.info("点击抽屉按钮")

    @allure.step("点击项目管理")
    def click_manage_project_button(self):
        self.baseControl.click(*login_locator.manage_project)
        logger.info("点击项目管理")

    @allure.step("点击系统管理")
    def click_manage_system_button(self):
        self.baseControl.click(*login_locator.system_manage)
        logger.info("点击系统管理")

    @allure.step("点击设备管理")
    def click_manage_equipment_button(self):
        self.baseControl.click(*login_locator.equipment_manage)
        logger.info("点击设备管理")

    @allure.step("点击知识库")
    def click_knowledge_base_button(self):
        self.baseControl.click(*login_locator.knowledge_base)
        logger.info("点击知识库")

    @allure.step("点击方法库")
    def click_method_library_button(self):
        self.baseControl.click(*login_locator.method_library)
        logger.info("点击方法库")

    #########################################################
    #########################################################

    @allure.step("点击查看项目")
    def click_show_project_button(self):
        self.click_manage_project_button()
        # time.sleep(2)
        self.baseControl.click(*login_locator.show_project)
        logger.info("点击查看项目")

    @allure.step("点击项目对比")
    def click_compare_project_button(self):
        self.click_manage_project_button()
        self.baseControl.click(*login_locator.compare_project)
        logger.info("点击项目对比")

    #########################################################

    @allure.step("点击角色管理")
    def click_role_manage_button(self):
        self.click_manage_system_button()
        self.baseControl.click(*login_locator.role_manage)
        logger.info("点击角色管理")

    @allure.step("点击组织管理")
    def click_organizaton_manage_button(self):
        self.click_manage_system_button()
        self.baseControl.click(*login_locator.organizaton_manage)
        logger.info("点击组织管理")

    @allure.step("点击用户管理")
    def click_user_manage_button(self):
        self.click_manage_system_button()
        self.baseControl.click(*login_locator.user_manage)
        logger.info("点击用户管理")

    @allure.step("点击安全中心")
    def click_safe_center_button(self):
        self.click_manage_system_button()
        self.baseControl.click(*login_locator.safe_center)
        logger.info("点击安全中心")

    @allure.step("点击审计管理")
    def click_audit_manage_button(self):
        self.click_manage_system_button()
        self.baseControl.click(*login_locator.audit_manage)
        logger.info("点击审计管理")

    #########################################################
    @allure.step("点击工作站")
    def click_workstation_button(self):
        self.click_manage_equipment_button()
        self.baseControl.click(*login_locator.workstation)
        logger.info("点击工作站")

    @allure.step("点击仪器分析")
    def click_instru_analysis_button(self):
        self.click_manage_equipment_button()
        self.baseControl.click(*login_locator.instru_analysis)
        logger.info("点击仪器分析")

    @allure.step("点击仪器系统")
    def click_instru_system_button(self):
        self.click_manage_equipment_button()
        self.baseControl.click(*login_locator.instru_system)
        logger.info("点击仪器系统")

    #########################################################

    @allure.step("点击文章列表")
    def click_article_list_button(self):
        self.click_knowledge_base_button()
        self.baseControl.click(*login_locator.article_list)
        logger.info("点击文章列表")

    @allure.step("点击我的收藏")
    def click_collection_button(self):
        self.click_knowledge_base_button()
        self.baseControl.click(*login_locator.collection)
        logger.info("点击我的收藏")

    #########################################################

    @allure.step("点击标准方法库")
    def click_standard_method_library_button(self):
        self.click_method_library_button()
        self.baseControl.click(*login_locator.standard_method_library)
        logger.info("点击标准方法库")

    @allure.step("点击用户方法库")
    def click_user_method_library_button(self):
        self.click_method_library_button()
        self.baseControl.click(*login_locator.user_method_library)
        logger.info("点击用户方法库")

    @allure.step("点击典型项目")
    def click_typical_project_button(self):
        self.click_method_library_button()
        self.baseControl.click(*login_locator.typical_project)
        logger.info("点击典型项目")

    @allure.step("点击光谱库")
    def click_spectral_library_button(self):
        self.click_method_library_button()
        self.baseControl.click(*login_locator.spectral_library)
        logger.info("点击光谱库")
