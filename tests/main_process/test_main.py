from page.show_project.project_details_page import Project_Details_Page
from page.show_project.raw_data_detail_page import Raw_Data_Detail_Page
from page.show_project.raw_data_tab_page import Raw_Data_Tab_Page
from page.show_project.results_list_page import Results_List_Page
from page.public_page import Public_Page
from page.show_project.method_tab_page import Method_Tab_Page
from tests import *
import allure
import pytest
from util.read_file import Read_Yaml
from tests.login_common import Login_Common
from tests.common import Common
from util.assets import Assert_Control
from locators.raw_data_locator import raw_data_list_locator


@allure.epic("主流程测试")
class Test_main:
    login_common = Login_Common()
    common = Common()

    @allure.title("全局积分测试")
    @pytest.mark.parametrize("result_list", Read_Yaml(login_path).read_yaml()["login_success"])
    @pytest.mark.parametrize("input_param", Read_Yaml(main_test_path).read_yaml()["single_global_success"])
    def test_single_global_success(self, driver, result_list, input_param):
        self.public_page = Public_Page(driver)
        self.public_page.start_project(input_param["project_name"], result_list)

        # 点击方法tab、选择新建方法
        self.project_details_page = Project_Details_Page(driver)
        self.project_details_page.click_tab_method_button()
        self.project_details_page.click_tab_method_create_method_deal_with_method_button()

        # 新建方法
        self.deal_with_method = Deal_With_Method(driver)
        self.deal_with_method.single_global(input_param["peak_with"],
                                            input_param["slope"], input_param["deal_with_name"])

        method_list = self.project_details_page.show_all_method_list_name_button()
        #  判断新建的方法在不在方法列表里面
        assert input_param["deal_with_name"] in self.common.read_method_list(method_list)

        # 第一条原始数据选择方法处理
        self.public_page.choose_first_raw_data_deal(input_param["deal_with_name"])
        # 仅处理
        self.public_page.choose_deal_with_only()

        # 断言积分结果表弹窗是否存在
        asse = Assert_Control(driver)
        asse.assert_isExists(*raw_data_list_locator.view_the_integral_result)
        data1_method, data1 = raw_data_list_locator.view_the_integral_result_datas
        asse.assert_isExists(data1_method, data1 % input_param["data1"])
        asse.assert_isExists(data1_method, data1 % input_param["data2"])
        asse.assert_isExists(data1_method, data1 % input_param["data3"])

        # 积分结果表 -> 确定按钮
        self.raw_data_tab_page = Raw_Data_Tab_Page(driver)
        self.raw_data_tab_page.click_confirm()

        # 进入结果tab -> 进入第一条结果的结果详情 -> 出版报告
        self.project_details_page.click_tab_result_button()
        self.result_list_page = Results_List_Page(driver)
        self.result_list_page.click_some_result(0)
        self.result_list_page.click_report_result_button()
        self.result_list_page.click_info_report_list_button()
        self.result_list_page.click_info_all_report_name(input_param["report_name"])
        self.result_list_page.click_info_report_confirm()

    @allure.title("全局积分+组分")
    @pytest.mark.parametrize("result_list", Read_Yaml(login_path).read_yaml()["login_success"])
    @pytest.mark.parametrize("input_param", Read_Yaml(main_test_path).read_yaml()["global_constituent_success"])
    def test_global_constituent_success(self, driver, result_list, input_param):
        self.public_page = Public_Page(driver)
        self.public_page.start_project(input_param["project_name"], result_list)

        # 点击方法tab、选择新建方法
        self.project_details_page = Project_Details_Page(driver)
        self.project_details_page.click_tab_method_button()
        self.project_details_page.click_tab_method_create_method_deal_with_method_button()

        self.deal_with_method = Deal_With_Method(driver)
        self.deal_with_method.global_constituent(input_param["peak_with"],
                                                 input_param["slope"],
                                                 input_param["constituent_name"], input_param["constituent_param"],
                                                 input_param["constituent_time"], input_param["deal_with_name"])

        method_list = self.project_details_page.show_all_method_list_name_button()
        #  判断新建的方法在不在方法列表里面
        assert input_param["deal_with_name"] in self.common.read_method_list(method_list)

        # 进行曲线拟合操作
        self.method_tab_page = Method_Tab_Page(driver)
        self.method_tab_page.click_img_fit_of_curve()
        self.method_tab_page.click_img_fit_of_curve_alert_choose()
        self.method_tab_page.click_img_fit_of_curve_match_and_fit()
        self.method_tab_page.click_img_fit_of_curve_alert_confirm()
        self.method_tab_page.click_choose_first_raw_data()
        self.method_tab_page.click_choose_raw_data_confirm()

        self.method_tab_page.click_level()
        self.method_tab_page.click_level_select()
        self.method_tab_page.input_create_curve_x(1)
        self.method_tab_page.input_create_curve_unit("q")
        self.method_tab_page.click_create_curve_confirm()

        # # 第一条原始数据选择方法处理
        # self.public_page.choose_first_raw_data_deal(input_param["deal_with_name"])
        # 处理并定量
        # self.public_page.choose_process_and_quantify()

    @allure.title("原始数据详情测试")
    @pytest.mark.parametrize("result_list", Read_Yaml(login_path).read_yaml()["login_success"])
    @pytest.mark.parametrize("input_param", Read_Yaml(main_test_path).read_yaml()["global_constituent_success"])
    def test_raw_data(self, driver, result_list, input_param):
        self.public_page = Public_Page(driver)
        self.public_page.start_project(input_param["project_name"], result_list)

        self.project_details_page = Project_Details_Page(driver)
        # 点击原始数据tab
        self.project_details_page.click_tab_data_button()

        # 进入任意一条原始数据
        self.raw_data_tab_page = Raw_Data_Tab_Page(driver)
        self.raw_data_tab_page.click_raw_data_list_names(0)

        # 进入原始数据详情界面
        self.raw_data_detail_page = Raw_Data_Detail_Page(driver)
        self.raw_data_detail_page.click_new_deal_with_method_button()
        self.raw_data_detail_page.click_show_deal_with_method_button()
        # self.raw_data_detail_page.input_order_peak_width(11)
        # self.raw_data_detail_page.input_order_slope(11)

        # 点击分段积分
        # self.raw_data_detail_page.click_integral_subsection_order()
        # self.raw_data_detail_page.click_subsection_order_none()
        # self.raw_data_detail_page.input_subsection_order_start_time(1)
        # self.raw_data_detail_page.input_subsection_order_end_time(10)
        # self.raw_data_detail_page.input_subsection_order_peak_width(22)
        # self.raw_data_detail_page.input_subsection_order_slope(22)
        #
        # self.raw_data_detail_page.click_event_subsection_order_none()  # 添加积分事件
        #
        # self.raw_data_detail_page.input_event_start_time(11)
        # self.raw_data_detail_page.input_event_end_time(22)
        # self.raw_data_detail_page.click_order_event_type()
        # self.raw_data_detail_page.input_choose_event_name("设定最小高度")
        # self.raw_data_detail_page.input_order_event_value(999)

        # self.raw_data_detail_page.click_save_button()

        # 点击组分tab
        self.raw_data_detail_page.click_constituent_tab()
        self.raw_data_detail_page.click_component_order_none()
        self.raw_data_detail_page.input_accumulate_match_type("线性过原点")

