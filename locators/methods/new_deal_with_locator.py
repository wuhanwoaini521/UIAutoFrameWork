# 积分
first_order_integral = ("id", "viewitems-processingmethod-integral-first-order")  # 一阶积分
second_order_integral = ("id", "viewitems-processingmethod-integral-two-order")  # 二阶积分
sectional_integral = ("id", "viewitems-processingmethod-integral-subsection-order")  # 分段积分
global_integral = ("id", "viewitems-processingmethod-integral-overall-order")  # 全局积分
peak_width = ("id", "viewitems-processingmethod-accumulate-all-order-peak-width")  # 峰宽
slope = ("id", "viewitems-processingmethod-accumulate-all-order-slope")  # 斜率

# 添加积分事件、分段积分参数
add_integral_event = ("xpath", "//div[@class='accumulate']//img[@id='viewitems-processingmethod-accumulate-subsection"
                               "-order-none']")  # 添加积分事件

add_second_order_integralevent = ("xpath", "//div[@class='accumulate mag']//img["
                                           "@id='viewitems-processingmethod-accumulate-subsection-order-none']")  # 添加分段积分参数

# 组分
open_constituent = ("xpath", "//li[contains(text(),'组分')]")

# 系统适应性
open_system_adaptation = ("id", "viewitems-processingmethod-openpda")

# PDA
open_pda = ("id", "viewitems-processingmethod-openpda")

# 保存
new_method_save = ("id", "viewitems-processingmethod-save")

###################################################################

# 保存处理方法弹窗
alert_save_deal_with_method = ("xpath", "//div[contains(text(),'保存处理方法')]")

alert_save_deal_with_method_confirm_button = ("xpath", "//section[@class='app-main']//span[text()='确定']")
alert_save_deal_with_method_cancel_button = ("xpath", "//section[@class='app-main']//span[text()='取消']")
alert_save_deal_with_method_input = ("xpath", "//section[@class='app-main']//div[@class='formlist']//input")

