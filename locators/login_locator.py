# 登录页面
username_text = ("name", "username")
password_text = ("name", "password")
login_button = ("xpath", "//span[text()='登录 ']")

# 弹窗
error_alert = ("xpath", "//p[@class='el-message__content']")


# 权限选择页面
authority_choose = ("xpath", "//div[text()='请选择角色']")
system_administrator = ("xpath", "//div[text()='系统管理员']")
safe_administrator = ("xpath", "//div[text()='系统管理员']")
aduit_administrator = ("xpath", "//div[text()='系统管理员']")
ordinary_user = ("xpath", "//div[text()='系统管理员']")
custom_role = ("xpath", "//div[text()='%s']")  # 可以自定义填入角色

