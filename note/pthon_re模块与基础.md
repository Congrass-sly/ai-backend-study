```markdown
# re模块与正则表达式学习笔记 - 2026-05-21

## 一、今天学会的内容

### 1. re模块核心函数

| 函数 | 作用 | 返回值 |
|------|------|--------|
| `re.match(pattern, str)` | 从**开头**匹配 | 匹配对象 / None |
| `re.search(pattern, str)` | 扫描全文，返回**第一个**匹配 | 匹配对象 / None |
| `re.findall(pattern, str)` | 返回**所有**匹配 | 列表（无匹配时返回 []） |
| `re.split(pattern, str)` | 按正则切分字符串 | 列表 |
| `re.compile(pattern)` | 预编译正则，提高效率 | 正则对象 |

### 2. 正则基础语法

#### 元字符

| 元字符 | 含义 | 示例 |
|--------|------|------|
| `.` | 匹配除换行外的任意单个字符 | `a.b` 匹配 `acb`、`a#b` |
| `^` | 匹配字符串开头 | `^Hello` 匹配 `Hello world` |
| `$` | 匹配字符串结尾 | `world$` 匹配 `Hello world` |
| `*` | 前一个字符出现 0 次或多次 | `ab*c` 匹配 `ac`、`abc`、`abbbc` |
| `+` | 前一个字符出现 1 次或多次 | `ab+c` 匹配 `abc`、`abbbc` |
| `?` | 前一个字符出现 0 次或 1 次 | `ab?c` 匹配 `ac`、`abc` |
| `{n}` | 前一个字符出现 n 次 | `\d{11}` 匹配 11 个数字 |
| `{n,}` | 前一个字符至少出现 n 次 | `\d{3,}` 匹配至少 3 个数字 |
| `{n,m}` | 前一个字符出现 n 到 m 次 | `\d{3,5}` 匹配 3-5 个数字 |
| `\|` | 或 | `a\|b` 匹配 `a` 或 `b` |
| `[]` | 字符集合 | `[a-z]` 匹配任意小写字母 |
| `[^]` | 取反字符集合 | `[^0-9]` 匹配非数字 |

#### 量词

| 量词 | 含义 |
|------|------|
| 贪婪匹配 | 默认，尽可能多匹配 |
| 懒惰匹配 | 加 `?`，尽可能少匹配（如 `.*?`） |

### 3. 分组

```python
# 普通分组 ( )
pattern = r'(\d{3})-(\d{8})'
match = re.search(pattern, "电话：010-12345678")
print(match.group(1))  # 010
print(match.group(2))  # 12345678

# 非捕获分组 (?: )
pattern = r'(?:\d{3})-\d{8}'  # 不保存分组

# 命名分组 (?P<name>)
pattern = r'(?P<area>\d{3})-(?P<number>\d{8})'
match = re.search(pattern, "010-12345678")
print(match.group('area'))   # 010
```

### 4. 预定义字符集

| 简写 | 含义 | 等价于 | 注意 |
|------|------|--------|------|
| `\d` | 数字 | `[0-9]` | Python3 匹配 Unicode 数字 |
| `\D` | 非数字 | `[^0-9]` | |
| `\w` | 单词字符 | `[a-zA-Z0-9_]` | Python3 匹配 Unicode 字母 |
| `\W` | 非单词字符 | `[^a-zA-Z0-9_]` | |
| `\s` | 空白字符 | `[ \t\n\r\f\v]` | |
| `\S` | 非空白字符 | `[^ \t\n\r\f\v]` | |

### 5. re模块修饰符（标志）

| 修饰符 | 含义 |
|--------|------|
| `re.I` | 忽略大小写 |
| `re.M` | 多行模式，`^` 和 `$` 匹配每行开头/结尾 |
| `re.S` | 让 `.` 匹配包括换行符在内的任意字符 |
| `re.U` | Unicode 匹配（Python3 默认） |
| `re.X` | 允许正则写注释和空格 |
| `re.A` | ASCII 模式，让 `\d`、`\w` 只匹配 ASCII |

### 6. 常用正则示例

```python
# 手机号
r'^1[3-9][0-9]{9}$'

# 邮箱
r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# 关键词提取
'|'.join(re.escape(kw) for kw in keywords)

# 提取所有数字
re.findall(r'\d+', text)

# 按非数字切分
re.split(r'\D+', text)
```

---

## 二、今天犯的错误

### 错误1：混淆 match 和 group 的返回值

```python
# ❌ 错误
result = re.match(pattern, text)
return result  # 返回匹配对象，不是布尔值

# ✅ 正确
result = re.match(pattern, text)
return result is not None  # 返回布尔值
```

### 错误2：混淆 findall 和 match/search 的使用场景

```python
# match/search：返回匹配对象，只找第一个
# findall：返回列表，找所有匹配

# ❌ 错误：想找所有匹配但用了 search
result = re.search(r'\d+', "1a2b3c")  # 只返回 '1'

# ✅ 正确
result = re.findall(r'\d+', "1a2b3c")  # 返回 ['1', '2', '3']
```

### 错误3：手机号正则写错

```python
# ❌ 错误
r'^1[3-9]$\d{9}'   # $ 位置不对

# ✅ 正确
r'^1[3-9]\d{9}$'
```

### 错误4：邮箱正则中 `\.+` 和 `@+` 不应有 `+`

```python
# ❌ 错误
r'@+'
r'\.+'

# ✅ 正确
r'@'
r'\.'
```

### 错误5：`{2.}` 语法错误

```python
# ❌ 错误
{2.}   # 点不是合法语法

# ✅ 正确
{2,}   # 逗号
```

### 错误6：`re.escape` 用在不该用的地方

```python
# 构建关键词正则时，keywords 中可能有特殊字符（如 . * ?）
# 需要转义
pattern_str = '|'.join(re.escape(kw) for kw in keywords)
```

### 错误7：match 和 fullmatch 区别

```python
# match：只要开头匹配就成功
re.match(r'\d+', "123abc")  # 匹配 "123"

# fullmatch：必须完全匹配整个字符串
re.fullmatch(r'\d+', "123abc")  # None
```

---

## 三、还没学会/不熟的知识点

### 1. 预定义字符集（已会）
- `\w`, `\W`, `\d`, `\D`, `\s`, `\S` ✅

### 2. 需要补充的正则语法

| 语法 | 含义 | 掌握程度 |
|------|------|---------|
| `\b` | 单词边界 | ❌ |
| `\B` | 非单词边界 | ❌ |
| `\A` | 字符串开头（不受 re.M 影响） | ❌ |
| `\Z` | 字符串结尾（不受 re.M 影响） | ❌ |
| `(?=...)` | 正向先行断言 | ❌ |
| `(?!...)` | 负向先行断言 | ❌ |
| `(?<=...)` | 正向后行断言 | ❌ |
| `(?<!...)` | 负向后行断言 | ❌ |
| `(?(id/name)yes\|no)` | 条件匹配 | ❌ |

### 3. re模块其他函数

| 函数 | 作用 | 掌握程度 |
|------|------|---------|
| `re.finditer()` | 返回所有匹配的迭代器 | ❌ |
| `re.sub()` | 替换 | ❌ |
| `re.subn()` | 替换并返回替换次数 | ❌ |
| `re.fullmatch()` | 完全匹配 | ⚠️ 刚学 |

### 4. 修饰符

| 修饰符 | 含义 | 掌握程度 |
|--------|------|---------|
| `re.I` | 忽略大小写 | ✅ |
| `re.M` | 多行模式 | ✅ |
| `re.S` | 让 `.` 匹配换行 | ❌ |
| `re.X` | 允许注释和空格 | ❌ |
| `re.A` | ASCII 模式 | ⚠️ 知道 |
| `re.U` | Unicode 模式（默认） | ⚠️ 知道 |

---

## 四、需要补充的内容

### 补充1：`re.finditer` 用法

```python
# 返回匹配对象的迭代器，适合大文本
for match in re.finditer(r'\d+', "1a2b3c"):
    print(match.group())  # 1, 2, 3
```

### 补充2：`re.sub` 替换

```python
# 将数字替换为 #号
result = re.sub(r'\d', '#', "a1b2c3")  # "a#b#c#"

# 用函数替换
def double(match):
    return str(int(match.group()) * 2)
result = re.sub(r'\d', double, "a1b2c3")  # "a2b4c6"
```

### 补充3：`re.S` 修饰符

```python
# 默认 . 不匹配换行
print(re.findall(r'a.b', "a\nb"))  # []

# re.S 让 . 匹配换行
print(re.findall(r'a.b', "a\nb", flags=re.S))  # ['a\nb']
```

### 补充4：`re.X` 修饰符（允许注释）

```python
pattern = re.compile(r'''
    ^1           # 开头是1
    [3-9]        # 第二位3-9
    \d{9}        # 后面9个数字
    $            # 结尾
''', re.X)
```

### 补充5：单词边界 `\b`

```python
# 匹配单独的 "cat"，不匹配 "catalog"
pattern = r'\bcat\b'
print(re.findall(pattern, "cat catalog"))  # ['cat']
```

### 补充6：正则表达式调试技巧

```python
# 1. 用 print 输出正则字符串检查
print(pattern)

# 2. 用在线工具调试（推荐：regex101.com）

# 3. 用 re.DEBUG 查看编译过程
re.compile(r'^1[3-9]\d{9}$', re.DEBUG)
```

---

## 五、记忆口诀

> **match 开头，search 全文，findall 全找**
> **group 拿值，groups 拿组，return None 要判断**
> **fullmatch 全匹配，split 切分，sub 替换**
> **点号不要换行，re.S 来帮忙**
> **\b 是边界，\B 是反**
> **先行断言 (?=)，后行断言 (?<=)**

---

## 六、速查表

| 需求 | 正则/代码 |
|------|----------|
| 手机号 | `^1[3-9][0-9]{9}$` |
| 邮箱 | `^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$` |
| 提取数字 | `re.findall(r'\d+', text)` |
| 替换数字 | `re.sub(r'\d+', '#', text)` |
| 关键词提取 | `'\|'.join(re.escape(kw) for kw in keywords)` |
| 忽略大小写 | `flags=re.I` |
| 多行模式 | `flags=re.M` |
| 点号匹配换行 | `flags=re.S` |
| 正则注释 | `flags=re.X` |
| ASCII 模式 | `flags=re.A` |

---

*笔记日期：2026-05-21*
```