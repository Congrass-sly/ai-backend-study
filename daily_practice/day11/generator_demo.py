"""
生成器内存优势演示
对比列表推导式和生成器表达式的内存占用
"""

import sys


def countdown(n):
    """
    生成器函数：倒计时
    
    使用 yield 实现惰性生成，每次只产生一个值
    """
    while n > 0:
        yield n
        n -= 1


# ========== 1. 使用生成器函数 ==========
print("=== 1. 生成器函数 ===")
for x in countdown(5):
    print(x, end=" ")  # 输出: 5 4 3 2 1
print("\n")


# ========== 2. 内存对比 ==========
print("=== 2. 内存对比 ===")

# 列表推导式：一次性生成所有元素，占用大量内存
# 100万个整数，每个28字节（Python int），约28MB
list_count = [x for x in range(1000000)]
print(f"列表内存占用：{sys.getsizeof(list_count):,} 字节")

# 生成器表达式：惰性生成，只保存状态（指针、当前位置等）
# 内存占用固定，与数据量无关
gen_count = (x for x in range(1000000))
print(f"生成器内存占用：{sys.getsizeof(gen_count):,} 字节")


# ========== 内存说明 ==========
print("\n=== 3. 内存说明 ===")
print("列表：一次性创建100万个元素，占用约 8,000,000 字节（8MB）")
print("      + 每个int对象额外的内存开销")
print("生成器：只保存生成器对象本身（约 120 字节），与数据量无关")