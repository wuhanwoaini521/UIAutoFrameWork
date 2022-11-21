import pytest
from util.choose_driver import Choose_Driver
from util import settings
import allure
from allure_commons.types import AttachmentType
from PIL import ImageGrab
from io import BytesIO
from base.baseControl import BaseControl


@pytest.fixture(scope='function')
def driver():
    """
    统一启动
    :return:
    """
    # 打开driver
    driver = Choose_Driver(settings.DRIVER_NAME).choose_driver()
    baseControl = BaseControl(driver)
    baseControl.open_url()  # 打开浏览器
    yield driver
    #关闭driver
    driver.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    """
    异常捕获截图
    :return:
    """
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        with BytesIO() as output:
            img = ImageGrab.grab()
            img.save(output, 'PNG')
            data = output.getvalue()
        allure.attach(data, name="异常截图", attachment_type=AttachmentType.PNG)
