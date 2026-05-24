"""
正则表达式工具模块
包含 IP 提取、手机号/邮箱校验、关键词提取、数字提取、替换等功能
"""

import re

def extract_ip(text):
    """
    从文本中提取第一个 IPv4 地址

    参数:
        text: 待匹配的字符串

    返回:
        匹配到的 IP 字符串，未找到返回 None
    """
    pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    match = re.search(pattern, text)
    return match.group() if match else None

def validate_phone(phone):
    """
    校验中国大陆手机号（1开头，第二位3-9，共11位）

    参数:
        phone: 手机号字符串

    返回:
        bool: 是否合法
    """
    pattern = r'^1[3-9]\d{9}$'
    return re.match(pattern, phone) is not None

def validate_email(email):
    """
    校验邮箱地址（简化版，支持常见格式）

    参数:
        email: 邮箱字符串

    返回:
        bool: 是否合法
    """
    pattern = r'^[a-zA-Z0-9._%]+@[a-zA-Z0-9._%]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def extract_keywords(text, keywords):
    """
    从文本中提取所有指定的关键词（支持转义特殊字符）

    参数:
        text: 待搜索的文本
        keywords: 关键词列表

    返回:
        list: 匹配到的关键词列表
    """
    pattern_str = '|'.join(re.escape(kw) for kw in keywords)
    pattern = re.compile(pattern_str)
    return pattern.findall(text)

def extract_numbers(text):
    """
    提取文本中的所有连续数字

    参数:
        text: 待搜索的文本

    返回:
        list: 数字字符串列表
    """
    return re.findall(r'\d+', text)

def replace_pattern(text, pattern, repl):
    """
    用正则表达式替换文本中的匹配项

    参数:
        text: 原始文本
        pattern: 正则表达式模式
        repl: 替换字符串

    返回:
        str: 替换后的新字符串
    """
    return re.sub(pattern, repl, text)