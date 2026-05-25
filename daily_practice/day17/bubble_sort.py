def bubble_sort(lst):
    """
    冒泡排序

    核心逻辑：
    1. 相邻两个元素比较
    2. 如果前面的比后面的大，就交换
    3. 每一轮把最大的"冒"到末尾
    4. 重复n-1轮
    """
    n = len(lst)
    for i in range(n - 1):           # 外层：控制轮数
        for j in range(n - 1 - i):   # 内层：每轮比较的次数
            if lst[j] > lst[j + 1]:  # 相邻比较
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # 交换
    return lst


# 测试
nums = [64, 34, 25, 12, 22, 11, 90]
print(f"排序前：{nums}")
print(f"排序后：{bubble_sort(nums.copy())}")
