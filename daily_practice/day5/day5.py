from utils_module.utils import file_open
import requests
#====================================多返回值调用
def get_user():
    name = "小明"
    age = 18
    city = "北京"
    return name, age, city  # 返回多个值，用逗号隔开

n, a, c = get_user()  # 接收多个返回值，分别赋值给变量n、a、c
print(n)  # 输出小明
print(a)  # 输出18
print(c)  # 输出北京

#=====================================关键字参数调用
def show_info(name, age, **info):   #定义一个函数show_info，接受两个位置参数name和age，以及一个可变关键字参数info
    print(f"姓名：{name}, 年龄：{age}")   #输出姓名和年龄
    for k, v in info.items():        #遍历info字典中的键值对，输出其他信息
        print(f"{k}: {v}")

show_info("小红", 20, city="上海", hobby="画画")  #调用函数show_info，传入姓名、小红，年龄20，以及其他信息城市和爱好

#=====================================文件的下载和清理
def download_file(url):    #定义一个函数download_file，接受一个参数url，表示要下载的文件的URL地址
    print("📡 开始下载...")
    temp_file = "temp.dat"
    try:
        # 假装下载
        open(temp_file, "w").write("data")   #创建一个临时文件temp.dat，并写入一些数据，模拟下载过程
        return "下载成功"
    finally:
        print("🧹 清理临时文件...")
        import os
        if os.path.exists(temp_file):
            os.remove(temp_file)  # 清理：删除临时文件
        print("✅ 清理完成")

result = download_file("http://example.com/file")  #调用download_file函数，传入一个URL地址，并将返回结果赋值给变量result
print(result)  #输出下载结果


#=====================================编写带异常处理的文件读取函数
def read_file(filename):#定义一个函数read_file，接受一个参数filename，表示要读取的文件名
    try:
        open(filename)  #尝试打开文件，如果文件不存在会引发FileNotFoundError异常
        print("文件读取成功")
    except FileNotFoundError:  #捕获FileNotFoundError异常，并输出错误信息
        print("错误：文件未找到")

read_file("nonexistent.txt")  #调用read_file函数，传入一个不存在的文件名，触发异常处理逻辑
read_file(__file__)  #调用read_file函数，传入当前脚本的文件名，成功读取文件并输出成功信息

# #=====================================列表偶数过滤函数
# numbers = [1, 2, 3, 4, 5, 6]
# def filter_even_numbers(numbers):
#     even_number = list(filter(lambda x:x % 2 == 0, numbers))  #使用filter函数和lambda表达式过滤出列表中的偶数，并将结果转换为列表
#     return even_number  #返回过滤后的偶数列表

# print(filter_even_numbers(numbers))  #调用filter_even_numbers函数，传入一个包含数字的列表，并输出过滤后的偶数列表

#========================================升级函数
numbers = [1, 2, 3, 4, 5, 6]
def filter_numbers(numbers):
    even_number = list(filter(lambda x:x % 2 == 0, numbers))  #使用filter函数和lambda表达式过滤出列表中的偶数，并将结果转换为列表
    odd_number = list(filter(lambda x:x % 2 != 0, numbers))   #使用filter函数和lambda表达式过滤出列表中的奇数，并将结果转换为列表
    bigger_than_2 = list(filter(lambda x:x > 2, numbers))     #使用filter函数和lambda表达式过滤出列表中比2大的数，并将结果转化为列表
    return even_number, odd_number, bigger_than_2  #返回过滤后的偶数列表
e_n, o_n, b_t = filter_numbers(numbers)
print(e_n)
print(o_n)
print(b_t)

#=========================================隐式异常链
def get_profile():
    try:
        raise ValueError("原始错误：邮箱格式错误")
    except ValueError:
        raise RuntimeError("新错误：用户资料无效")

try:
    get_profile()
except RuntimeError as e:
    print(f"错误: {e}")
    print(f"原始异常: {e.__context__}")

#=========================================显示异常链
def get_profile():
    try:
        raise ValueError("原始错误：邮箱格式错误")
    except ValueError as e:
        raise RuntimeError("新错误：用户资料无效") from e

try:
    get_profile()
except RuntimeError as e:
    print(f"错误: {e}")
    print(f"直接原因: {e.__cause__}")

