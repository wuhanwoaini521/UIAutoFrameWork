
# 按钮
compare_result = ("xpath", "//span[contains(text(),'对比结果')]")
report_result = ("xpath", "//span[contains(text(),'出版报告')]")
export_result = ("xpath", "//span[contains(text(),'导出')]")
lock_result = ("xpath", "//span[contains(text(),'锁定设置')]")
delete_result = ("xpath", "//span[contains(text(),'删除')]")

name_list_result = ("xpath", "//div[@id='applyTable']//span[contains(text(),'%s')]")  # 结果列表的名称
first_check_box = ("xpath", "//div[@id='applyTable']//tr[1]//td[1]//div[1]/label[1]/span[1]/span[1]")
result_list_check_box = ("xpath",
                         "//tbody//tr//label/span")

result_name_lists = ("xpath", "//span[@id='viewitems-components-result-list-sample-name']")  # 结果名称列表

first_report = ("xpath", "//li[@id='viewitems-components-result-publishing-reports0']")  # 第一个出版报告

all_report_name = ("xpath", "//li[contains(text(),'%s')]")  # 用名称找出版报告 (结果列表 页面)



# 结果详情页面，出版报告下拉框
info_report_list = ("id", "viewitems-components-result-details-peak-label-select")
info_all_report_name = ("xpath", "//span[contains(text(),'%s')]")  # 用名称找出版报告 (结果详情 页面)
info_report_confirm = ("id", "viewitems-components-result-details-peak-label-sure")
info_report_cancel = ("id", "viewitems-components-result-details-peak-label-cane")
