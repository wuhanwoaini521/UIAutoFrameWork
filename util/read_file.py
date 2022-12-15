import yaml
import json
from util.log_control import MyLogger

logger = MyLogger()


class Read_Yaml:
    """
        读取yaml文件的类
        """

    def __init__(self, file):
        self.file = file
        result = yaml.load(open(file, encoding='utf-8'), Loader=yaml.SafeLoader)

    def read_yaml(self):
        result = yaml.load(open(self.file, encoding='utf-8'), Loader=yaml.SafeLoader)
        dumps_result = json.dumps(result, indent=2)

        logger.info("-->> 读取文件开始 -->> %s " % self.file)

        logger.info("-->> 文件内容 -->> %s " % dumps_result)

        logger.info("-->> 读取文件结束  -->> ")
        return result


class Read_Excel:

    def __init__(self):
        pass


if __name__ == '__main__':
    read_yaml = Read_Yaml(r"C:\Users\Administrator\Desktop\UIAutoFrameWork\datas\login.yml")
    dic = read_yaml.read_yaml()
    print(dic["login_success"])
