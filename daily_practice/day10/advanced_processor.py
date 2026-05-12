"""
AdvancedProcessor 类 - DataProcessor 的子类
功能：扩展了统计分析、数据清洗、排序过滤等功能
"""

from data_processor import DataProcessor


class AdvancedProcessor(DataProcessor):
    """高级数据处理器，继承自 DataProcessor"""
    
    def __init__(self, file_name=None, numbers=None, write_data=""):
        """
        初始化方法，兼容两种传参方式
        
        参数:
            file_name: 文件名（如果提供，从文件读取数字）
            numbers: 数字列表（如果提供，直接使用）
            write_data: 写入文件的数据
        """
        # 调用父类初始化，保持兼容性
        # numbers 默认为空列表，file_name 和 write_data 按传入值
        super().__init__(
            numbers=numbers if numbers is not None else [],
            file_name=file_name,
            write_data=write_data
        )
        
        # 如果提供了文件名但没有提供数字列表，从文件加载
        if file_name is not None and numbers is None:
            self.numbers = self._load_numbers()
        
        # 新增私有属性：标记文件是否已被处理
        self.__processed = False
    
    def open_file(self):
        """
        重写 open_file 方法
        调用父类方法并标记已处理状态
        """
        result = super().open_file()  # 调用父类的 open_file
        self.__processed = True       # 标记为已处理
        return result
    
    def is_processed(self):
        """
        检查文件是否已被处理
        
        返回:
            bool: True 表示已处理，False 表示未处理
        """
        return self.__processed
    
    def _load_numbers(self):
        """
        私有方法：从文件加载数字
        
        返回:
            list: 整数列表，文件不存在返回空列表
        """
        try:
            with open(self.file_name, 'r', encoding='utf-8') as f:
                # 逐行读取，去除空白字符，过滤空行，转换为整数
                return [int(line.strip()) for line in f if line.strip()]
        except FileNotFoundError:
            print("文件不存在！")
            return []
    
    def median(self):
        """
        计算中位数
        
        返回:
            float: 中位数；空列表返回 0
        """
        if not self.numbers:
            return 0
        sorted_list = sorted(self.numbers)
        n = len(sorted_list)
        if n % 2 == 0:
            # 偶数长度：中间两个数的平均值
            return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
        else:
            # 奇数长度：中间那个数
            return sorted_list[n // 2]
    
    def std_dev(self):
        """
        计算标准差
        
        返回:
            float: 标准差；空列表返回 0.0
        """
        if not self.numbers:
            return 0.0
        
        n = len(self.numbers)
        mean_val = self.mean_numbers()  # 复用父类方法计算平均值
        
        # 计算方差：各数与平均值的差的平方和，除以个数
        sum_squared_diff = 0
        for x in self.numbers:
            sum_squared_diff += (x - mean_val) ** 2
        
        variance = sum_squared_diff / n
        std_deviation = variance ** 0.5  # 开平方根
        return std_deviation
    
    def count_above(self, threshold):
        """
        统计大于阈值的元素个数
        
        参数:
            threshold: 阈值
        
        返回:
            int: 大于阈值的元素个数；空列表返回 0
        """
        if not self.numbers:
            return 0
        return len([x for x in self.numbers if x > threshold])
    
    def unique(self):
        """
        列表去重（保持原顺序）
        
        返回:
            list: 去重后的列表；空列表返回 []
        """
        if not self.numbers:
            return []
        # dict.fromkeys() 保持插入顺序（Python 3.7+）
        return list(dict.fromkeys(self.numbers))
    
    def sorted_numbers(self, reverse=False):
        """
        排序列表
        
        参数:
            reverse: True 为降序，False 为升序（默认）
        
        返回:
            list: 排序后的新列表；空列表返回 []
        """
        if not self.numbers:
            return []
        return sorted(self.numbers, reverse=reverse)
    
    def filter_numbers(self, filter_func=None):
        """
        过滤数字列表（重写父类方法）
        
        参数:
            filter_func: 过滤函数，接收一个参数返回布尔值
        
        返回:
            list: 过滤后的列表；空列表返回 []
        
        默认行为: 当 filter_func 为 None 时，返回所有 >=0 的数
        """
        if not self.numbers:
            return []
        
        if filter_func is None:
            # 默认过滤：保留非负数
            return [x for x in self.numbers if x >= 0]
        else:
            # 使用自定义过滤函数
            return list(filter(filter_func, self.numbers))


# ========== 测试代码 ==========
if __name__ == "__main__":
    # 测试1：从文件读取数字
    print("=" * 40)
    print("测试1：从文件读取")
    ap = AdvancedProcessor("num.txt")
    print(f"中位数：{ap.median():.2f}")
    print(f"标准差：{ap.std_dev():.2f}")
    
    # 测试2：直接传入数字列表
    print("\n" + "=" * 40)
    print("测试2：直接传入列表")
    ap2 = AdvancedProcessor(numbers=[-1, -5, 0, 4, 3])
    print(f"原始数据: {ap2.numbers}")
    print(f"中位数: {ap2.median():.2f}")
    print(f"标准差: {ap2.std_dev():.2f}")
    print(f"大于3的个数: {ap2.count_above(3)}")
    print(f"去重: {ap2.unique()}")
    print(f"降序排序: {ap2.sorted_numbers(reverse=True)}")
    print(f"默认过滤(>=0): {ap2.filter_numbers()}")
    print(f"自定义过滤(偶数): {ap2.filter_numbers(lambda x: x % 2 == 0)}")