import random

# 生成一个随机整数，范围在1到10之间
print(random.randint(1, 10))

#从0到1之间生成一个随机小数
print(random.random())

#区间随机小数
print(random.uniform(1, 10))

#从序列随机选一个
print(random.choice(['apple', 'banana', 'cherry']))

#打乱列表顺序
lit = [1, 2, 3, 4, 5]
print("原列表：", lit)
random.shuffle(lit)
print("打乱顺序：", lit)
#随机选多个不重复
print(random.sample(lit, 3))


# 题目3：6位数字验证码
code = []
for i in range(6):  # 循环6次最简单
    num = random.randint(0, 9)
    code.append(str(num))  # 转字符串方便拼接

# 把列表拼成最终验证码
result = "".join(code)
print("6位验证码：", result)