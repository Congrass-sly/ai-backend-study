"""
JsonUtils 类 - JSON 文件/数据操作工具
功能：Python对象与JSON格式的相互转换，支持文件和字符串两种方式
"""

import json


class JsonUtils:
    """
    JSON 工具类（有状态设计）
    
    实例属性:
        file_path: JSON 文件路径（用于 dump/load）
        data: Python 对象（用于 dump/dumps）
        ensure: 是否转义非 ASCII 字符（默认 False，保留中文）
        indent: JSON 缩进空格数（默认 4，美化输出）
    """
    
    def __init__(self, file_path=None, data=None, ensure_ascii=False, indent=4):
        """
        初始化 JSON 工具实例
        
        参数:
            file_path: 文件路径（可选，用于 dump/load）
            data: Python 对象（可选，用于 dump/dumps）
            ensure_ascii: 是否对非 ASCII 字符进行转义，False 时保留中文
            indent: JSON 缩进空格数，用于美化输出
        """
        self.file_path = file_path
        self.data = data
        self.ensure = ensure_ascii
        self.indent = indent

    def dumps(self):
        """
        将 self.data 转换为 JSON 字符串
        
        返回:
            str: JSON 字符串，失败返回 None
        
        异常:
            TypeError: self.data 不是可序列化类型时捕获并打印
        """
        try:
            return json.dumps(self.data, ensure_ascii=self.ensure, indent=self.indent)
        except TypeError as e:
            print(f"错误：数据无法序列化为JSON - {e}")
            return None

    def dump(self):
        """
        将 self.data 写入 self.file_path 指定的 JSON 文件
        
        返回:
            None（失败时返回 None，成功时打印提示）
        
        异常处理:
            FileNotFoundError: 文件路径不存在
            TypeError: 数据无法序列化
            PermissionError: 没有写入权限
        """
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=self.ensure, indent=self.indent)
            print('成功写入')
        except FileNotFoundError:
            print("错误：找不到文件")
        except TypeError as e:
            print(f"错误：数据无法序列化为JSON - {e}")
        except PermissionError:
            print("错误：权限不足")
        
    def loads(self, json_str):
        """
        将 JSON 字符串转换为 Python 对象
        
        参数:
            json_str: JSON 格式的字符串
        
        返回:
            object: 解析后的 Python 对象，失败返回 None
        
        异常:
            JSONDecodeError: 字符串不是有效 JSON 时捕获并打印
        """
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"错误：字符串不是有效的JSON - {e}")
            return None
    
    def load(self):
        """
        从 self.file_path 读取 JSON 文件并转换为 Python 对象
        
        返回:
            object: 解析后的 Python 对象，失败返回 None
        
        异常处理:
            FileNotFoundError: 文件不存在
            PermissionError: 没有读取权限
            JSONDecodeError: 文件内容不是有效 JSON
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("错误：找不到文件")
            return None
        except PermissionError:
            print("错误：权限不足")
            return None
        except json.JSONDecodeError as e:
            print(f"错误：文件内容不是有效的JSON - {e}")
            return None


# ========== 测试代码 ==========
if __name__ == "__main__":
    # 测试数据
    stu = {
        "name": "张三",
        "age": 20,
        "hobby": ["篮球", "足球"],
        "is_student": True
    }
    
    print("=" * 40)
    print("测试1：dumps - Python对象转JSON字符串")
    j = JsonUtils(data=stu, ensure_ascii=False, indent=2)
    json_str = j.dumps()
    print(f"JSON字符串：\n{json_str}")
    
    print("\n" + "=" * 40)
    print("测试2：dump - Python对象写入文件")
    j2 = JsonUtils(file_path="stu.json", data=stu, ensure_ascii=False, indent=4)
    j2.dump()
    
    print("\n" + "=" * 40)
    print("测试3：load - 从文件读取JSON")
    j3 = JsonUtils(file_path="stu.json")
    loaded = j3.load()
    print(f"读取结果：{loaded}")
    
    print("\n" + "=" * 40)
    print("测试4：loads - JSON字符串转Python对象")
    j4 = JsonUtils()
    obj = j4.loads(json_str)
    print(f"转换结果：{obj}")