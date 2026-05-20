"""
自定义数据库连接上下文管理器 - 完整版
功能：模拟数据库连接的建立、事务提交/回滚、自动关闭
"""

import time

class DataBaseConnection:
    """
    数据库连接上下文管理器
    
    实现了上下文管理协议（__enter__ 和 __exit__）
    用于模拟数据库连接的自动管理
    """
    
    def __init__(self, db_name):
        """
        初始化数据库连接对象
        
        参数:
            db_name: 数据库名称（用于标识连接）
        """
        self.name = db_name          # 数据库名称
        self.connection = None       # 连接对象（模拟）
    
    def __enter__(self):
        """
        进入 with 块时自动调用
        
        作用：
            建立数据库连接
        
        返回:
            self: 返回实例本身，让 with 块内可以调用方法
        """
        print("正在连接中")
        self.connection = '我是被连接的'  # 模拟连接成功
        return self
    
    def __exit__(self, exc_type, exc, tb):
        """
        退出 with 块时自动调用（无论是否发生异常）
        
        参数:
            exc_type: 异常类型（如 ValueError），无异常时为 None
            exc: 异常实例
            tb: 异常追踪信息
        
        返回:
            False: 让异常继续向上传播（不吞掉异常）
        """
        # 检查是否有异常发生
        if exc_type is not None:
            # 有异常：回滚事务
            print(f"发生异常：{exc_type.__name__}: {exc}")
            print("事务已回滚")
        else:
            # 无异常：提交事务
            print("事务已提交")
        
        # 关闭连接
        self.connection = None
        print("连接已关闭")
        
        # 返回 False 表示不吞掉异常，让异常继续向上抛出
        return False
    
    def query(self, sql):
        """
        执行查询操作
        
        参数:
            sql: SQL 查询语句
        
        返回:
            list: 模拟的查询结果
        
        异常:
            RuntimeError: 未连接数据库时抛出
        """
        if self.connection is None:
            raise RuntimeError("未连接数据库")
        print(f"执行SQL：{sql}")
        # 模拟查询结果
        return [{"id": 1, "name": "张三"}]


# ========== 测试1：正常使用（无异常） ==========
print("=== 测试1：正常使用 ===")
with DataBaseConnection('test.txt') as dbc:
    print('在with块内')
    print(f'连接对象：{dbc.connection}')
    print(f'数据库名：{dbc.name}')
    # 执行查询
    result = dbc.query("SELECT * FROM users")
    print(f"查询结果：{result}")

print("\n" + "=" * 50 + "\n")

# ========== 测试2：异常情况（事务回滚） ==========
print("=== 测试2：发生异常 ===")
try:
    with DataBaseConnection('test.txt') as dbc:
        print('在with块内')
        # 模拟异常发生
        raise ValueError("模拟异常")
except ValueError as e:
    print(f"捕获到异常：{e}")