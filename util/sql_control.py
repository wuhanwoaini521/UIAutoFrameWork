import datetime
import os
import subprocess
import sys

import pymysql
import traceback
from util.log_control import MyLogger
from util import settings

logger = MyLogger()


class Sql_Control:

    def __init__(self):
        self.host = settings.MYSQL_HOST
        self.username = settings.MYSQL_USER
        self.password = settings.MYSQL_PASSWORD
        self.db = settings.MYSQL_DB_NAME
        self.port = settings.MYSQL_PORT

    def connect(self):
        """
        创建数据库连接
        :return:
        """
        try:
            self.conn = pymysql.connect(host=self.host,
                                        port=self.port,
                                        user=self.username,
                                        password=self.password,
                                        db=self.db)

            logger.info("☆☆☆数据库连接成功！☆☆☆")
        except Exception:
            logger.error("数据库连接失败！错误原因：{}".format(traceback.format_exc()))
        else:
            self.cursor = self.conn.cursor()

    def close(self):
        """
        关闭数据库连接
        :return:
        """
        logger.info("☆☆☆数据库连接关闭！☆☆☆")
        self.cursor.close()
        self.conn.close()

    def commit(self):
        """
        提交事务
        :return:
        """
        logger.info("★★★数据提交！★★★")
        self.conn.commit()

    def rollback(self):
        """
        回滚事务
        :return:
        """
        logger.info("★★★数据回滚！★★★")
        self.conn.rollback()

    def __execute(self, sql, params=()):
        try:
            self.connect()
            self.cursor.execute(sql, params)
        except Exception:
            logger.error("sql执行失败！报错原因：{}".format(traceback.format_exc()))
        else:
            return True

    def get_one(self, sql, params=()):
        """
        获取单条数据
        :param sql:
        :param params:
        :return:
        """
        result = None
        try:
            # self.connect()
            # self.cursor.execute(sql, params)
            self.__execute(sql, params)
            result = self.cursor.fetchone()
        except Exception as e:
            logger.error("数据获取失败！报错原因：{}".format(traceback.format_exc()))
        finally:
            self.close()
        return result

    def get_all(self, sql, params=()):
        """
        获取多条数据
        :param sql:
        :param params:
        :return:
        """
        list_data = ()
        try:
            # self.connect()
            # self.cursor.execute(sql, params)
            self.__execute(sql, params)
            list_data = self.cursor.fetchall()
        except Exception as e:
            logger.error("数据获取失败！报错原因：{}".format(traceback.format_exc()))
        finally:
            self.close()
        return list_data

    def delete_one(self, sql, params=()):
        """
        删除一条数据
        :param sql:
        :param params:
        :return:
        """
        result = None
        try:
            # self.connect()
            # self.cursor.execute(sql, params)
            self.__execute(sql, params)
            result = self.cursor.fetchone()

        except Exception as e:
            logger.error("删除数据失败！报错原因：{}".format(traceback.format_exc()))
            self.rollback()
        else:
            self.commit()
        finally:
            self.close()
        return result

    def update_one(self, sql, params=()):
        """
        修改数据
        :param sql:
        :param params:
        :return:
        """
        result = None
        try:
            # self.connect()
            # self.cursor.execute(sql, params)
            self.__execute(sql, params)
            result = self.cursor.fetchone()
        except Exception as e:
            logger.error("修改数据失败！报错原因：{}".format(traceback.format_exc()))
            self.rollback()
        else:
            self.commit()
        finally:
            self.close()
        return result

if __name__ == '__main__':
    host = "192.168.1.180"
    username = "cims"
    password = "cims123$%"
    db = "cims_db"
    my_db = Sql_Control()

    # 获取单个
    sql = 'SELECT * FROM `users`;'
    result = my_db.get_one(sql)
    print("result:{}\n".format(result))
    #
    # print("_"*50)
    #
    # # 获取多个
    # sql = "Select * from `users`;"
    # result = my_db.get_all(sql)
    # # print("result:{}".format(result))
    #
    # for i in result:
    #     print(i)
    # my_db.backUp_db()