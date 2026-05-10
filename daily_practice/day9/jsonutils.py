import json

class JsonUtils:
    def __init__(self, file_path=None, data=None, ensure_ascii=False, indent=4):
        self.file_path = file_path
        self.data = data
        self.ensure = ensure_ascii
        self.indent = indent

    def dumps(self):
        try:
            return json.dumps(self.data, ensure_ascii=self.ensure, indent=self.indent)
        except TypeError as e:
            print(f"错误：数据无法序列化为JSO - {e}")
            return
    
    def dump(self):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=self.ensure, indent=self.indent)
            print('成功写入')
            return
        except FileNotFoundError:
            print("错误：找不到文件")
            return
        except TypeError as e:
            print(f"错误：数据无法序列化为JSO - {e}")
            return
        except PermissionError:
            print("错误：权限不足")
            return
        
    def loads(self, json_str):
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"错误：字符串不是有效的JSON - {e}")
            return
    
    def load(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("错误：找不到文件")
            return
        except PermissionError:
            print("错误：权限不足")
            return
        except json.JSONDecodeError as e:
            print(f"错误：字符串不是有效的JSON - {e}")
            return 


if __name__ == "__main__":
    # 测试数据
    stu = {
        "name": "张三",
        "age": 20,
        "hobby": ["篮球", "足球"],
        "is_student": True
    }
    
    # 方式B：有状态使用
    j = JsonUtils(file_path="stu.json", data=stu, ensure_ascii=False, indent=4)
    
    # 1. 测试 dumps
    json_str = j.dumps()
    print("dumps结果：", json_str)
    
    # 2. 测试 dump
    j.dump()
    
    # 3. 测试 load
    j2 = JsonUtils(file_path="stu.json")
    loaded_data = j2.load()
    print("load结果：", loaded_data)
    
    # 4. 测试 loads
    j3 = JsonUtils()
    obj = j3.loads(json_str)
    print("loads结果：", obj)

