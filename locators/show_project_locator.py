# 新建项目
create_project = ("xpath", "//span[text()='新建项目']")
backup_project = ("xpath", "//span[text()='项目备份']")
restore_project = ("xpath", "//span[text()='项目还原']")
load_project = ("xpath", "//span[text()='上传至典型项目']")
delete_project = ("xpath", "//span[text()='删除']")

# 名称列表
name_project = ("xpath", "//span[text()='%s']")  # 可以自己选项目名称填入

# 页面上tab
tab_sequence = ("xpath", "//span[text()='序 列']")
tab_injection = ("xpath", "//span[text()='进 样']")
tab_data = ("xpath", "//span[text()='原始数据']")
tab_method = ("xpath", "//span[text()='方 法']")
tab_curve = ("xpath", "//span[text()='曲 线']")
tab_resultGroup = ("xpath", "//span[text()='结果组']")
tab_result = ("xpath", "//span[text()='结 果']")

# 序 列tab
tab_sequence_lock = ("xpath", "//span[text()='锁定设置']")
tab_sequence_delete = ("xpath", "//span[text()='删除']")

# 进样tab
tab_injection_lock = ("xpath", "//span[text()='锁定设置']")
tab_injection_delete = ("xpath", "//span[text()='删除']")

# 原始数据tab
tab_data_sequence = ("xpath", "//span[text()='序列']")
tab_data_deal_with = ("xpath", "//span[text()='处理']")
tab_data_compare = ("xpath", "//span[text()='对比']")
tab_data_update_sample_type = ("xpath", "//span[text()='修改样品类型']")
tab_data_export = ("xpath", "//span[text()='导出']")
tab_data_lock = ("xpath", "//span[text()='锁定设置']")
tab_data_extract = ("xpath", "//span[text()='提取2D']")
tab_data_delete = ("xpath", "//span[text()='删除']")

# 方法tab
tab_method_upload = ("xpath", "//span[text()='上传至用户方法库']")
tab_method_sequence = ("xpath", "//span[text()='序列']")
tab_method_create_method = ("xpath", "//span[text()='新建方法']")
tab_method_export = ("xpath", "//span[text()='导出']")
tab_method_lock = ("xpath", "//span[text()='锁定设置']")
tab_method_delete = ("xpath", "//span[text()='删除']")

tab_method_create_method_instrument_method = ("xpath", "//li[text()='仪器方法']")
tab_method_create_method_report_method = ("xpath", "//li[text()='报告方法']")
tab_method_create_method_deal_with_method = ("xpath", "//li[text()='处理方法']")


## 方法列表页的名称
method_list_name = ("xpath", "//span[text()='%s']")
tab_method_list_name = ("id", "viewitems-components-method-list-method-name")  # 方法页列表所有名称


# 曲线tab
tab_curve_sequence = ("xpath", "//span[text()='序列']")
tab_curve_export = ("xpath", "//span[text()='导出']")
tab_curve_delete = ("xpath", "//span[text()='删除']")

# 结果组tab
tab_resultGroup_sequence = ("xpath", "//span[text()='序列']")
tab_resultGroup_lock = ("xpath", "//span[text()='锁定设置']")
tab_resultGroup_delete = ("xpath", "//span[text()='删除']")

# 结果tab
tab_result_sequence = ("xpath", "//span[text()='序列']")
tab_result_compare = ("xpath", "//span[text()='对比']")
tab_result_publish = ("xpath", "//span[text()='出版报告']")
tab_result_export = ("xpath", "//span[text()='导出']")
tab_result_lock = ("xpath", "//span[text()='锁定设置']")
tab_result_delete = ("xpath", "//span[text()='删除']")