"""测试入口 🚀.

流程：
1. 通过 pymysql 执行 ``datas/init.sql`` 初始化测试数据（密码不落命令行）；
2. 调用 pytest 执行用例并生成 allure 结果。

用法：
    python main.py
    UIAF_SKIP_DB_INIT=1 python main.py   # 跳过数据库初始化
"""

import os
import sys

import pytest

from util import settings
from util.log_control import MyLogger
from util.sql_control import Sql_Control

logger = MyLogger()


def init_db_data() -> None:
    """使用 pymysql 执行初始化 SQL，替代旧的 mysql 命令行拼接。

    旧实现把密码明文拼进 shell 命令（进程列表可见，且有注入风险），
    现在改为参数化连接 + 逐条执行。
    """
    sql_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), settings.DB_INIT_PATH
    )
    with open(sql_path, encoding="utf-8") as f:
        statements = [
            line.strip().rstrip(";")
            for line in f
            if line.strip() and not line.strip().startswith("--")
        ]

    db = Sql_Control()
    db.connect()
    try:
        for statement in statements:
            db.cursor.execute(statement)
        db.commit()
        logger.info("★★★★ 清除、初始化数据完成 ★★★★")
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    if settings.SKIP_DB_INIT:
        logger.info("⏭️ SKIP_DB_INIT=1，跳过数据库初始化")
    else:
        logger.info("★★★★ 开始清除、初始化数据 ★★★★")
        try:
            init_db_data()
        except Exception as exc:  # noqa: BLE001 - 数据库不可达时给出明确提示
            logger.error(f"❌ 数据库初始化失败：{exc}")
            logger.error("可设置环境变量 UIAF_SKIP_DB_INIT=1 跳过该步骤")
            sys.exit(1)

    logger.info("★★★★ 开始执行用例 ★★★★")
    pytest.main([
        "-s", "-q",
        "./tests/main_process/test_main.py::Test_main::test_raw_data",
        "--clean-alluredir",
        "--alluredir", "outFiles/reports/allure-results",
    ])
