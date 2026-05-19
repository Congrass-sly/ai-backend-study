"""
任务三：为已有函数添加多个装饰器
- decorator_timer: 计时装饰器
- decorator_log: 日志装饰器
"""

import random
import time


def decorator_timer(func):
    """计时装饰器：统计函数运行时间"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数 {func.__name__}，耗时：{end - start:.4f} 秒")
        return result
    return wrapper


def decorator_log(func):
    """日志装饰器：记录函数调用信息和返回值"""
    def wrapper(*args, **kwargs):
        print("调用函数之前:")
        result = func(*args, **kwargs)
        print(f"返回值：{result}")
        print("调用函数之后")
        return result
    return wrapper  # ← 修正：必须返回 wrapper


# 两个装饰器同时使用
# 执行顺序：从下往上，先 timer，再 log
@decorator_log      # 2. 然后执行日志
@decorator_timer    # 1. 先执行计时
def generate_code(length=6):
    """
    生成纯数字验证码
    
    参数:
        length: 验证码长度，默认6位
    
    返回:
        str: 纯数字验证码字符串
    """
    code = []
    for i in range(length):
        num = random.randint(0, 9)
        code.append(str(num))
    result = "".join(code)
    return result


# ========== 测试 ==========
generate_code(8)