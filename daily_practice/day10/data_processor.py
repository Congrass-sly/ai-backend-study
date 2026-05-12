"""
DataProcessor 类 - 数据处理基础工具
功能：文件读写、数字列表过滤、均值计算、最大值获取
"""

class DataProcessor():
    """数据处理类，封装了文件操作和数字列表处理功能"""
    
    def __init__(self, file_name, numbers, write_data):
        """
        初始化方法
        
        参数:
            file_name: 文件名（用于读写文件）
            numbers: 数字列表（用于计算和过滤）
            write_data: 要写入文件的数据
        """
        self.file_name = file_name
        self.numbers = numbers
        self.write_data = write_data

    def open_file(self):
        """
        读取并打印文件内容
        
        异常处理:
            FileNotFoundError: 文件不存在时提示错误
        """
        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                print(f"文件内容：{f.read()}")
        except FileNotFoundError:
            print("错误：找不到该文件!")

    def write_file(self):
        """
        将 write_data 写入文件（覆盖写入模式）
        
        异常处理:
            Exception: 捕获所有异常并打印错误信息
        """
        try:
            with open(self.file_name, "w", encoding="utf-8") as f:
                f.write(self.write_data)
            print(f"成功写入：{self.write_data}")
        except Exception as e:
            print(f"写入失败：{e}")

    def filter_numbers(self, filter_func):
        """
        根据过滤函数筛选数字列表
        
        参数:
            filter_func: 过滤函数，接收一个数字返回布尔值
        
        返回:
            list: 满足条件的数字列表
        """
        # 判断是否为空列表
        if self.numbers == []:
            return []
        else:
            # filter() 返回迭代器，用 list() 转换为列表
            return list(filter(filter_func, self.numbers))
        
    def mean_numbers(self):
        """
        计算数字列表的平均值
        
        返回:
            float: 平均值；空列表返回 0
        """
        if not self.numbers:
            return 0
        total = 0
        # 遍历累加所有数字
        for i in self.numbers:
            total += i
        mean = total / len(self.numbers)
        return mean
    
    def max_numbers(self):
        """
        获取数字列表的最大值
        
        返回:
            int/float: 最大值
        
        异常:
            ValueError: 空列表时抛出异常
        """
        if not self.numbers:
            raise ValueError("空列表没有最大值")
        return max(self.numbers)
    

# ========== 测试代码 ==========
if __name__ == "__main__":
    # 测试数据
    numbers = [10, 20, 30, 40, 50]
    
    # 创建 DataProcessor 实例
    D1 = DataProcessor("test.txt", numbers, "Hello, Python!")
    
    # 1. 写入文件
    D1.write_file()
    
    # 2. 读取并打印文件
    D1.open_file()
    
    # 3. 过滤数字（大于25的）
    print(D1.filter_numbers(lambda x: x > 25))
    
    # 4. 计算平均值
    print(D1.mean_numbers())
    
    # 5. 获取最大值
    print(D1.max_numbers())