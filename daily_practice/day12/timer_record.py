"""
任务一：计时装饰器 - 统计函数运行时间
"""

import time
from datetime import datetime


def timer_decorator(func):
    """
    计时装饰器
    
    作用：
        计算被装饰函数的执行时间并打印
    
    参数：
        func: 被装饰的函数
    
    返回：
        wrapper: 包装后的函数
    """
    def wrapper(*args, **kwargs):
        """
        包装函数
        
        *args: 接收任意位置参数
        **kwargs: 接收任意关键字参数
        """
        # 1. 记录开始时间
        start = datetime.now()
        
        # 2. 执行原函数，并保存返回值
        result = func(*args, **kwargs)
        
        # 3. 记录结束时间
        end = datetime.now()
        
        # 4. 计算耗时并打印
        #    end - start 得到 timedelta 对象
        #    total_seconds() 把时间差转换为秒（浮点数）
        #    :.4f 表示保留4位小数
        print(f"函数 {func.__name__}，耗时：{(end - start).total_seconds():.4f} 秒")
        
        # 5. 返回原函数的结果
        return result
    
    return wrapper


# ========== 测试 ==========

@timer_decorator
def sleep_one_second():
    """模拟耗时操作：暂停1秒"""
    time.sleep(1)           # 让程序暂停1秒
    print("执行完毕")       # 函数执行完成后的提示


# 调用被装饰的函数
sleep_one_second()