# import os

# # 1. 获取当前工作目录
# current_path = os.getcwd()
# print("当前目录：", current_path)

# # 2. 列出当前目录所有文件/文件夹
# print("\n当前目录下所有内容：")
# for item in os.listdir():
#     print(item)

# # 3. 拼接路径（跨平台通用，推荐永远用这个）
# file_path = os.path.join("day4_module", "math_tools.py")
# print("\n拼接后的路径：", file_path)

# # 4. 判断路径是否存在
# print("\nday4_module 是否存在：", os.path.exists("day4_module"))

# # 5. 判断是文件还是文件夹
# print("math_tools.py 是文件：", os.path.isfile(file_path))
# print("day4_module 是文件夹：", os.path.isdir("day4_module"))

# # 6. 分离文件名和后缀
# name_suffix = os.path.splitext("using_sys.py")
# print("\n文件名：", name_suffix[0])
# print("文件后缀：", name_suffix[1])

import os

# ========== 核心万能三板斧 ==========
# 1. __file__：当前脚本本身的路径
# 2. abspath：转绝对路径
# 3. dirname：拿到所在文件夹

# 1. 当前脚本的绝对路径
self_path = os.path.abspath(__file__)
print("1. 当前脚本完整路径：")
print(self_path)

# 2. 当前脚本所在文件夹（day4_moudle）
self_dir = os.path.dirname(self_path)
print("\n2. 当前脚本所在文件夹：")
print(self_dir)

# 3. 项目根目录（回退上一级 ai-backend-study）
root_dir = os.path.dirname(self_dir)
print("\n3. 项目根目录：")
print(root_dir)

# ========== 随便拼接项目里任意文件/文件夹 ==========
# 拼接根目录下的任意文件夹+文件，跨终端、跨位置都不会错
math_tool_path = os.path.join(root_dir, "day4_moudle", "math_tools.py")
print("\n4. 拼接 math_tools.py 完整路径：")
print(math_tool_path)

# 判断是否存在、是文件还是文件夹
print("\n5. 路径检测：")
print("是否存在：", os.path.exists(math_tool_path))
print("是文件：", os.path.isfile(math_tool_path))
print("是文件夹：", os.path.isdir(math_tool_path))

# 列出项目根目录下所有内容
print("\n6. 项目根目录下所有文件/文件夹：")
for item in os.listdir(root_dir):
    print(item)