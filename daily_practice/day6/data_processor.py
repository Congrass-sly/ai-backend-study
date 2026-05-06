class DataProcessor():
    def __init__(self, file_name, numbers, write_data):
        self.file_name = file_name
        self.numbers = numbers
        self.write_data = write_data

    def open_file(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                print(f"文件内容：{f.read()}")
        except FileNotFoundError:
            print("错误：找不到该文件!")

    def write_file(self):
        try:
            with open(self.file_name, "w", encoding="utf-8") as f:
                f.write(self.write_data)
            print(f"成功写入：{self.write_data}")
        except Exception as e:
            print(f"写入失败：{e}")

    def filter_numbers(self, filter_func):
        if self.numbers == []:
            return []
        else:
            return list(filter(filter_func, self.numbers))
        
    def mean_numbers(self):
        if not self.numbers:
            return 0
        total = 0
        for i in self.numbers:
            total += i
        mean = total / len(self.numbers)
        return mean
    
    def max_numbers(self):
        if not self.numbers:
            raise ValueError("空列表没有最大值")
        return max(self.numbers)

if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    D1 = DataProcessor("test.txt", numbers, "Hello, Python!")
    D1.write_file()
    D1.open_file()
    print(D1.filter_numbers(lambda x: x > 25))
    print(D1.mean_numbers())
    print(D1.max_numbers())