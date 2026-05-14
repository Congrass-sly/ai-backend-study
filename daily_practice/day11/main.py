import sys
from read_large_file import read_large_file
from generator_demo import countdown, gen_count, list_count
from iterator_demo import CountDown, countdown_generator

# 生成器基础
print("=== 倒计时 ===")
for x in countdown(5):
    print(x)

# 内存对比
print("\n=== 内存对比 ===")
list_count = [x for x in range(1000000)]
gen_count = (x for x in range(1000000))
print(f"列表内存：{sys.getsizeof(list_count)} 字节")
print(f"生成器内存：{sys.getsizeof(gen_count)} 字节")

# 大文件读取
print("\n=== 大文件逐行读取 ===")
for line in read_large_file("test_file.txt"):
    print(line.strip())

# 迭代器
print("\n=== 自定义迭代器 ===")
from iterator_demo import CountDown
for num in CountDown(5):
    print(num)