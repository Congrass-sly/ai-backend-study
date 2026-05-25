import time

class SortUtils:
    """排序工具类"""

    @staticmethod
    def bubble_sort(lst):
        """冒泡排序"""
        n = len(lst)
        result = lst.copy()  # 不修改原列表
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result

    @staticmethod
    def selection_sort(lst):
        """选择排序"""
        n = len(lst)
        result = lst.copy()
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if result[j] < result[min_idx]:
                    min_idx = j
            result[i], result[min_idx] = result[min_idx], result[i]
        return result

    @staticmethod
    def compare(lst):
        """对比两种排序的耗时"""
        import random

        # 冒泡
        data1 = lst.copy()
        start = time.time()
        SortUtils.bubble_sort(data1)
        bubble_time = time.time() - start

        # 选择
        data2 = lst.copy()
        start = time.time()
        SortUtils.selection_sort(data2)
        selection_time = time.time() - start

        # 内置
        data3 = lst.copy()
        start = time.time()
        data3.sort()
        builtin_time = time.time() - start

        print(f"数据量：{len(lst)}")
        print(f"冒泡排序：{bubble_time:.4f} 秒")
        print(f"选择排序：{selection_time:.4f} 秒")
        print(f"内置排序：{builtin_time:.6f} 秒")


if __name__ == "__main__":
    import random
    data = [random.randint(0, 10000) for _ in range(10000)]
    SortUtils.compare(data)
