import json

stu = {
    "name": "张三",
    "age": 20,
    "hobby": ["篮球", "足球"],
    "is_student": True
}

# 1. dumps:Python对象转JSON字符串
json_str = json.dumps(stu, ensure_ascii=False, indent=4)
print("JSON字符串：")
print(json_str)
print("类型：", type(json_str))

#2. loads: JSON字符串转Python对象
stu_obj = json.loads(json_str)
print("\nPython对象：")
print(stu_obj)
print("类型：", type(stu_obj))

#3.dump: Python对象转JSON字符串并写入文件
with open("stu.json", "w", encoding="utf-8") as f:
    json.dump(stu, f, ensure_ascii=False, indent=4)
print("\nstu对象已写入stu.json文件")

# 5. load：读取本地 json 文件
with open("stu.json", "r", encoding="utf-8") as f:
    stu_from_file = json.load(f)
print("\n从stu.json文件读取的对象：")
print(stu_from_file)
print("爱好：", stu_from_file["hobby"])
