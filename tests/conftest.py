import pytest
from util.choose_driver import Choose_Driver
from util import settings


@pytest.fixture(scope='session')
def driver():
    # 打开driver
    driver = Choose_Driver(settings.DRIVER_NAME).choose_driver()
    yield driver
    #关闭driver
    driver.close()
