# #字符串切片
# var1 = 'never gonna give you up'
# var2 = 'im gonna let you down'
# print("var1[0]:",var1[0:])
# print("var2[1:9]:",var2[1:9])

# #字符串更新
# var1 = 'never gonna give you up'
# print("更新字符串：",var1[0:] + ", dear Li")

# #转义字符
# print("hello\
#     world\
#     I'm Li")#\表示续行符，表示下一行也是当前行的内容

# print("\\")#输出\，需要使用\\

# print("Li said:\"I am a student.\"")#输出引号需要使用\转义

# print("lisa said:\'I am a student.\'")#输出单引号需要使用\转义

# print("你的特别关心发消息给你了\a")#\a表示响铃符，输出时会发出响声

# print("hello\nworld")#\n表示换行符，输出时会换行

# print("hello\b world")#\b表示退格符，输出时会删除前一个字符

# print("\000")#\000表示空字符，输出时不会显示任何内容

# print("google taobao huawei\r12306")#\r表示回车符，输出时会将光标移到行首，覆盖之前的内容

# print("hello\tworld")#\t表示水平制表符，输出时会在hello和world之间插入一个制表符
# print("hello\vworld")#\v表示垂直制表符，输出时会在hello和world之间插入一个垂直制表符

# print("hello\fworld")#\f表示换页符，输出时会在hello和world之间插入一个换页符

# print("hello\r\nworld")#\r\n表示回车换行符，输出时会换行并将光标移到行首 组合使用

# print("\110\145\154\154\157\40\127\157\162\154\144\41")#\后面跟着八进制数表示对应的字符，输出时会显示对应的字符
# print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x20")#\后面跟着十六进制数表示对应的字符，输出时会显示对应的字符

# # #倒计时
# # import time

# # for i in range(100,0,-1):
# #     sign = '=' * i
# #     space = ' ' * (100 - i)
# #     bar ='[' + sign + space + ']'
# #     print(f"{bar}{i:3}%",end='\r')#\r表示回车符，输出时会将光标移到行首，覆盖之前的内容
# #     time.sleep(0.1)

# # #数字倒计时
# # for a in range(10):
# #     print(f"倒计时：{10-a}秒",end='\r')#\r表示回车符，输出时会将光标移到行首，覆盖之前的内容
# #     time.sleep(1)

# print("B 的 ASCII 码值为：",ord('B'))#ord()函数返回字符的ASCII码值
# #十进制转换
# decimal_number = 255
# print("十进制数 255 转换为二进制：",bin(decimal_number))#bin()函数将十进制数转换为二进制字符串
# print("十进制数 255 转换为八进制：",oct(decimal_number))#oct()函数将十进制数转换为八进制字符串
# print("十进制数 255 转换为十六进制：",hex(decimal_number))#hex()函数将十进制数转换为十六进制字符串

# a = 'Happy Birthday'
# if('a' in a):
#     print("a 在字符串中")
# else:
#     print("a 不在字符串中")

# #\n有关于换行符的使用
# text = "张三\n李四\n王五\n赵六"
# new_text = text.replace("\n", ", ") #将换行符替换为逗号和空格 解法一
# print(new_text)
# new_text = text.split("\n") #将字符串按换行符分割成列表 解法二


# #\t有关于水平制表符的使用
# text = "姓名\t年龄\t性别"
# student1 = "张三\t20\t男"
# student2 = "李四\t22\t女"   
# print(f"{text}\n{student1}\n{student2}")

# #字符串方法
# text = " hello world "
# print(text.upper())#将字符串转换为大写字母  
# print(text.lower())#将字符串转换为小写字母

# print(text.replace(" ", ","))#将字符串中的空格替换为逗号
# print(text.strip(" "))#去除字符串两端的空格

# print(text.split(" "))#将字符串按空格分割成列表
# print("- ".join(text.split(" ")))#将列表中的元素用空格连接成字符串

# print(text.find("world"))#返回字符串中第一次出现"world"的位置，如果没有找到则返回-1
# print(text.count("o"))#返回字符串中"o"出现的次数
# print(text.rfind("o"))#返回字符串中最后一次出现"o"的位置，如果没有找到则返回-1
# print(text.index("o"))#返回字符串中第一次出现"o"的位置，如果没有找到则抛出异常
# print(text.rindex("o"))#返回字符串中最后一次出现"o"的位置，如果没有找到则抛出异常

# print(text.startswith(" hello"))#判断字符串是否以" hello"开头，返回True或False
# print(text.endswith("bye "))#判断字符串是否以"bye "结尾，返回True或False

# print(text.isalpha())#判断字符串是否只包含字母，返回True或False
# print(text.isdigit())#判断字符串是否只包含数字，返回True或False 
# print(text.isalnum())#判断字符串是否只包含字母和数字，返回True或False

#--------------------------------文件IO--------------------------------
import os
import os.path

# ls = []#用来存储找到的.py文件的路径

# def getAppointFile(path, ls):#递归查找指定路径下的所有.py文件，并将它们的路径储存在ls列表中
#     fileList = os.listdir(path)#os.listdir()函数返回指定路径下的所有文件和目录的名称列表，不包括子目录中的内容
#     try:#使用try-except块来处理可能出现的权限错误，如果没有权限访问某个目录，就跳过该目录继续查找其他目录
#         for tmp in fileList:#遍历文件列表中的每个文件或目录，使用os.path.join()函数将路径和文件名连接起来，得到完整的路径
#             pathTmp = os.path.join(path, tmp)#os.path.join()函数将路径和文件名连接起来，得到完整的路径

#         if os.path.isdir(pathTmp):#os.path.isdir()函数判断路径是否是一个目录，如果是目录，就递归调用getAppointFile()函数继续查找该目录下的文件
#             getAppointFile(pathTmp, ls)#递归调用getAppointFile()函数继续查找该目录下的文件

#         elif pathTmp[pathTmp.rfind(".")+1:].upper() == "py":#如果路径不是目录，就判断文件的扩展名是否是.py，如果是.py文件，就将它的路径添加到ls列表中
#             ls.append(pathTmp)#ls.append()方法将指定的元素添加到列表的末尾，这里将找到的.py文件的路径添加到ls列表中
#     except PermissionError:
#         pass#如果没有权限访问某个目录，就跳过该目录继续查找其他目录

# def main():#主函数，提示用户输入要查找的路径，并调用getAppointFile()函数进行查找，最后打印找到的.py文件的路径和数量
#     while True:#使用while循环来不断提示用户输入要查找的路径，直到用户输入一个有效的目录路径为止
#         path = input("请输入要查找的路径：").strip()#input()函数用于获取用户输入的字符串，strip()方法用于去除字符串两端的空格，这样用户输入的路径就不会因为多余的空格而导致错误
#         if os.path.isdir(path):#os.path.isdir()函数判断用户输入的路径是否是一个有效的目录，如果是目录，就调用
#             getAppointFile(path, ls)#调用getAppointFile()函数进行查找，并将找到的.py文件的路径存储在ls列表中
#             break

#     getAppointFile(path, ls)#调用getAppointFile()函数进行查找，并将找到的.py文件的路径存储在ls列表中
#     print(ls)#打印找到的.py文件的路径列表
#     print(len(ls))#打印找到的.py文件的数量，即ls列表的长度

# main()

# os.startfile("python_str_interview_note.md")#打开当前目录下的python_str_interview_note.md文件

# #获取文件扩展名
# def getfile_fix(filename):
#      return filename[filename.rfind('.')+1:]
# print(getfile_fix("python_str_interview_note.md"))#输出md

with open("python_str_interview_note.md", "r", encoding="utf-8") as f:
    content = f.read()
    print("文件内容：", content)
    print("第一次读完，指针在末尾")
    
    f.seek(0)  # 回到开头
    pos = f.tell()  # 输出当前指针位置，应该是0
    print("指针位置：", pos)

    line = f.readline()  # 现在能读到第一行
    print("第一行内容：", line)

    f.seek(0)  # 再次回到开头

    lines = f.readlines()  # 现在能读到所有行
    print("所有行内容：", lines)

with open("text.txt", "w+", encoding="utf-8") as f1:
    print("写入hello world:", f1.write("hello world\n"))
    f1.writelines("li hao\nhello world\nI love you so")

    f1.seek(0)  # 回到开头

    print(f1.read())  # 现在能读到写入的内容

def file_io_demo(): 
    with open("test.txt", "w+", encoding="utf-8") as f:
        f.write("这是一个测试文件。\n")

        f.seek(0)  # 回到开头

        print("大写:", f.read().upper())  # 现在能读到写入的内容

if __name__ == "__main__":
    file_io_demo()