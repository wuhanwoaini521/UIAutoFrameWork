import util.settings as settings
from time import sleep

from base.baseControl import BaseControl
from page.login_page import Login_Page
from page.authority_choose_page import Authority_Choose_Page
from tests import *
from util.choose_driver import Choose_Driver
import allure
import pytest
import os

from util.log_control import MyLogger
from util.read_file import Read_Yaml

logger = MyLogger()


class Login_Common:

    def __init__(self):
        self.authority_choose_page = None
        self.login_page = None

    @allure.step("登录用户操作")
    def login_success(self, driver, result_list):
        """
        登录测试用例
        :return:
        """
        self.login_page = Login_Page(driver)  # 登录页面
        self.authority_choose_page = Authority_Choose_Page(driver)
        self.login_page.username_text(result_list["username"])
        self.login_page.password_text(result_list["password"])
        self.login_page.click_login_button()

        self.login_page.show_password_due_to_remind_banner("密码将要到期请修改密码")  # 试试

        self.authority_choose_page.click_system_role()
