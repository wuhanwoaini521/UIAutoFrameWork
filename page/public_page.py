from page.navigate_menu_page import Navigate_Menu_Page
from page.show_project.project_details_page import Project_Details_Page
from page.show_project.list_project_page import List_Project_Page
from tests.login_common import Login_Common
from tests.common import Common
from util.log_control import MyLogger

logger = MyLogger()


class Public_Page:

    def __init__(self, driver):
        self.driver = driver
        self.login_common = Login_Common()
        self.common = Common()
        self.navigate_menu = Navigate_Menu_Page(self.driver)
        self.list_project_page = List_Project_Page(self.driver)
        self.project_details_page = Project_Details_Page(self.driver)

    def start_project(self, project_name, result_list):
        """
            登录 -> 选择角色 -> 选择项目
        :param project_name:
        :param result_list:
        :return:
        """
        logger.info("进行连续操作： 登录 -> 选择角色 -> 选择项目")
        self.login_common.login_success(self.driver, result_list)
        self.navigate_menu.click_drawer_button()
        self.navigate_menu.click_show_project_button()
        # 进入查看项目页面、选择任意项目
        self.list_project_page.click_choose_project(project_name)

    def choose_first_raw_data_deal(self, deal_with_name):
        """
            点击原始数据tab -> 选中第一个原始数据 -> 使用新建的方法进行处理
        :param deal_with_name:
        :return:
        """
        logger.info("进行连续操作： 点击原始数据tab -> 选中第一个原始数据 -> 使用新建的方法进行处理")
        self.project_details_page.click_tab_data_button()
        self.project_details_page.click_first_check_box_button()
        self.project_details_page.click_tab_data_deal_with_button()
        self.project_details_page.click_any_name(deal_with_name)

    def choose_deal_with_only(self):
        """
            处理数据弹窗 -> 仅处理 -> 确定
        :return:
        """
        logger.info("进行连续操作： 处理数据弹窗 -> 仅处理 -> 确定")
        self.project_details_page.click_choose_deal_with_way()
        self.project_details_page.click_deal_with_only()
        self.project_details_page.click_confirm_button()

    def choose_process_and_quantify(self):
        """
            处理数据弹窗 -> 处理并定量 -> 确定
        :return:
        """
        logger.info("进行连续操作： 处理数据弹窗 -> 处理并定量 -> 确定")
        self.project_details_page.click_choose_deal_with_way()
        self.project_details_page.click_process_and_quantify()
        self.project_details_page.click_confirm_button()
