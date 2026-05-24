"""
装饰器工具模块
提供计时装饰器和日志装饰器
"""

import time

def decorator_time(func):
    """
    计时装饰器：打印函数执行时间

    参数:
        func: 被装饰的函数

    返回:
        wrapper: 包装后的函数
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数 {func.__name__} 执行时间: {end - start:.4f} 秒")
        return result
    return wrapper

def log_decorator(func):
    """
    日志装饰器：打印函数调用信息、参数和返回值

    参数:
        func: 被装饰的函数

    返回:
        wrapper: 包装后的函数
    """
    def wrapper(*args, **kwargs):
        print(f"调用函数 {func.__name__}，参数: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"函数 {func.__name__} 返回值: {result}")
        return result
    return wrapper