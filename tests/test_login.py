import util.settings as settings
from time import sleep
from page.login_page import Login_Page
from page.authority_choose_page import Authority_Choose_Page
from util.choose_driver import Choose_Driver
import allure
import pytest
import os


@allure.feature('登录页测试')
class Test_Login:

    def setup_method(self):
        self.driver = Choose_Driver(settings.DRIVER_NAME).choose_driver()
        self.login_page = Login_Page(self.driver)
        self.authority_choose_page = Authority_Choose_Page(self.driver)
        self.driver.get(settings.WEB_TEST_BASE_URL)

    @allure.title("登录成功测试")
    def test_login_success(self):
        """
        登录测试用例
        :return:
        """
        self.login_page.username_text("wuhan")
        self.login_page.password_text("123456")
        self.login_page.click_login_button()
        assert self.authority_choose_page.show_authority() == "请选择角色"

    @allure.title("登录失败测试")
    def test_login_failed(self):
        """
        登录测试用例
        :return:
        """
        self.login_page.username_text("wuhan")
        self.login_page.password_text("123456")
        self.login_page.click_login_button()
        assert self.authority_choose_page.show_authority() == "请选择角色1"

    def teardown_method(self):
        sleep(4)
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'test_login.py', '--clean-alluredir', '--alluredir=outFiles/reports/allure-results'])
    os.system(r"allure generate -c -o outFiles/reports/allure-results")