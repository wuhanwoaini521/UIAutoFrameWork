"""文件读取工具 📖.

支持读取 YAML 配置文件，并解析为字典。
"""

import json

import yaml

from util.log_control import MyLogger

logger = MyLogger()


class Read_Yaml:
    """读取 YAML 文件并转换为 Python 对象。"""

    def __init__(self, file):
        self.file = file

    def read_yaml(self):
        """读取 YAML 文件内容并返回解析结果。"""
        logger.info("-->> 读取文件开始 -->> %s " % self.file)
        with open(self.file, encoding="utf-8") as f:
            result = yaml.load(f, Loader=yaml.SafeLoader)
        logger.info("-->> 文件内容 -->> %s " % json.dumps(result, indent=2, ensure_ascii=False))
        logger.info("-->> 读取文件结束  -->> ")
        return result


if __name__ == "__main__":
    import os

    demo_file = os.path.join(os.path.dirname(__file__), "..", "datas", "login.yml")
    read_yaml = Read_Yaml(demo_file)
    data = read_yaml.read_yaml()
    print(data)
