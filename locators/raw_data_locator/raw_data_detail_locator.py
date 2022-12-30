choose_deal_with_method = ("xpath", "//input[@id='channelInfo-select-processing-method']")  # 选择处理办法下拉框
deal_with_button = ("xpath", "//span[contains(text(),'处 理')]")
edit_deal_with_method_button = ("xpath", "//div[@id='channelInfo-edit-processing-method']")  # 编辑处理办法
new_deal_with_method_button = ("xpath", "//span[contains(text(),'新建处理方法')]")

choose_deal_with = ("xpath", "//span[contains(text(),'%s')]")  # 根据名称选择处理办法

# 新建处理方法
show_deal_with_method_button = ("xpath", "//span[contains(text(),'显示处理方法')]")
show_system_adaptability_button = ("xpath", "//span[contains(text(),'开启系统适应性')]")
automatic_component_button = ("xpath", "//span[contains(text(),'自动组分')]")
pretreatment_button = ("xpath", "//span[contains(text(),'预处理')]")
save_button = ("xpath", "//span[@id='viewitemscom-method-save']")  # 保存按钮
# 保存方法和结果弹窗
save_method_result_name = ("xpath", "//input[@id='views-viewitemscom-method-save-method']")
save_method_result_confirm = ("xpath", "//span[@id='views-viewitemscom-method-save-method-sure']")
save_method_result_type = ("xpath", "//input[@id='views-viewitemscom-method-save-method-type']")
choose_type_name = ("xpath", "//span[text()='%s']")  # 选择保存类型

# 显示处理方法
constituent_tab = ("xpath", "//li[@id='viewitemscom-method-composition1']")  # 组分tab

integral_first_order = ("xpath", "//label[@id='viewitemscom-components-integral-first-order']")  # 一阶积分
integral_two_order = ("xpath", "//label[@id='viewitemscom-components-integral-two-order']")  # 二阶积分
integral_subsection_order = ("xpath", "//label[@id='viewitemscom-components-integral-subsection-order']")  # 分段积分
integral_overall_order = ("xpath", "//label[@id='viewitemscom-components-integral-overall-order']")  # 全局积分

# 全局积分
order_peak_width = ("css", "#viewitemscom-components-accumulate-all-order-peak-width")  # 全局积分-峰宽
order_slope = ("css", "#viewitemscom-components-accumulate-all-order-slope")  # 全局积分-斜率

# 分段积分
# subsection_order_none = ("xpath", "//div[@class='accumulate mag']//img[@id='viewitemscom-components-accumulate-subsection-order-none']")  # 分段积分-添加参数按钮
subsection_order_none = ("css", "#viewitemscom-components-accumulate-subsection-order-none")  # 分段积分-添加参数按钮
subsection_order_start_time = ("css", "#viewitemscom-components-accumulate-subsection-order-start-time")  # 分段积分-开始时间
subsection_order_end_time = ("css", "#viewitemscom-components-accumulate-subsection-order-end-time")  # 分段积分-结束时间
subsection_order_peak_width = ("css", "#viewitemscom-components-accumulate-subsection-order-peak-width")  # 分段积分-峰宽
subsection_order_slope = ("css", "#viewitemscom-components-accumulate-subsection-order-slope")  # 分段积分-斜率

# 积分事件
# event_subsection_order_none = ("xpath", "//div[@class='accumulate']//img[@id='viewitemscom-components-accumulate-subsection-order-none']")  # 分段积分-添加参数按钮
event_subsection_order_none = ("css", "#viewitemscom-components-accumulate-subsection-order-none")

event_start_time = ("xpath", "//input[@id='viewitemscom-components-accumulate-subsection-event-start-time']")  # 积分事件-开始时间
event_end_time = ("xpath", "//input[@id='viewitemscom-components-accumulate-subsection-event-end-time']")  # 积分事件-结束时间
order_event_type = ("xpath", "//input[@id='viewitemscom-components-accumulate-subsection-order-event-type']")  # 积分事件-事件类型
order_event_value = ("xpath", "//input[@id='viewitemscom-components-accumulate-subsection-order-event-value']")  # 积分事件-事件参数


# 组分tab
# 添加组分参数
component_order_none = ("css", "#viewitemscom-components-accumulate-subsection-order-none")
# 组分名称
accumulate_component_name = ("xpath", "//input[@id='viewitemscom-components-accumulate-component-name']")
# 匹配类型
accumulate_match_type = ("xpath", "//input[@id='viewitemscom-components-accumulate-match-type']")
# 匹配值
accumulate_match_value = ("xpath", "//input[@id='viewitemscom-components-accumulate-match-value']")
# 匹配窗口
accumulate_match_window = ("xpath", "//input[@id='viewitemscom-components-accumulate-match-window']")
# 拟合类型
accumulate_fit_type = ("xpath", "//input[@id='viewitemscom-components-accumulate-fit-type']")
# x轴
components_accumulate_x = ("xpath", "//input[@id='viewitemscom-components-accumulate-x']")
# y轴
components_accumulate_y = ("xpath", "//input[@id='viewitemscom-components-accumulate-y']")



