import os
import sys

current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
data_path = current_path + os.sep + "datas" + os.sep

# 登录用例
login_path = data_path + "login.yml"


if __name__ == '__main__':
    print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

    print(login_path)