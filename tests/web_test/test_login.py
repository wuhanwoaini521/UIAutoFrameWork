import util.settings as settings
from time import sleep

from base.baseControl import BaseControl
from page.login_page import Login_Page
from page.authority_choose_page import Authority_Choose_Page
from util.choose_driver import Choose_Driver
import allure
import pytest
import os
from util.read_file import Read_Yaml

@allure.epic('登录页测试')
class Test_Login:

    # def setup_method(self, driver):
    #     # self.driver = Choose_Driver(settings.DRIVER_NAME).choose_driver()
    #     # self.baseControl = BaseControl(driver)
    #     # self.baseControl.open_url()
    #
    #     self.login_page = Login_Page(driver)  # 登录页面
    #     self.authority_choose_page = Authority_Choose_Page(driver)  # 权限选择页面

    @allure.title("登录成功测试")
    @pytest.mark.parametrize("result_list", Read_Yaml(r"C:\Users\Administrator\Desktop\UIAutoFrameWork\datas\login.yml").read_yaml()["login_success"])
    def test_login_success(self, driver, result_list):
        """
        登录测试用例
        :return:
        """
        self.login_page = Login_Page(driver)  # 登录页面
        self.authority_choose_page = Authority_Choose_Page(driver)
        self.login_page.username_text(result_list["username"])
        self.login_page.password_text(result_list["password"])
        self.login_page.click_login_button()
        assert self.authority_choose_page.show_authority() == "请选择角色"

    @allure.title("登录失败测试")
    @pytest.mark.xfail("就是跳过")
    def test_login_failed(self, driver):
        """
        登录测试用例
        :return:
        """
        self.login_page = Login_Page(driver)  # 登录页面
        self.authority_choose_page = Authority_Choose_Page(driver)
        self.login_page.username_text("wuhan")
        self.login_page.password_text("123456")
        self.login_page.click_login_button()
        assert self.authority_choose_page.show_authority() == "请选择角色1"

    # def teardown_method(self):
    #     sleep(4)
    #     self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'test_login.py', '--clean-alluredir', '--alluredir=outFiles/reports/allure-results'])
    os.system(r"allure generate -c -o outFiles/reports/allure-results")
