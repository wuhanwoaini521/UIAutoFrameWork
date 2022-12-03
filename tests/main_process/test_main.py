import util.settings as settings
from time import sleep

from base.baseControl import BaseControl
from page.login_page import Login_Page
from page.authority_choose_page import Authority_Choose_Page
from page.navigate_menu_page import Navigate_Menu_Page
from page.show_project.project_details_page import Project_Details_Page
from page.show_project.list_project_page import List_Project_Page
from page.show_project.new_method_page import New_Method_Page
from tests import *
from util.choose_driver import Choose_Driver
import allure
import pytest
import os
from util.read_file import Read_Yaml
from tests.login_common import Login_Common
from tests.common import Common


@allure.epic("主流程测试")
class Test_main:

    login_common = Login_Common()
    common = Common()

    @allure.title("主流程测试")
    @pytest.mark.parametrize("result_list", Read_Yaml(login_path).read_yaml()["login_success"])
    @pytest.mark.parametrize("input_param", Read_Yaml(main_test_path).read_yaml()["save_success"])
    def test_create_project(self, driver, result_list, input_param):
        self.login_common.login_success(driver, result_list)  # 登录成功
        self.navigate_menu = Navigate_Menu_Page(driver)
        self.navigate_menu.click_drawer_button()
        self.navigate_menu.click_show_project_button()
        # 进入查看项目页面、选择任意项目
        self.list_project_page = List_Project_Page(driver)
        print(input_param["project_name"])

        self.list_project_page.click_choose_project(input_param["project_name"])

        # 点击方法tab、选择新建方法
        self.project_details_page = Project_Details_Page(driver)
        self.project_details_page.click_tab_method_create_method_deal_with_method_button()
        # 获取当前页面url判断一下 /viewitems/processingmethod
        self.baseControl = BaseControl(driver)

        # 点击保存按钮
        self.new_method_page = New_Method_Page(driver)
        self.new_method_page.input_peak_width(input_param["peak_with"])
        self.new_method_page.input_slope(input_param["slope"])
        self.new_method_page.click_new_method_save_button()

        self.new_method_page.input_alert_save_deal_with_method_input(input_param["deal_with_name"])
        self.new_method_page.click_alert_save_deal_with_method_confirm_button()

        method_list = self.project_details_page.show_all_method_list_name_button()
        assert input_param["deal_with_name"] in self.common.read_method_list(method_list)

    def delete_project(self):
        # 删除项目前 应该要有项目呗创建，可以用接口造一些测试数据
        pass
