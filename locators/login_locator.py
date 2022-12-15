# 登录页面
username_text = ("name", "username")
password_text = ("name", "password")
login_button = ("xpath", "//span[text()='登录 ']")

# 弹窗
error_alert = ("xpath", "//p[@class='el-message__content']")
public_text = ("xpath", "//p[contains(text(),'%s')]")
redmin_confirm = ("xpath", "//div[@aria-label='提醒']//span[contains(text(),'确定')]")


# 权限选择页面
authority_choose = ("xpath", "//div[text()='请选择角色']")
system_administrator = ("xpath", "//div[text()='系统管理员']")
safe_administrator = ("xpath", "//div[text()='安全管理员']")
aduit_administrator = ("xpath", "//div[text()='审计管理员']")
ordinary_user = ("xpath", "//div[text()='普通用户']")
custom_role = ("xpath", "//div[text()='%s']")  # 可以自定义填入角色

# 页面左上侧抽屉开关
drawer_switch = ("xpath", "//img[@class='image-logo']")

# 页面左侧导航栏
menu_navigation = ("id", "layout-components-sidebar")

## 项目管理
manage_project = ("xpath", "//div[@id='layout-components-sidebar10']//span[text()='项目管理']")
show_project = ("xpath", "//div[@id='layout-components-sidebar10']//span[text()='查看项目']")
compare_project = ("xpath", "//div[@id='layout-components-sidebar10']//span[text()='项目对比']")

## 系统管理
system_manage = ("xpath", "//div[@id='layout-components-sidebar11']//span[text()='系统管理']")
role_manage = ("xpath", "//div[@id='layout-components-sidebar11']//span[text()='角色管理']")
organizaton_manage = ("xpath", "//div[@id='layout-components-sidebar11']//span[text()='组织管理']")
user_manage = ("xpath", "//div[@id='layout-components-sidebar11']//span[text()='用户管理']")
safe_center = ("xpath", "//div[@id='layout-components-sidebar11']//span[text()='安全中心']")
audit_manage = ("xpath", "//div[@id='layout-components-sidebar11']//span[text()='审计管理']")

## 设备管理
equipment_manage = ("xpath", "//div[@id='layout-components-sidebar11']//span[text()='设备管理']")
workstation = ("xpath", "//div[@id='layout-components-sidebar12']//span[text()='工作站']")
instru_analysis = ("xpath", "//div[@id='layout-components-sidebar12']//span[text()='仪器分析']")
instru_system = ("xpath", "//div[@id='layout-components-sidebar12']//span[text()='仪器系统']")

## 知识库
knowledge_base = ("xpath", "//div[@id='layout-components-sidebar13']//span[text()='知识库']")
article_list = ("xpath", "//div[@id='layout-components-sidebar13']//span[text()='文章列表']")
collection = ("xpath", "//div[@id='layout-components-sidebar13']//span[text()='我的收藏']")

## 方法库
method_library = ("xpath", "//div[@id='layout-components-sidebar12']//span[text()='方法库']")
standard_method_library = ("xpath", "//div[@id='layout-components-sidebar12']//span[text()='标准方法库']")
user_method_library = ("xpath", "//div[@id='layout-components-sidebar12']//span[text()='用户方法库']")
typical_project = ("xpath", "//div[@id='layout-components-sidebar12']//span[text()='典型项目']")
spectral_library = ("xpath", "//div[@id='layout-components-sidebar12']//span[text()='光谱库']")
