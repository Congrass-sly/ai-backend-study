"""
模块说明：演示从 utils_module 导入工具函数的使用
功能包括：数字过滤、文件读取、目录信息查看
"""

from utils_module import file_open, filter_numbers
import os

# ========== 数字列表过滤 ==========
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# 调用过滤函数，返回三个元组：偶数列表、奇数列表、大于2的列表
a, b, c = filter_numbers(numbers)

# 打印过滤结果
print(a)  # 偶数列表: [2, 4, 6, 8]
print(b)  # 奇数列表: [1, 3, 5, 7]
print(c)  # 大于2的列表: [3, 4, 5, 6, 7, 8]

# ========== 调试信息：查看当前工作目录 ==========
print("当前目录:", os.getcwd())

# 列出当前目录下的所有文件和文件夹
print("文件夹内容:", os.listdir("."))

# ========== 读取文件 ==========
# 使用相对路径读取文件（路径相对于当前工作目录）
file_open("daily_practice/day5/day5.py")
