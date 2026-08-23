"""浏览器驱动选择器 🌐.

根据配置的浏览器名称返回对应的 Selenium WebDriver 实例。

优先使用 ``settings.CHROMEDRIVER`` / ``settings.FIREFOXDRIVER`` 指定的本地驱动；
路径为空或文件不存在时，自动回退到 **Selenium Manager**（Selenium >= 4.6 内置），
无需再手动下载 chromedriver 🎉
"""

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService

from util import settings


def _resolve_service(driver_path: str, service_cls):
    """驱动路径有效则返回 Service，否则返回 None（交给 Selenium Manager）。"""
    if driver_path and Path(driver_path).is_file():
        return service_cls(driver_path)
    return None


class Choose_Driver:
    """根据名称选择并创建浏览器驱动。"""

    def __init__(self, driver_name: str):
        self.driver_name = driver_name.lower()
        self.driver = None

    def choose_driver(self):
        """选择并返回对应浏览器的 WebDriver 实例。"""
        if self.driver_name == "chrome":
            service = _resolve_service(settings.CHROMEDRIVER, Service)
            self.driver = webdriver.Chrome(service=service)
        elif self.driver_name == "firefox":
            service = _resolve_service(settings.FIREFOXDRIVER, FirefoxService)
            self.driver = webdriver.Firefox(service=service)
        else:
            raise ValueError(f"不支持的浏览器类型: {self.driver_name}")
        return self.driver
