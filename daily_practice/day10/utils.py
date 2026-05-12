"""
工具模块 - 提供数学运算、列表操作、字符串处理、文件读写、验证码生成等功能
"""

import random


# ========== 数学运算 ==========

def add(x, y):
    """两数相加"""
    return x + y


def subtract(x, y):
    """两数相减"""
    return x - y


def multiply(x, y):
    """两数相乘"""
    return x * y


def divide(x, y):
    """两数相除，除数为0时返回错误提示"""
    if y == 0:
        return "除数不能为0"
    return x / y


def calculate(op, x, y):
    """
    根据操作符执行计算（使用字典映射方式）
    
    参数:
        op: 操作符字符串，支持 "add", "sub", "mul", "div"
        x: 第一个数
        y: 第二个数
    
    返回:
        计算结果，或错误提示
    
    注意：
        用 ops 做字典名，避免覆盖传入的形参 op 的值
    """
    ops = {
        "add": lambda x, y: x + y,
        "sub": lambda x, y: x - y,
        "mul": lambda x, y: x * y,
        "div": lambda x, y: x / y if y != 0 else "除数不能为0"
    }
    if op in ops:
        return ops[op](x, y)
    else:
        return "不支持的操作"


# ========== 列表操作 ==========

def list_deduplicate(lst, /):
    """
    列表去重（保持原顺序）
    
    参数:
        lst: 输入列表（位置参数，不支持关键字传参）
    
    返回:
        去重后的新列表
    """
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst


def filter_numbers(numbers):
    """
    对数字列表进行三种过滤
    
    返回:
        tuple: (偶数列表, 奇数列表, 大于2的列表)
    """
    # 过滤出偶数
    even_number = list(filter(lambda x: x % 2 == 0, numbers))
    # 过滤出奇数
    odd_number = list(filter(lambda x: x % 2 != 0, numbers))
    # 过滤出大于2的数
    bigger_than_2 = list(filter(lambda x: x > 2, numbers))
    return even_number, odd_number, bigger_than_2


# ========== 字符串操作 ==========

def split_string(s, delimiter):
    """
    使用指定分隔符拆分字符串
    
    参数:
        s: 输入字符串
        delimiter: 分隔符
    
    返回:
        拆分后的子字符串列表
    """
    return s.split(delimiter)


def reverse_string(s):
    """
    反转字符串
    
    参数:
        s: 输入字符串
    
    返回:
        反转后的字符串（使用切片 [::-1]）
    """
    return s[::-1]


def count_vowels(s):
    """
    统计字符串中元音字母（a、e、i、o、u）的个数
    
    参数:
        s: 输入字符串
    
    返回:
        元音字母个数（不区分大小写）
    """
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def is_palindrome(s):
    """
    检查字符串是否是回文字符串（忽略大小写和空格）
    
    参数:
        s: 输入字符串
    
    返回:
        True: 是回文，False: 不是回文
    
    示例:
        >>> is_palindrome("A man a plan a canal panama")
        True
    """
    # 移除空格并转换为小写
    s = s.replace(" ", "").lower()
    # 反转字符串
    reversed_s = s[::-1]
    # 比较原字符串和反转后的字符串
    return s == reversed_s


# ========== 文件操作 ==========

def read_file(filename):
    """
    读取文件内容并打印
    
    参数:
        filename: 文件名
    
    返回:
        文件内容（字符串），文件不存在时返回空字符串
    
    异常处理:
        FileNotFoundError: 文件不存在时打印提示
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
            return content
    except FileNotFoundError:
        print("错误：文件未找到")
        return ""


# ========== 验证码生成 ==========

def generate_code(length=6):
    """
    生成纯数字验证码
    
    参数:
        length: 验证码长度，默认6位
    
    返回:
        str: 纯数字验证码字符串
    
    示例:
        >>> generate_code(4)
        '3847'
    """
    code = []
    # 循环 length 次，每次生成一个随机数字
    for i in range(length):
        # random.randint(0, 9)：生成 0-9 之间的随机整数
        num = random.randint(0, 9)
        # 将数字转为字符串，存入列表
        code.append(str(num))
    # 将列表中的字符拼接成字符串
    result = "".join(code)
    return result


