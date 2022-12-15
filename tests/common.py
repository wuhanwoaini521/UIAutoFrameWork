import util.settings as settings
from time import sleep

from base.baseControl import BaseControl
from page.login_page import Login_Page
from page.authority_choose_page import Authority_Choose_Page
from page.show_project.project_details_page import Project_Details_Page
from tests import *
from util.choose_driver import Choose_Driver
import allure
import pytest
import os

from util.log_control import MyLogger
from util.read_file import Read_Yaml

logger = MyLogger()


class Common:

    def __init__(self):
        self.authority_choose_page = None
        self.login_page = None
        self.project_details_page = None

    @allure.step("获取方法页所有方法名称")
    def read_method_list(self, locator):
        method_name = []

        for lo in locator:
            text = lo.text
            method_name.append(text)

        return method_name

    @allure.step("返回结果tab页的checkbox")
    def read_result_list(self, locator):
        result_checkbox = []

        for ele in locator:
            result_checkbox.append(ele)

        print(result_checkbox)
        return result_checkbox
