import yaml
import json


class Read_Yaml:
    """
        读取yaml文件的类
        """

    def __init__(self, file):
        self.file = file
        result = yaml.load(open(file, encoding='utf-8'), Loader=yaml.SafeLoader)
        print(json.dumps(result, indent=2))

    def read_yaml(self):
        return yaml.load(open(self.file, encoding='utf-8'), Loader=yaml.SafeLoader)


class Read_Excel:

    def __init__(self):
        pass


if __name__ == '__main__':
    read_yaml = Read_Yaml(r"C:\Users\Administrator\Desktop\UIAutoFrameWork\datas\login.yml")
    dic = read_yaml.read_yaml()
    print(dic["login_success"])
