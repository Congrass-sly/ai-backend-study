Python 文件IO & OS 模块 今日笔记
一、open 函数基础
1. 完整语法与省略原理
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
- 除 file 外，其余参数均为「带默认值的可选参数」，可直接省略
- 日常开发/学习，仅需记住 3 个核心参数：文件路径、mode（访问模式）、encoding（编码）
- 文本文件操作必须加 encoding="utf-8"，避免中文乱码
2. 打开文件固定语法（推荐）
with open("文件路径", "模式", encoding="utf-8") as f:
    # 所有读写操作均写在缩进内
- with 上下文管理器：自动关闭文件，无需手动调用 close()
- 缩进内：文件处于打开状态，可正常读写
- 缩进外：文件自动关闭，此时再操作文件会报错：I/O operation on closed file
二、文件访问模式（必背）
1. 三大基础模式
模式
读写权限
文件不存在
文件已存在
指针位置
r
只读
报错
不变
开头
w
只写
新建
清空覆盖
开头
a
只写
新建
末尾追加
末尾
2. 扩展读写模式（可读可写）
- r+：可读可写，不清空文件，文件不存在报错
- w+：可读可写，先清空文件，文件不存在新建
- a+：可读可写，末尾追加，文件不存在新建
三、文件对象常用方法（必背）
1. 读操作（读取文件内容）
- f.read()：一次性读取文件全部内容
- f.readline()：一次读取一行内容（适合大文件，节省内存）
- f.readlines()：读取所有行，返回列表，每行作为一个列表元素
2. 写操作（写入文件内容）
（1）f.write("字符串")
- 只能写入字符串，数字、列表等需先转成字符串（str()）
- 不自动换行，需手动添加换行符 \n
- 有返回值：返回写入的字符个数
# 示例
with open("test.txt", "w", encoding="utf-8") as f:
    count = f.write("hello world\n")  # 写入并获取字符数
print(count)  # 输出：12（hello world + \n）
（2）f.writelines(可迭代对象)
- 可传入字符串、字符串列表（批量写入）
- 不自动换行，需在元素中手动添加 \n
- 无返回值，永远返回 None
# 示例
with open("test.txt", "w", encoding="utf-8") as f:
    f.writelines(["第一行\n", "第二行\n", "第三行"])
3. 文件指针操作
- f.tell()：获取当前文件指针的位置（单位：字节）
- f.seek(offset, whence=0)：移动文件指针
        
  - whence=0（默认）：从文件开头偏移
  - f.seek(0)：指针回到文件开头，可重新读取内容
4. 关键坑点
- read()执行后，指针会跑到文件末尾，再次读取会得到空字符串
- 同个 with 内，写完后想立刻读，需满足两个条件：① 使用 w+/r+/a+ 模式；② 调用f.seek(0) 回到开头
四、文件指针核心概念
- 文件指针：下一次读/写操作的起始位置（类比“看书时眼睛的位置”）
- 读/写操作后，指针会自动向后移动对应字节数
- 指针到达文件末尾时，再次读取会返回空字符串
- 如需重新读取，必须用 f.seek(0) 将指针移回开头
五、文件路径写法（必背）
1. 相对路径
- 适用场景：文件与代码在同一个文件夹
- 写法：直接写文件名，如 "test.txt"
2. 绝对路径
- 适用场景：文件与代码不在同一个文件夹
- 写法（Windows系统，两种均正确）：
        
  - 原始字符串（推荐，避免转义）：r"C:\Users\Admin\test.txt"
  - 双反斜杠（手动转义）："C:\\Users\\Admin\\test.txt"
六、OS 模块核心知识点
1. 模块作用
os = operating system（操作系统），用于让Python操作文件、文件夹、路径、系统命令，是文件/目录操作的核心模块。
2. 常用方法（必背）
- os.getcwd()：获取当前代码所在文件夹路径
- os.listdir(path)：列出指定目录下所有文件和文件夹，返回列表
- os.path.join(path, 文件名)：跨平台路径拼接（自动添加 / 或 \，面试必考）
- os.path.isdir(path)：判断指定路径是否是文件夹（返回 True/False）
- os.path.isfile(path)：判断指定路径是否是文件（返回 True/False）
- os.path.exists(path)：判断指定文件/文件夹是否存在（返回 True/False）
- os.path.splitext(文件名)：分割文件名和后缀（如 os.path.splitext("a.py") 返回 ("a", ".py")）
3. 批量操作文件（高频考点）
（1）批量创建文件
import os
# 批量创建 1~5 的 txt 文件
for i in range(1, 6):
    filename = f"{i}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"这是第{i}个文件\n")
（2）批量重命名文件
import os
# 把 1.txt~5.txt 重命名为 旧_1.txt~旧_5.txt
for i in range(1, 6):
    old_name = f"{i}.txt"
    new_name = f"旧_{i}.txt"
    if os.path.exists(old_name):  # 先判断文件是否存在，避免报错
        os.rename(old_name, new_name)
（3）批量删除文件
import os
# 批量删除 旧_1.txt~旧_5.txt
for i in range(1, 6):
    file_path = f"旧_{i}.txt"
    if os.path.isfile(file_path):  # 确保是文件，避免误删文件夹
        os.remove(file_path)
（4）批量查找文件（面试必考）
场景：遍历目录及所有子目录，查找指定后缀的文件（如 .py、.txt）
import os
# 递归查找所有子目录下的 .py 文件
def find_all_file(path, suffix, res):
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        if os.path.isdir(full_path):  # 如果是文件夹，递归进入
            find_all_file(full_path, suffix, res)
        elif os.path.isfile(full_path) and full_path.endswith(suffix):
            res.append(full_path)

# 使用示例
result = []
find_all_file(r"C:\Users\Admin\Desktop", ".py", result)
print("找到的 .py 文件：", result)
print("文件总数：", len(result))
七、高频易错点汇总（必背）
1. w 模式只能写不能读，强行读会报错 UnsupportedOperation: not readable；想读写用 w+ 模式。
2. write() 和 writelines() 都不会自动换行，必须手动添加\n。
3. 所有文件操作（read/write/tell/seek）必须写在 with 的缩进内，出缩进文件自动关闭。
4. read() 读完后指针在文件末尾，再次读取为空，需用 seek(0) 回到开头。
5. 二进制模式（rb/wb/ab）不能指定 encoding，否则报错。
6. 递归遍历目录时，需捕获 PermissionError，避免因文件夹权限不足导致程序崩溃。
八、经典标准示例（可直接运行）
1. 先写后读（w+ 模式）
def file_io_demo(): 
    with open("test.txt", "w+", encoding="utf-8") as f:
        f.write("这是一个测试文件。\n")
        f.seek(0)  # 指针回到开头，才能读到写入的内容
        print("大写转换：", f.read().upper())

if __name__ == "__main__":
    file_io_demo()
2. 分开写、分开读（最稳妥，推荐）
# 写入内容
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("hello world\n")
    f.writelines(["Python\n", "File IO"])
# 读取内容
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("文件内容：", content)
3. 调用系统软件，直接打开文件（弹窗）
import os
# 打开当前目录下的 test.txt（Windows系统）
os.startfile("test.txt")