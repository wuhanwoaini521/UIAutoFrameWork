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

integral_event_start_time = ("xpath", "//input[@id='viewitems-processingmethod-accumulate-subsection-event-start-time']")  # 开始时间
integral_event_end_time = ("xpath", "//input[@id='viewitems-processingmethod-accumulate-subsection-event-end-time']")  # 结束时间
integral_event_type = ("xpath", "//input[@id='viewitems-processingmethod-accumulate-subsection-order-event-type']")  # 事件类型
integral_event_param = ("xpath", "//input[@id='//input[@id='viewitems-processingmethod-accumulate-subsection-order-event-value']")  # 事件参数
integral_event_type_section = ("xpath", "//span[text()='%s']")

add_second_order_integralevent = ("xpath", "//div[@class='accumulate mag']//img["
                                           "@id='viewitems-processingmethod-accumulate-subsection-order-none']")  # 添加分段积分参数
subsection_order_start_time = ("xpath", "//input[@id='viewitems-processingmethod-accumulate-subsection-order-start-time']")  # 分段积分-开始时间
subsection_order_end_time = ("xpath", "//input[@id='viewitems-processingmethod-accumulate-subsection-order-end-time']")  # 分段积分-结束时间
subsection_order_peak_width = ("xpath", "//input[@id='viewitems-processingmethod-accumulate-subsection-order-peak-width']")  # 分段积分-峰宽
subsection_order_slope = ("xpath", "//input[@id='viewitems-processingmethod-accumulate-subsection-order-slope']")  # 分段积分-斜率



# 组分
open_constituent = ("xpath", "//li[contains(text(),'组分')]")
open_constituent_add_button = ("xpath", "//div[@class='accumulate mag']//img[@id='viewitems-processingmethod-accumulate-subsection-order-none']")  # 添加组分参数按钮
open_constituent_name = ("xpath", "//input[@id='viewitems-components-accumulate-component-name']")  # 组分名称
open_constituent_type = ("xpath", "//input[@id='viewitems-components-accumulate-match-type']")  # 匹配类型
open_constituent_param = ("xpath", "//input[@id='viewitems-components-accumulate-match-value']")  # 匹配值
open_constituent_time = ("xpath", "//input[@id='viewitems-components-accumulate-match-window']")  # 匹配窗口
open_constituent_fitting_type = ("xpath", "//input[@id='viewitems-components-accumulate-fit-type']")  # 拟合类型
open_constituent_x = ("xpath", "//input[@id='viewitems-components-accumulate-x']")  # X轴
open_constituent_y = ("xpath", "//input[@id='viewitems-components-accumulate-y']")  # Y轴
open_constituent_input = ("xpath", "//span[contains(text(),'%s')]")  # 下拉框自定义选择

# 系统适应性
open_system_adaptation = ("id", "viewitems-processingmethod-openpda")
close_system_adaptation = ("id", "//span[@id='viewitems-processingmethod-turn-system-adaptability-close']")
open_system_adaptation_empty_volume_time = ("xpath", "//input[@id='viewitems-components-suitparams-empty-volume-time']")  # 空体积时间
open_system_adaptation_suitparams_column_length = ("xpath", "//input[@id='viewitems-components-suitparams-column-length']")  # 色谱柱长度
open_system_adaptation_baseline_noise_max = ("xpath", "//input[@id='viewitems-components-baseline-noise-max']")  # 最大允许噪音
open_system_adaptation_baseline_drift_max = ("xpath", "//input[@id='viewitems-components-baseline-drift-max']")  # 最大允许漂移
open_system_adaptation_baseline_running_time = ("xpath", "//input[@id='viewitems-components-baseline-running-time']")  # 平均运行时间
open_system_adaptation_baseline_start_time = ("xpath", "//input[@id='viewitems-components-baseline-start-time']")  # 基线开始时间
open_system_adaptation_baseline_end_time = ("xpath", "//input[@id='viewitems-components-baseline-end-time']")  # 基线结束时间
open_system_adaptation_computer_baseline_start_time = ("xpath", "//input[@id='viewitems-components-computer-baseline-start-time']")  # 计算检测器噪音和漂移基线开始时间
open_system_adaptation_computer_baseline_end_time = ("xpath", "//input[@id='viewitems-components-computer-baseline-end-time']")  # 计算检测器噪音和漂移基线结束时间
open_system_adaptation_pda_slice_width = ("xpath", "//input[@id='viewitems-components-pda-slice-width']")  # 切片宽度

# PDA
open_pda = ("id", "viewitems-processingmethod-openpda")
close_pda = ("xpath", "//span[@id='viewitems-processingmethod-closepda']")
open_pda_wavelength = ("xpath", "//input[@id='viewitems-components-pda-wavelength']")  # 波长
open_pda_wavelength_start = ("xpath", "//input[@id='viewitems-components-pda-wavelength-range-start-point']")  # 波长范围开始点
open_pda_wavelength_end = ("xpath", "//input[@id='viewitems-components-pda-wavelength-range-end-point']")  # 波长范围结束点
open_pda_spectral_library = ("xpath", "//input[@id='viewitems-components-pda-spectral-library']")  # 光谱库

open_pda_spectral_library_name = ("xpath", "//span[text()='%s']")  # 光谱库名称


# 保存
new_method_save = ("id", "viewitems-processingmethod-save")

###################################################################

# 保存处理方法弹窗
alert_save_deal_with_method = ("xpath", "//div[contains(text(),'保存处理方法')]")

alert_save_deal_with_method_confirm_button = ("xpath", "//section[@class='app-main']//span[text()='确定']")
alert_save_deal_with_method_cancel_button = ("xpath", "//section[@class='app-main']//span[text()='取消']")
alert_save_deal_with_method_input = ("xpath", "//section[@class='app-main']//div[@class='formlist']//input")

