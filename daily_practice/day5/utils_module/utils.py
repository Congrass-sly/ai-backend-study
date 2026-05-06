"""
utils_module - 工具函数模块

提供常用的工具函数，包括：
- filter_numbers: 数字列表过滤
- file_open: 带异常处理的文件读取
"""


def filter_numbers(numbers):
    """
    对数字列表进行三种过滤操作。

    参数:
        numbers (list): 包含整数的列表

    返回:
        tuple: (偶数列表, 奇数列表, 大于2的列表)

    示例:
        >>> filter_numbers([1, 2, 3, 4])
        ([2, 4], [1, 3], [3, 4])
    """
    even_number = list(filter(lambda x: x % 2 == 0, numbers))
    odd_number = list(filter(lambda x: x % 2 != 0, numbers))
    bigger_than_2 = list(filter(lambda x: x > 2, numbers))
    return even_number, odd_number, bigger_than_2


def file_open(filename):
    """
    安全地读取文件内容。

    参数:
        filename (str): 要读取的文件路径

    返回:
        None (仅打印结果，不返回值)

    异常处理:
        - FileNotFoundError: 文件不存在时打印错误信息

    示例:
        >>> file_open("existing.txt")
        文件内容：...
        >>> file_open("not_exist.txt")
        错误：未找到文件
    """
    try:
        with open(filename, 'r+', encoding='utf-8') as f:
            print(f"文件内容：{f.read()}")
    except FileNotFoundError:
        print("错误：未找到文件")