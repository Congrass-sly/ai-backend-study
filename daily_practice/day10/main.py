from advanced_processor import AdvancedProcessor
from data_processor import DataProcessor
from data_structures import Stack, Deque
from text_analyzer import count_word_frequency, display_result
from json_utils import JsonUtils
from utils import add, subtract, multiply, divide, calculate, list_deduplicate, filter_numbers, split_string, reverse_string, count_vowels, is_palindrome, generate_code

if __name__ == "__main__":
    # 测试数据
    stu = {
        "name": "张三",
        "age": 20,
        "hobby": ["篮球", "足球"],
        "is_student": True
    }
    
    print("=" * 40)
    print("测试1：dumps - Python对象转JSON字符串")
    j = JsonUtils(data=stu, ensure_ascii=False, indent=2)
    json_str = j.dumps()
    print(f"JSON字符串：\n{json_str}")
    
    print("\n" + "=" * 40)
    print("测试2：dump - Python对象写入文件")
    j2 = JsonUtils(file_path="stu.json", data=stu, ensure_ascii=False, indent=4)
    j2.dump()
    
    print("\n" + "=" * 40)
    print("测试3：load - 从文件读取JSON")
    j3 = JsonUtils(file_path="stu.json")
    loaded = j3.load()
    print(f"读取结果：{loaded}")
    
    print("\n" + "=" * 40)
    print("测试4：loads - JSON字符串转Python对象")
    j4 = JsonUtils()
    obj = j4.loads(json_str)
    print(f"转换结果：{obj}")

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

    numbers = [10, 20, 30, 40, 50]  
    D1 = DataProcessor("test.txt", numbers, "Hello, Python!")
    D1.write_file()
    D1.open_file()
    print(D1.filter_numbers(lambda x: x > 25))
    print(D1.mean_numbers())
    print(D1.max_numbers())

    # 测试1：直接统计字符串
    text = "Hello world! hello python. Hello WORLD"
    result = count_word_frequency(text)
    display_result(result)

    # 测试2：统计文件内容（路径用正斜杠避免转义问题）
    result2 = count_word_frequency('C:/Users/Admin/Desktop/ai-backend-study/daily_practice/day8/sample.txt')
    display_result(result2)

    # 测试 Stack
    print("=" * 40)
    print("测试 Stack")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"栈: {s}")
    print(f"弹出: {s.pop()}")
    print(f"栈顶: {s.peek()}")
    print(f"大小: {s.size()}")
    
    # 测试 Deque
    print("\n" + "=" * 40)
    print("测试 Deque")
    q = Deque([1, 2, 3])
    print(f"初始: {q}")
    q.append(4)
    q.appendleft(0)
    print(f"添加后: {q}")
    print(f"左侧弹出: {q.popleft()}")
    print(f"右侧弹出: {q.pop()}")
    print(f"最终: {q}")


    # 测试数学运算
    print("=== 数学运算测试 ===")
    print(f"add(10, 5): {add(10, 5)}")
    print(f"subtract(10, 5): {subtract(10, 5)}")
    print(f"multiply(10, 5): {multiply(10, 5)}")
    print(f"divide(10, 5): {divide(10, 5)}")
    print(f"divide(10, 0): {divide(10, 0)}")
    print(f"calculate('add', 10, 5): {calculate('add', 10, 5)}")
    print(f"calculate('unknown', 10, 5): {calculate('unknown', 10, 5)}")
    
    # 测试列表操作
    print("\n=== 列表操作测试 ===")
    print(f"list_deduplicate([1,2,2,3,3,3]): {list_deduplicate([1,2,2,3,3,3])}")
    even, odd, big = filter_numbers([1, 2, 3, 4, 5, 6, 7, 8])
    print(f"偶数: {even}, 奇数: {odd}, 大于2: {big}")
    
    # 测试字符串操作
    print("\n=== 字符串操作测试 ===")
    print(f"split_string('a,b,c', ','): {split_string('a,b,c', ',')}")
    print(f"reverse_string('hello'): {reverse_string('hello')}")
    print(f"count_vowels('hello world'): {count_vowels('hello world')}")
    print(f"is_palindrome('racecar'): {is_palindrome('racecar')}")
    print(f"is_palindrome('hello'): {is_palindrome('hello')}")
    
    # 测试验证码
    print("\n=== 验证码测试 ===")
    print(f"generate_code(): {generate_code()}")
    print(f"generate_code(4): {generate_code(4)}")