import requests

# 目标API地址：GitHub官方提供的Python仓库公开API
url = "https://api.github.com/repos/python/cpython"

# 请求参数（会作为查询字符串拼接到URL后面）
# 注意：GitHub API 并不接受这些参数，这里仅作为示例演示params的用法
person = {
    "name": "王磊",
    "age": 20,
    "gender": "男"
}

# 请求头：伪装成浏览器，防止被服务器拒绝
headers = {
    "User-Agent": "Mozilla/5.0"  # 模拟Chrome浏览器标识
}

# ========== 发送GET请求 ==========
# params: 将字典自动转换为查询字符串 ?name=王磊&age=20&gender=男
# timeout: 设置超时时间5秒，防止请求卡死
# headers: 添加请求头
response = requests.get(
    url,
    params=person,
    timeout=5,
    headers=headers
)

# ========== 调试信息 ==========
print(f"状态码: {response.status_code}")
print(f"响应文本前200字符: {response.text[:200]}")

# ========== 安全检查 + JSON解析 ==========
# 检查状态码是否为200（成功）且响应内容非空
if response.status_code == 200 and response.text.strip():
    try:
        read_data = response.json()  # 尝试解析JSON
    except:
        # 如果解析失败（比如返回HTML），打印提示
        print("返回的内容不是 JSON 格式")
        read_data = None
else:
    print(f"请求失败: {response.status_code}")
    read_data = None

# ========== 输出详细信息 ==========
# 再次打印状态码（和上面重复，可能是调试遗留）
print(response.status_code)

# 打印实际请求的完整URL（可以看到params被拼接到URL后面）
print("完整请求网址：", response.url)

# 打印完整的响应文本（可能很大）
print(response.text)

#打印响应的json数据
print(read_data)