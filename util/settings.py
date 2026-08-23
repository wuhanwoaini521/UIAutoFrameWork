"""全局配置 ⚙️.

所有配置项均支持通过 ``UIAF_`` 前缀的环境变量覆盖，
例如：``UIAF_WEB_TEST_BASE_URL=http://localhost:7777 python main.py``
敏感信息（数据库密码等）推荐走环境变量，不要写死在代码里 🔐
"""

import os


def _env(key: str, default: str = "") -> str:
    """读取 UIAF_ 前缀环境变量，未设置时返回默认值。"""
    return os.environ.get(f"UIAF_{key}", default)


# env config
ENV = _env("ENV", "test")

# test url test config
WEB_TEST_BASE_URL = _env("WEB_TEST_BASE_URL", "http://39.107.225.40:7777")
TIMES = int(_env("TIMES", "60"))
POLL_FREQUENCY = float(_env("POLL_FREQUENCY", "0.5"))

# webdriver：留空则交给 Selenium Manager 自动管理驱动（Selenium >= 4.6）
DRIVER_NAME = _env("DRIVER_NAME", "chrome")

# webdriver_path：跨平台路径；找不到文件时会自动回退到 Selenium Manager
CHROMEDRIVER = _env("CHROMEDRIVER", "")
FIREFOXDRIVER = _env("FIREFOXDRIVER", "")

# mysql 🔐 敏感信息建议通过环境变量注入
MYSQL_HOST = _env("MYSQL_HOST", "39.107.225.40")
MYSQL_USER = _env("MYSQL_USER", "cims")
MYSQL_PASSWORD = _env("MYSQL_PASSWORD", "")
MYSQL_PORT = int(_env("MYSQL_PORT", "3306"))
MYSQL_DB_NAME = _env("MYSQL_DB_NAME", "cims_db")
MYSQL_CHARSET = _env("MYSQL_CHARSET", "utf8")
DB_INIT_PATH = _env("DB_INIT_PATH", "datas/init.sql")

# 设为 1 时 main.py 跳过数据库初始化（被测库不可达也能跑用例）
SKIP_DB_INIT = _env("SKIP_DB_INIT", "") == "1"

# mongodb
MONGODB_HOST = _env("MONGODB_HOST", "")
MONGODB_USER = _env("MONGODB_USER", "")
MONGODB_PASSWORD = _env("MONGODB_PASSWORD", "")
MONGODB_PORT = _env("MONGODB_PORT", "")

# redis
REDIS_HOST = _env("REDIS_HOST", "")
