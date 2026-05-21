import re

# ========== re.match() 示例 ==========
# match() 从字符串开头匹配
print(re.match(r'www', 'www.runoob.com').span())  
# 输出: (0, 3) - 在索引0-3位置匹配到'www'

print(re.match(r'com', 'www.runoob.com'))  
# 输出: None - 因为'com'不在开头，match要求从头匹配

# ========== re.match() 提取分组 ==========
line = 'Dogs are smarter than cats'
matchobj = re.match(r'(.*) are (.*?) .*', line, re.I)
# (.*) 贪婪匹配第一个单词 'Dogs'
# are 匹配字面量
# (.*?) 非贪婪匹配 'smarter' (遇到空格就停)
# .* 匹配剩余内容
print(matchobj.group(0))   # 'Dogs are smarter than cats' (完整匹配)
print(matchobj.group(1))   # 'Dogs' (第一个分组)
print(matchobj.group(2))   # 'smarter' (第二个分组)

# ========== re.search() 示例 ==========
# search() 在整个字符串中搜索，不要求从开头开始
print(re.search(r'www', 'www.runoob.com').span())  
# 输出: (0, 3) - 在开头找到'www'

print(re.search(r'com', 'www.runoob.com').span())  
# 输出: (11, 14) - 在索引11-14找到'com'

# ========== re.search() 提取分组 ==========
line = 'Dogs are smarter than cats'
searchobj = re.search(r'(.*) are (.*?) .*', line, re.I)
if searchobj:
    print(f"searchobj_group(0)：{searchobj.group(0)}")  # 完整匹配
    print(f"searchobj_group(1)：{searchobj.group(1)}")  # 'Dogs'
    print(f"searchobj_group(2)：{searchobj.group(2)}")  # 'smarter'
else:
    print("没搜索到")

# ========== re.sub() 替换示例 ==========
phone = "2004-959-559 # 这是一个电话号码"
# 替换注释部分：'#' 后面任意字符直到行尾
num = re.sub(r'#.*$', '', phone)
print(f"电话号码：{num}")  # 输出: "2004-959-559 " (注意末尾有空格)
# 替换非数字字符：\D 匹配任何非数字字符，替换为空
new_num = re.sub(r'\D', '', num)
print(f"电话号码：{new_num}")  # 输出: "2004959559"

# ========== 使用函数作为替换逻辑 ==========
def double(matched):
    value = int(matched.group('value'))  # 获取命名分组的值
    return str(value * 2)  # 返回乘以2的结果

s = 'A23G4HFD567'
# (?P<value>\d+) 命名分组，匹配连续数字
print(re.sub(r'(?P<value>\d+)', double, s))
# 输出: A46G8HFD1134 (23→46, 4→8, 567→1134)

# ========== 分组重排示例 ==========
time = '2026-5-21'
# 将日期格式从 年-月-日 改为 日/月/年
# (\d{4}) 捕获4位数字的年
# (\d{1}) 捕获1位数字的月
# (\d{2}) 捕获2位数字的日
# \3/\2/\1/ 重新排列为 日/月/年
print(re.sub(r'(\d{4})-(\d{1})-(\d{2})', r'\3/\2/\1/', time))
# 输出: 21/5/2026/

# ========== re.compile() 预编译正则表达式 ==========
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # 匹配两个单词，忽略大小写
m = pattern.match('Hello World Wide Find')  # match必须从开头匹配
if m:
    print(m.group(0))      # 'Hello World'
    print(m.span(1))       # (0, 5) 'Hello'的位置
    print(m.span(2))       # (6, 11) 'World'的位置

# ========== re.findall() 查找所有匹配 ==========
# 方式1：直接调用
result1 = re.findall(r'\d+', 'runoob 123 google 456')
# 输出: ['123', '456']

# 方式2：使用编译后的模式
pattern = re.compile(r'\d+')
result2 = pattern.findall('runoob 123 google 456')
# 输出: ['123', '456']

# 带范围限制的findall (只搜索索引0-10)
result3 = pattern.findall('run88oob123google456', 0, 10)
# 在索引0-10范围内查找数字
# 'run88oob123' 中的数字: '88', '123'
# 输出: ['88', '123']
print(result1)
print(result2)
print(result3)

# ========== re.finditer() 返回迭代器 ==========
it = re.finditer(r"\d+", "12a32bc43jf3") 
for match in it: 
    print(match.group())  # 依次输出: 12, 32, 43, 3

# ========== re.split() 分割字符串 ==========
# 方式1：不分隔符不保留
print(re.split(r'\W+', 'runoob, runoob, runoob.'))
# 输出: ['runoob', 'runoob', 'runoob', '']
# 注：末尾的空串因为最后一个分隔符在结尾

# 方式2：使用捕获组，分隔符会保留
print(re.split(r'(\W+)', 'runoob, runoob, runoob.'))
# 输出: ['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']
# 开头的空串：因为字符串以分隔符开始
# 中间保留：分隔符作为独立元素
# 结尾空串：最后一个分隔符后没有字符

# 方式3：限制分割次数 maxsplit=1
print(re.split(r'\W+', 'runoob, runoob, runoob.', 1))
# 输出: ['', 'runoob, runoob, runoob.']
# 只分割1次，剩余部分作为整体保留