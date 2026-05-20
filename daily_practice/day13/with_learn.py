#with语句工作原理
# mrg = open("text.txt", "r", encoding='utf-8')
# f = mrg.__enter__()
# try:
#     data = f.read()
# finally:
#     mrg.__exit__(None, None, None)

#自定义上下文管理器
class MyContextManager:
    def __enter__(self):#进入上下文
        #申请资源/准备环境
        return 
    
    def __exit__(self, exc_type, exc, tb):#退出上下文
        #释放资源/清理环境
        return False
    
import time

def list_deduplicate(lst, /):
    """
    列表去重（保持原顺序）
    
    参数:
        lst: 输入列表（位置参数，不支持关键字传参）
    
    返回:
        去重后的新列表
    """
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):    #exc_type：异常信息；exc：异常对象；tb：traceback调用栈信息
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"耗时：{self.elapsed}")
        return False                          #返回True:抑止异常；返回False：异常继续抛出
    
lst = [2, 2, 3, 3, 4, 6, 7, 7, 8]

with Timer() as t:
    list_deduplicate(lst)
print(f"耗时秒数：{t.elapsed:.4f}")

from contextlib import suppress, contextmanager, nullcontext
from threading import Lock
"""
contextlib常用工具：
suppress：忽略特定异常
closing：把只有close的对象包装成with
nullcontext：可选的with(不做任何事)
ExitStack：动态进入多个上下文(重点)
"""
# with suppress(ZeroDivisionError):  #忽略异常Zero Division Error
@contextmanager    #生成器写法
def open_file(file_path):     
    """
    生成器写法要点：
    yield返回给as变量约等于__enter__()
    yield后面负责清理（类似__exit__()）
    异常会回到yield处(可在yield后捕获)
    多数情况finally足够
    """                      
    f = open(file_path, 'r', encoding='utf-8')               
    try:
        yield f
    finally:
        f.close()

with open_file('daily_practice/day8/sample.txt') as f:
    print(f.readline())

#nullcontext
def process_file(need_lock):
    lock = Lock() if need_lock else None
    cm = lock if lock is not None else nullcontext()


    with cm:
        with open_file('daily_practice/day8/sample.txt') as f:
            return f.read()
        
# 测试
print(process_file(True))   # 带锁执行
print(process_file(False))  # 不带锁执行

#ExitStack解决问题
from contextlib import ExitStack
"""
资源数量在运行时才知道
想统一进入，统一退出，而不是写一堆嵌套的with
enter_context：进入并登记退出动作
退出时按“先进后出”统一清理
"""
paths = ['daily_practice/day8/sample.txt', 'test_file.txt', 'test.txt']

with ExitStack() as stack:
    files = [stack.enter_context(open(p, 'r', encoding='utf-8')) for p in paths]
    contents = [f.read() for f in files]
    print(contents)

def cleanup(msg):
    print(f"清理：{msg}")

with ExitStack() as stack:
    stack.callback(cleanup, "离开with了")
    f = stack.enter_context(open('test_file.txt', 'r', encoding='utf-8'))
    text = f.read()
    print(text)