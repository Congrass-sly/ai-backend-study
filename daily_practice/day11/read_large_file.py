"""
大文件逐行读取生成器模块
功能：使用生成器逐行读取大文件，避免一次性加载到内存
"""


def read_large_file(file_path, encoding='utf-8'):
    """
    逐行读取大文件的生成器函数
    
    参数:
        file_path: 文件路径（字符串）
        encoding: 文件编码，默认 utf-8
    
    返回:
        generator: 每次 yield 一行内容（包含换行符）
    
    示例:
        >>> for line in read_large_file("data.txt"):
        ...     print(line.strip())
    
    优势:
        使用生成器惰性求值，不会一次性将整个文件读入内存，
        适合处理超大文件（如几GB的日志文件）
    
    异常:
        文件不存在时抛出 FileNotFoundError
        编码错误时抛出 UnicodeDecodeError
    """
    try:
    # with 语句确保文件读取完成后自动关闭
        with open(file_path, 'r', encoding=encoding) as f:
        # 逐行遍历文件对象（文件对象本身是可迭代的）
        # 每次循环读取一行，不会一次性加载整个文件
            for line in f:
                yield line  # 返回当前行，暂停函数状态，等待下次调用
    except FileNotFoundError:
        print(f"错误：找不到文件{file_path}")
        return
    except UnicodeDecodeError:
        print(f"错误：b文件编码不是{encoding}")
        return
    


# ========== 测试代码 ==========
if __name__ == "__main__":
    
    # 测试1：使用 for 循环读取所有行
    print("=== 测试1：for 循环读取全部 ===")
    for line in read_large_file("test_file.txt"):
        # strip() 去掉行尾的换行符和首尾空白
        print(line.strip())

    print("\n=== 测试2：手动 next() 读取前3行 ===")
    # 创建生成器对象
    gen = read_large_file("test_file.txt")
    # 使用 next() 手动控制读取进度
    print(next(gen).strip())  # 第1行
    print(next(gen).strip())  # 第2行
    print(next(gen).strip())  # 第3行

    print("\n=== 测试3：读到某一行就停止 ===")
    # 可以随时中断读取，不会影响文件资源（with 已确保正确关闭）
    for line in read_large_file("test_file.txt"):
        if "第5行" in line:
            print("找到第5行，停止读取")
            break  # 跳出循环，生成器被销毁，文件已关闭
        print(line.strip())