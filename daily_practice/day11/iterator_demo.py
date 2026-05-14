"""
迭代器与生成器示例代码
包含：手动迭代、迭代器类、生成器函数
"""

# ========== 1. 手动迭代列表 ==========
print("=== 1. 手动迭代列表 ===")

num = [1, 2, 3, 4, 5]

# iter() 从可迭代对象创建迭代器
it = iter(num)

# next() 逐个获取元素
print(next(it))  # 输出: 1
print(next(it))  # 输出: 2

# for 循环会从迭代器当前位置继续
print("剩余元素: ", end="")
for x in it:
    print(x, end="")  # 输出: 345
print("\n")


# ========== 2. 自定义迭代器类（倒计时） ==========
print("=== 2. 自定义迭代器类 ===")

class CountDown:
    """
    倒计时迭代器
    
    实现迭代器协议：
    - __iter__ 返回迭代器对象本身
    - __next__ 返回下一个值，结束时抛出 StopIteration
    """
    
    def __init__(self, start):
        """
        初始化倒计时器
        
        参数:
            start: 起始数字
        """
        self.current = start
    
    def __iter__(self):
        """
        返回迭代器对象本身
        
        for 循环开始时自动调用
        """
        return self
    
    def __next__(self):
        """
        返回下一个倒计数值
        
        返回:
            int: 当前倒计数值
        
        异常:
            StopIteration: 倒计时结束（current == 0）
        """
        # 倒计时结束，停止迭代
        if self.current <= 0:
            raise StopIteration
        
        # 先减1，再返回减之前的值
        # 例如 current=5: 减1变4，返回4+1=5
        self.current -= 1
        return self.current + 1


# 使用 for 循环自动迭代
for num in CountDown(5):
    print(num, end=" ")  # 输出: 5 4 3 2 1
print("\n")


# ========== 3. 生成器函数（对比） ==========
print("=== 3. 生成器函数（对比） ===")

def countdown_generator(start):
    """
    生成器函数版本的倒计时
    
    使用 yield 自动实现迭代器协议，无需手动定义 __iter__ 和 __next__
    """
    while start > 0:
        yield start
        start -= 1

for num in countdown_generator(5):
    print(num, end=" ")  # 输出: 5 4 3 2 1
print("\n")


# ========== 4. 迭代器一次性特性 ==========
print("=== 4. 迭代器一次性特性 ===")

it = iter([1, 2, 3])
print(f"第一次遍历: {list(it)}")  # [1, 2, 3]
print(f"第二次遍历: {list(it)}")  # []（已耗尽）