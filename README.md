# 🚀 UIAutoFrameWork

> 基于 **Selenium + Pytest + Allure** 的**UI 自动化测试框架** 🧪
> 采用 **PO 模式**（Page Object）设计，封装了浏览器操作、日志、断言与数据库访问。

---

## ✨ 项目特色

- 🏗️ **PO 模式**：`page/` 页面对象 + `locators/` 元素定位分离，维护更清晰
- 🎯 **灵活定位**：`baseControl` 封装 8 种定位方式（id / name / xpath / css ...）
- 🌐 **驱动免下载**：基于 Selenium Manager 自动管理 chromedriver，也支持手动指定路径
- ⚙️ **环境变量配置**：所有配置支持 `UIAF_` 前缀环境变量覆盖，敏感信息不落代码
- 📝 **全量日志**：基于 loguru 的控制台 + 文件双输出，按大小轮转
- 📸 **失败留痕**：断言失败自动用 driver 截图并接入 allure 报告
- 🗄️ **数据支撑**：内置 MySQL 连接封装与 YAML 测试数据驱动，初始化数据不再明文暴露密码
- 🧵 **并行执行**：集成 pytest-xdist 支持用例并发

## 🛠️ 技术栈

| 技术 | 说明 |
|------|------|
| 🌐 Selenium | 浏览器自动化 |
| 🧪 pytest | 测试框架 |
| ✨ allure-pytest | 测试报告 |
| 🧵 pytest-xdist | 多进程并行 |
| 🔁 pytest-rerunfailures | 用例失败重跑 |
| 📝 loguru | 日志系统 |
| 🗄️ pymysql | MySQL 访问 |
| 🎵 PyYAML | 测试数据 |
| 🌐 Selenium Manager | 自动管理浏览器驱动 |

## 📦 安装

```bash
git clone https://github.com/wuhanwoaini521/UIAutoFrameWork.git
cd UIAutoFrameWork

# 使用 uv 安装依赖（自动创建 .venv）
uv sync
```

> 💡 **无需手动下载 chromedriver！** 驱动路径留空时由 Selenium Manager（Selenium >= 4.6 内置）自动匹配；也可通过 `UIAF_CHROMEDRIVER` 环境变量或 `settings.py` 指定本地驱动。

## 🚀 使用

### 配置环境

所有配置项都支持 `UIAF_` 前缀的环境变量覆盖 🔧，例如：

```bash
UIAF_WEB_TEST_BASE_URL=http://your-host python main.py
```

或直接编辑 `util/settings.py`：

```python
WEB_TEST_BASE_URL = "http://your-host"   # 被测系统地址
DRIVER_NAME = "chrome"                   # 浏览器类型
MYSQL_HOST = "..."                       # 数据库信息（密码建议走环境变量 🔐）
```

### 运行全部测试

```bash
# 运行测试
python -m pytest -s -q
# 或仅运行主流程
python main.py
# 跳过数据库初始化（被测库不可达时）
UIAF_SKIP_DB_INIT=1 python main.py
```

### 生成 Allure 报告

```bash
pytest --alluredir=outFiles/reports/allure-results
allure generate outFiles/reports/allure-results -o outFiles/reports/allure-report --clean
allure open outFiles/reports/allure-report
```

## 📁 项目结构

```
UIAutoFrameWork/
├── base/
│   └── baseControl.py        # 🔧 底层元素操作封装
├── datas/
│   ├── init.sql              # 🗄️ 初始化 SQL
│   ├── login.yml             # 🔐 登录测试数据
│   └── main_test.yml         # 🧪 主页测试数据
├── driver/                   # 🌐 chromedriver（已 gitignore）
├── locators/                 # 📌 元素定位（按模块分组）
├── page/                     # 📄 页面对象（PO 模式）
├── tests/                    # 🧪 测试用例（按模块分组）
├── util/
│   ├── assets.py             # ✅ 断言控制
│   ├── choose_driver.py      # 🌐 浏览器驱动选择
│   ├── log_control.py        # 📝 日志系统
│   ├── read_file.py          # 📖 YAML/文件读取
│   ├── settings.py           # ⚙️ 全局配置
│   └── sql_control.py        # 🗄️ 数据库访问
├── main.py                   # 🚀 入口（初始化数据 + 跑用例）
├── pyproject.toml            # uv 依赖管理
└── uv.lock                   # uv 锁定的依赖版本
```

## 🏗️ 如何新增一个测试

1. 📌 在 `locators/` 新建元素定位文件
2. 📄 在 `page/` 新建页面对象，继承 `BaseControl` 的操作
3. 🧪 在 `tests/` 新增测试方法，通过 fixture 获取 driver
4. 🚀 运行 `pytest` 即可

## 📄 License

MIT License © 2024 [wuhanwoaini521](https://github.com/wuhanwoaini521)
