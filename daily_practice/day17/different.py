import time
import random

def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

# 生成10000个随机数
data = [random.randint(0, 10000) for _ in range(10000)]

# 测试冒泡排序
bubble_data = data.copy()
start = time.time()
bubble_sort(bubble_data)
bubble_time = time.time() - start
print(f"冒泡排序：{bubble_time:.4f} 秒")

# 测试选择排序
selection_data = data.copy()
start = time.time()
selection_sort(selection_data)
selection_time = time.time() - start
print(f"选择排序：{selection_time:.4f} 秒")

# 测试Python内置排序（作为对照）
sorted_data = data.copy()
start = time.time()
sorted_data.sort()
builtin_time = time.time() - start
print(f"内置排序：{builtin_time:.6f} 秒")
