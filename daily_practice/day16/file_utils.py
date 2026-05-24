"""
文件操作工具模块
提供带异常处理的文件读写和生成器逐行读取功能
"""

def read_file(file_path):
    """
    读取整个文件内容

    参数:
        file_path: 文件路径

    返回:
        文件内容字符串，失败返回 None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
    except IOError as e:
        print(f"读取文件 {file_path} 时发生错误：{e}")

def write_file(file_path, content):
    """
    将内容写入文件（覆盖模式）

    参数:
        file_path: 文件路径
        content: 要写入的字符串

    返回:
        无返回值，失败时打印错误
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    except IOError as e:
        print(f"写入文件 {file_path} 时发生错误：{e}")

def read_lines_generator(file_path):
    """
    生成器函数，逐行读取文件（适合大文件）

    参数:
        file_path: 文件路径

    生成:
        每一行字符串（包含换行符）
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            yield from f
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
    except IOError as e:
        print(f"读取文件 {file_path} 时发生错误：{e}")