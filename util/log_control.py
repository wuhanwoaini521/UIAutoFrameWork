"""日志控制器 📝.

基于 loguru，支持控制台彩色输出 + 文件按大小轮转（rotation）。
"""

import datetime
import os
import sys
from pathlib import Path

from loguru import logger

ROOT_PATH = Path(__file__).resolve().parent.parent

today = datetime.datetime.now().strftime("%Y_%m_%d")
log_dir = ROOT_PATH / "outFiles" / "logs"
log_dir.mkdir(parents=True, exist_ok=True)
log_path = log_dir / f"log_{today}.log"


class MyLogger:
    """loguru 日志封装，提供 info/debug/warning/error 便捷方法。"""

    def __init__(self, my_log_path: Path = log_path):
        self.logger = logger
        # 清空所有设置，避免重复注册 handler
        self.logger.remove()
        # 控制台输出
        self.logger.add(
            sys.stdout,
            colorize=True,
            format="<green>{time:YYYYMMDD HH:mm:ss}</green> | "
                   "{process.name} | "
                   "{thread.name} | "
                   "<cyan>{module}</cyan>.<cyan>{function}</cyan>"
                   ":<cyan>{line}</cyan> | "
                   "<level>{level}</level>: "
                   "<level>{message}</level>",
        )
        # 文件输出（按 10MB 轮转）
        self.logger.add(
            str(my_log_path),
            level="DEBUG",
            format='{time:YYYYMMDD HH:mm:ss} - '
                   "{process.name} | "
                   "{thread.name} | "
                   '{module}.{function}:{line} - {level} - {message}',
            rotation="10 MB",
        )

    def get_logger(self):
        return self.logger

    def info(self, msg):
        return self.logger.info(">>>>>> %s" % msg)

    def debug(self, msg):
        return self.logger.debug(">>>>>> %s" % msg)

    def warning(self, msg):
        return self.logger.warning(">>>>>> %s" % msg)

    def error(self, msg):
        return self.logger.error("★★★★★★★ %s ★★★★★★" % msg)


my_logger = MyLogger().get_logger()


if __name__ == "__main__":
    logger.info("日志路径: %s" % log_path)
