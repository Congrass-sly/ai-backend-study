"""
真实数据库连接上下文管理器 - SQLite 版本
功能：自动管理数据库连接的打开、事务提交/回滚、关闭
"""

import sqlite3


class DatabaseConnection:
    """
    数据库连接上下文管理器
    
    实现了上下文管理协议，自动处理：
    - 连接建立（__enter__）
    - 事务提交或回滚（__exit__）
    - 连接关闭（__exit__）
    """
    
    def __init__(self, db_name):
        """
        初始化数据库连接对象
        
        参数:
            db_name: 数据库文件名（如 "example.db"）
        """
        self.name = db_name          # 数据库名称/文件路径
        self.connection = None       # 数据库连接对象
        self.cursor = None           # 游标对象（执行 SQL）

    def __enter__(self):
        """
        进入 with 块时自动调用
        
        作用：
            建立数据库连接，创建游标
        
        返回:
            self: 让 with 块内可以调用 query/execute 方法
        """
        # 建立数据库连接
        self.connection = sqlite3.connect(self.name)
        
        # 创建游标（用于执行 SQL 语句）
        # 修正：从 self.connection 获取游标，不是 sqlite3.connection
        self.cursor = self.connection.cursor()
        
        print(f"已连接到数据库：{self.name}")
        return self

    def __exit__(self, exc_type, exc, tb):
        """
        退出 with 块时自动调用（无论是否发生异常）
        
        参数:
            exc_type: 异常类型（如 ValueError），无异常时为 None
            exc: 异常实例
            tb: 异常追踪信息（traceback）
        
        返回:
            False: 让异常继续向上抛出
        """
        if exc_type is not None:
            # 有异常：回滚事务（撤销本次操作的所有修改）
            self.connection.rollback()
            print(f"事务回滚：{exc_type.__name__}：{exc}")
        else:
            # 无异常：提交事务（将修改保存到数据库）
            self.connection.commit()
            print("事务提交")
        
        # 关闭游标和连接，释放资源
        self.cursor.close()
        self.connection.close()
        print("连接已关闭")
        
        # 返回 False 表示不吞掉异常，让异常继续向上抛出
        return False

    def query(self, sql, params=None):
        """
        执行查询语句（SELECT）
        
        参数:
            sql: SQL 查询语句
            params: 参数元组，用于替换 SQL 中的 ? 占位符
        
        返回:
            list: 查询结果，每行是一个元组
        
        示例:
            >>> db.query("SELECT * FROM users WHERE id=?", (1,))
            [(1, '张三')]
        """
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        return self.cursor.fetchall()  # 获取所有结果行

    def execute(self, sql, params=None):
        """
        执行更新语句（INSERT、UPDATE、DELETE、CREATE TABLE 等）
        
        参数:
            sql: SQL 语句
            params: 参数元组，用于替换 SQL 中的 ? 占位符
        
        返回:
            int: 受影响的行数（INSERT/UPDATE/DELETE 时有效）
        
        示例:
            >>> db.execute("INSERT INTO users VALUES (?, ?)", (1, '张三'))
            1  # 插入了1行
        """
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        
        # rowcount 是属性，不是方法，不加括号
        # 返回受影响的行数
        return self.cursor.rowcount


# ========== 测试代码 ==========
if __name__ == "__main__":
    with DatabaseConnection("example.db") as db:
        # 创建表（如果不存在）
        db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
        
        # 插入数据（? 是占位符，用于防止 SQL 注入）
        db.execute("INSERT INTO users VALUES (?, ?)", (1, "张三"))
        
        # 查询数据
        result = db.query("SELECT * FROM users")
        print(f"查询结果: {result}")