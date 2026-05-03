from day4_moudle import add, subtract, count_vowels, is_palindrome

def main():
    # 测试数学工具
    num1 = 10
    num2 = 5
    print(f"Addition of {num1} and {num2}: {add(num1, num2)}")
    print(f"Subtraction of {num1} and {num2}: {subtract(num1, num2)}")

    # 测试字符串工具
    test_string = "A man a plan a canal Panama"
    print(f"字符串'{test_string}'中元音的数量: {count_vowels(test_string)}")
    print(f"字符串'{test_string}'是否是回文字符串：{is_palindrome(test_string)}")

if __name__ == "__main__": # 只有当这个脚本被直接运行时，才会执行 main() 函数
    main()