def selection_sort(lst):
    """
    选择排序

    核心逻辑：
    1. 每轮从未排序部分找到最小的元素
    2. 把它和未排序部分的第一个位置交换
    3. 重复n-1轮
    """
    n = len(lst)
    for i in range(n - 1):           # 外层：控制轮数
        min_idx = i                  # 假设当前位置是最小的
        for j in range(i + 1, n):    # 内层：从未排序部分找最小值
            if lst[j] < lst[min_idx]:
                min_idx = j          # 更新最小值下标
        lst[i], lst[min_idx] = lst[min_idx], lst[i]  # 交换
    return lst


# 测试
nums = [64, 34, 25, 12, 22, 11, 90]
print(f"排序前：{nums}")
print(f"排序后：{selection_sort(nums.copy())}")
