from locators import show_project_locator
from base.baseControl import BaseControl
from util.log_control import MyLogger
import allure

logger = MyLogger()


class List_Project_Page:
    """
    查看项目 - 项目列表页面
    """

    def __init__(self, driver):
        self.driver = driver
        self.baseControl = BaseControl(self.driver)

    # 公用
    @allure.step("点击{description}按钮")
    def click_button(self, button_name, description):
        """点击按钮"""
        self.baseControl.click(*button_name)
        logger.info("点击【%s】按钮" % description)

    @allure.step("点击新建项目按钮")
    def click_create_project(self):
        """新建项目"""
        self.baseControl.click(*show_project_locator.create_project)
        logger.info("点击新建项目按钮")

    @allure.step("点击项目备份按钮")
    def click_backup_project(self):
        """项目备份"""
        self.baseControl.click(*show_project_locator.create_project)
        logger.info("点击项目备份按钮")

    @allure.step("点击项目还原按钮")
    def click_restore_project(self):
        """项目还原"""
        self.baseControl.click(*show_project_locator.create_project)
        logger.info("点击项目还原按钮")

    @allure.step("点击上传至典型项目按钮")
    def click_load_project(self):
        """上传至典型项目"""
        self.baseControl.click(*show_project_locator.create_project)
        logger.info("点击上传至典型项目按钮")

    @allure.step("点击删除项目按钮")
    def click_load_project(self):
        """删除按钮"""
        self.baseControl.click(*show_project_locator.delete_project)
        logger.info("点击删除项目按钮")

    @allure.step("选择项目")
    def click_choose_project(self, project_name):
        """选择项目"""
        locator, name = show_project_locator.name_project
        self.baseControl.click(locator, name % project_name)
        logger.info("选择项目: %s" % project_name)

