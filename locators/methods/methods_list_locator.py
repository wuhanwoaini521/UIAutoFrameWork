"""
    方法tab页内容
"""

img_fit_of_curve = ("xpath", "//img[@id='viewitems-components-method-list-associative-curve']")  # 方法页 - 曲线拟合图标

img_fit_of_curve_alert_choose = ("xpath", "//input[@id='viewitems-components-method-list-associative-curve-select']") # 选择处理类型
img_fit_of_curve_alert_confirm = ("xpath", "//span[@id='viewitems-components-method-list-associative-curve-sure']")  # 确定按钮
img_fit_of_curve_alert_cancel = ("xpath", "//span[@id='viewitems-components-method-list-associative-curve-canel']")  # 取消按钮

img_fit_of_curve_match_and_fit = ("xpath", "//span[contains(text(),'匹配加拟合')]")
img_fit_of_curve_step_fit = ("xpath", "//span[contains(text(),'分步拟合')]")

# 曲线拟合页面选择原始数据
# TODO
choose_first_raw_data = ("xpath", "//tbody/tr[1]/td[1]/div[1]/label[1]/span[1]/span[1]")  # 第一个原始数据

choose_raw_data_confirm = ("xpath", "//span[@id='projects-handle-addstandardcurve--select-sure']")
choose_raw_data_cancel = ("xpath", "//span[@id='projects-handle-addstandardcurve-select-canel']")

# 建立标曲页面
# 组分切换
component_change = ("xpath", "//input[@id='projects-handle-addstandardcurve-component-switch']")
level = ("xpath", "//input[@id='projects-handle-addstandardcurve-level']")
# 级别的下拉框
level_select = ("xpath", "//div[@x-placement='bottom-start']//ul[@class='el-scrollbar__view el-select-dropdown__list']/li")

create_curve_x = ("xpath", "//input[@id='projects-handle-addstandardcurve-x']")  # x值
create_curve_unit = ("xpath", "//input[@id='projects-handle-addstandardcurve-company']")  # 单位

create_curve_confirm = ("xpath", "//span[@id='projects-handle-addstandardcurve-sure']")  # 确定
create_curve_cancel = ("xpath", "//span[@id='projects-handle-addstandardcurve-canel']")  # 取消
