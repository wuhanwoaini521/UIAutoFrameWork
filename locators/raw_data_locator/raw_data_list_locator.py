# 处理方式弹窗
choose_deal_with_way = ("xpath", "//input[@id='viewitems-components-basicdata-handle-select']")  # 选择处理方式

deal_with_only = ("xpath",
                  "//li[@id='viewitems-components-basicdata-handle-select-processonly']")  # 仅处理
process_and_quantify = ("xpath",
                        "//li[@id='viewitems-components-basicdata-handle-select-ration']")  # 处理并定量

cancel = ("xpath", "//span[@id='viewitems-components-basicdata-handle-canel']")  # 取消按钮
confirm = ("xpath", "//span[@id='viewitems-components-basicdata-handle-sure']")  # 确定按钮

# 查看积分结果弹窗
view_the_integral_result = ("xpath", "//div[contains(text(),'查看积分结果')]")
view_the_integral_result_save = ("xpath", "//div[contains(text(),'查看积分结果')]/parent::div/following-sibling::div["
                                          "@class='el-dialog__footer']//span[text()='保存']")
# 模糊匹配数据
view_the_integral_result_datas = ("xpath", "//span[contains(text(),'%s')]")
