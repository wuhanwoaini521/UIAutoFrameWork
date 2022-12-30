import pytest
from selenium import webdriver
from time import sleep
import os
import allure
from util.log_control import MyLogger
from util import settings

logger = MyLogger()


if __name__ == '__main__':
    # 清除数据操作
    logger.info("★★★★ 开始清除、初始化数据 ★★★★")
    sql = f"mysql -h{settings.MYSQL_HOST} -u{settings.MYSQL_USER} -p{settings.MYSQL_PASSWORD} --default-character-set=utf8 {settings.MYSQL_DB_NAME} < {settings.DB_INIT_PATH}"
    os.system(sql)
    logger.info("★★★★ 清除、初始化数据完成，开始执行用例 ★★★★")
    pytest.main(['-s', '-q', './tests/main_process/test_main.py::Test_main::test_raw_data', '--clean-alluredir', '--alluredir', 'outFiles/reports/allure-results'])
    # logger.info("★★★★★ 生成报告 ★★★★★")
    # os.system(r"allure generate outFiles/reports/allure-results -o outFiles/reports/allure-result --clean")
