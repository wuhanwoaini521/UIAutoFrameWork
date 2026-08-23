"""pytest 共享 fixture 与异常截图钩子 🧩."""

import pytest
from util.choose_driver import Choose_Driver
from util import settings
import allure
from allure_commons.types import AttachmentType
from base.baseControl import BaseControl
from util.log_control import MyLogger

logger = MyLogger()


@pytest.fixture(scope='function')
def driver():
    """统一启动浏览器。"""
    logger.info("☆☆☆☆☆启动公用driver☆☆☆☆☆")
    driver = Choose_Driver(settings.DRIVER_NAME).choose_driver()
    baseControl = BaseControl(driver)
    logger.info("☆☆☆☆☆打开浏览器 ☆☆☆☆☆")
    baseControl.open_url()  # 打开浏览器
    yield driver
    # 关闭driver（quit 会同时关闭窗口并结束驱动进程，无需先 close）
    logger.info("☆☆☆☆☆关闭driver☆☆☆☆☆")
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """用例失败时，用 driver 截取当前页面附加到 Allure 报告。

    相比旧的 ImageGrab 全屏抓屏，driver 截图只包含被测页面，
    更精准且在无显示器的 CI 环境下也能工作 📸
    """
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        current_driver = getattr(item, "funcargs", {}).get("driver")
        if current_driver is not None:
            try:
                allure.attach(
                    current_driver.get_screenshot_as_png(),
                    name="异常截图",
                    attachment_type=AttachmentType.PNG,
                )
            except Exception:  # noqa: BLE001 - 截图失败不应污染原始用例结果
                logger.warning("⚠️ 异常截图捕获失败")
