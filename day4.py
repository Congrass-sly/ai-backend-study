from day4_moudle import add, subtract, count_vowels, is_palindrome
import requests

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

    # 测试网络请求工具

url = "https://api.github.com/repos/python/cpython"

# 请求参数
person = {
    "name": "王磊",
    "age": 20,
    "gender": "男"
}

# 请求头伪装浏览器
headers = {
    "User-Agent": "Mozilla/5.0"
}

# 发送GET请求
response = requests.get(
    url,
    params=person,
    timeout=5,
    headers=headers
)
# 调试信息
print(f"状态码: {response.status_code}")
print(f"响应文本: {response.text[:200]}")

if response.status_code == 200 and response.text.strip():
    try:
        read_data = response.json()
    except:
        print("返回的内容不是 JSON 格式")
        read_data = None
else:
    print(f"请求失败: {response.status_code}")
    read_data = None

# 查看状态码
print(response.status_code)
# 查看完整请求链接
print("完整请求网址：", response.url)
# 查看网页文本
print(response.text)
# 解析JSON
read_data = response.json()

if __name__ == "__main__": # 只有当这个脚本被直接运行时，才会执行 main() 函数
    main()