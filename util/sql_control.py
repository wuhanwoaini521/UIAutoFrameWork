"""数据库操作控制器 🗄️.

基于 pymysql 封装常用 MySQL 操作：连接、查询、增删改、事务等。
"""

import traceback

import pymysql

from util import settings
from util.log_control import MyLogger

logger = MyLogger()


class Sql_Control:
    """MySQL 数据库访问封装。"""

    def __init__(self):
        self.host = settings.MYSQL_HOST
        self.username = settings.MYSQL_USER
        self.password = settings.MYSQL_PASSWORD
        self.db = settings.MYSQL_DB_NAME
        self.port = settings.MYSQL_PORT
        self.conn = None
        self.cursor = None

    def connect(self):
        """创建数据库连接。"""
        try:
            self.conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.username,
                password=self.password,
                db=self.db,
                charset=settings.MYSQL_CHARSET,
            )
            logger.info("☆☆☆数据库连接成功！☆☆☆")
            self.cursor = self.conn.cursor()
        except Exception:
            logger.error("数据库连接失败！错误原因：{}".format(traceback.format_exc()))
            raise

    def close(self):
        """关闭数据库连接。"""
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
                logger.info("☆☆☆数据库连接关闭！☆☆☆")
        except Exception:
            logger.error("关闭连接失败：{}".format(traceback.format_exc()))

    def commit(self):
        """提交事务。"""
        logger.info("★★★数据提交！★★★")
        self.conn.commit()

    def rollback(self):
        """回滚事务。"""
        logger.info("★★★数据回滚！★★★")
        self.conn.rollback()

    def _execute(self, sql, params=()):
        """执行 SQL 并返回执行状态 True/False。"""
        try:
            self.connect()
            self.cursor.execute(sql, params)
            return True
        except Exception:
            logger.error("sql执行失败！报错原因：{}".format(traceback.format_exc()))
            return False

    def get_one(self, sql, params=()):
        """获取单条数据。"""
        result = None
        try:
            if self._execute(sql, params):
                result = self.cursor.fetchone()
            return result
        except Exception:
            logger.error("数据获取失败！报错原因：{}".format(traceback.format_exc()))
            return None
        finally:
            self.close()

    def get_all(self, sql, params=()):
        """获取多条数据。"""
        list_data = ()
        try:
            if self._execute(sql, params):
                list_data = self.cursor.fetchall()
            return list_data
        except Exception:
            logger.error("数据获取失败！报错原因：{}".format(traceback.format_exc()))
            return ()
        finally:
            self.close()

    def delete_one(self, sql, params=()):
        """删除一条数据。"""
        result = None
        try:
            if not self._execute(sql, params):
                return None
            result = self.cursor.fetchone()
            self.commit()
            return result
        except Exception:
            logger.error("删除数据失败！报错原因：{}".format(traceback.format_exc()))
            self.rollback()
            return None
        finally:
            self.close()

    def update_one(self, sql, params=()):
        """修改数据。"""
        result = None
        try:
            if not self._execute(sql, params):
                return None
            result = self.cursor.fetchone()
            self.commit()
            return result
        except Exception:
            logger.error("修改数据失败！报错原因：{}".format(traceback.format_exc()))
            self.rollback()
            return None
        finally:
            self.close()


if __name__ == "__main__":
    my_db = Sql_Control()
    sql = "SELECT 1;"
    result = my_db.get_one(sql)
    print("result:{}".format(result))
