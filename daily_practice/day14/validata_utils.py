"""
正则工具类
功能：手机号校验、邮箱校验、关键词提取
"""

import re


class RegexUtils:
    """正则表达式工具类，封装常用的正则校验功能"""
    
    def validate_phone(self, phone):
        """
        校验中国大陆手机号
        
        规则：
            - 第1位：1
            - 第2位：3-9
            - 后9位：数字
            - 总长度：11位
        
        参数:
            phone: 待校验的手机号字符串
        
        返回:
            bool: 合法返回 True，否则返回 False
        """
        pattern = re.compile(r'^1[3-9]\d{9}$')
        num = pattern.match(phone)
        return num is not None
    
    def validate_email(self, email):
        """
        校验邮箱地址（简化版）
        
        规则：
            - 用户名：字母、数字、点、下划线、短横线
            - 必须包含 @
            - 域名主体：字母、数字、点、短横线
            - 域名后缀：至少2个字母
        
        参数:
            email: 待校验的邮箱字符串
        
        返回:
            bool: 合法返回 True，否则返回 False
        """
        pattern = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        e = pattern.fullmatch(email)
        return e is not None
    
    def find_keywords(self, text, keywords):
        """
        从文本中提取指定的关键词
        
        参数:
            text: 待搜索的文本
            keywords: 关键词列表
        
        返回:
            list: 在文本中出现的关键词列表（按原顺序）
        
        示例:
            >>> utils.find_keywords("我喜欢Python", ["Python", "Java"])
            ['Python']
        """
        # 用 | 连接关键词，如 "Python|Java|Go"
        # re.escape 转义关键词中的特殊字符（如 . * ? 等）
        pattern_str = '|'.join(re.escape(kw) for kw in keywords)
        pattern = re.compile(pattern_str)
        return pattern.findall(text)
    
    def __str__(self):
        """返回类的描述信息"""
        return "RegexUtils 正则工具类 - 提供手机号/邮箱校验、关键词提取功能"


# 测试代码
if __name__ == "__main__":
    utils = RegexUtils()
    print(utils)
    
    # 测试手机号
    print("\n=== 手机号校验 ===")
    print(f"13812345678: {utils.validate_phone('13812345678')}")  # True
    print(f"12812345678: {utils.validate_phone('12812345678')}")  # False（第二位2）
    print(f"1381234567: {utils.validate_phone('1381234567')}")    # False（10位）
    
    # 测试邮箱
    print("\n=== 邮箱校验 ===")
    print(f"test@example.com: {utils.validate_email('test@example.com')}")  # True
    print(f"test@example: {utils.validate_email('test@example')}")          # False（无后缀）
    
    # 测试关键词提取
    print("\n=== 关键词提取 ===")
    text = "我喜欢Python和Java，Go也很流行"
    keywords = ["Python", "Java", "Go", "Ruby"]
    result = utils.find_keywords(text, keywords)
    print(f"文本: {text}")
    print(f"关键词: {keywords}")
    print(f"提取结果: {result}")  # ['Python', 'Java', 'Go']