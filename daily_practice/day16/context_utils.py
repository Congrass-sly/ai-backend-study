"""
上下文管理器工具模块
提供数据库连接的上下文管理器
"""

import sqlite3

class DatabaseConnection:
    """SQLite 数据库连接上下文管理器，自动提交或回滚事务"""

    def __init__(self, db_name):
        """
        初始化

        参数:
            db_name: 数据库文件名
        """
        self.name = db_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
        进入上下文时打开连接和游标

        返回:
            self: 用于调用 execute/query 方法
        """
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        print(f"已连接到数据库：{self.name}")
        return self

    def __exit__(self, exc_type, exc_val, tb):
        """
        退出上下文时根据异常决定提交或回滚，并关闭资源

        参数:
            exc_type: 异常类型
            exc_val: 异常值
            tb: traceback

        返回:
            False: 不抑制异常
        """
        if exc_type is not None:
            self.connection.rollback()
            print(f"事务回滚：{exc_type.__name__}：{exc_val}")
        else:
            self.connection.commit()
            print(f"已提交事务：{self.name}")
        self.cursor.close()
        self.connection.close()
        return False

    def execute(self, sql, params=None):
        """
        执行非查询 SQL（INSERT, UPDATE, DELETE 等）

        参数:
            sql: SQL 语句
            params: 参数元组（可选）

        返回:
            int: 受影响的行数
        """
        if params:
            self.cursor.execute(sql, params)
            print(f"执行 SQL: {sql}，参数: {params}")
        else:
            self.cursor.execute(sql)
            print(f"执行 SQL: {sql}")
        return self.cursor.rowcount

    def query(self, sql, params=None):
        """
        执行查询 SQL（SELECT）

        参数:
            sql: SQL 语句
            params: 参数元组（可选）

        返回:
            list: 查询结果列表，每行为元组
        """
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        print(f"执行 SQL: {sql}")
        return self.cursor.fetchall()