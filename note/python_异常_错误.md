# Python 异常处理完整指南

## 目录
1. [异常处理基础](#1-异常处理基础)
2. [自定义异常](#2-自定义异常)
3. [__str__ 与 __repr__](#3-__str__-与-__repr__)
4. [finally 详解与陷阱](#4-finally-详解与陷阱)
5. [异常链](#5-异常链)
6. [常见内置异常](#6-常见内置异常)
7. [断言 assert](#7-断言-assert)
8. [上下文管理器 with](#8-上下文管理器-with)
9. [最佳实践](#9-最佳实践)
10. [面试常见问题](#10-面试常见问题)

---

## 1. 异常处理基础

### 1.1 基本语法

```python
try:
    # 可能抛出异常的代码
    result = 10 / 0
except ZeroDivisionError:
    # 处理特定异常
    print("除数不能为零")
except (TypeError, ValueError) as e:
    # 处理多种异常
    print(f"错误: {e}")
except Exception as e:
    # 捕获所有异常（不推荐作为首选）
    print(f"未知错误: {e}")
else:
    # 没有异常时执行
    print("操作成功")
finally:
    # 无论如何都执行（清理资源）
    print("执行完毕")
```

### 1.2 执行顺序

| 情况 | 执行路径 |
|------|---------|
| `try` 成功 | `try` → `else` → `finally` |
| `try` 异常，被 `except` 捕获 | `try` → `except` → `finally` |
| `try` 异常，未被捕获 | `try` → `finally` → 抛出异常 |

---

## 2. 自定义异常

### 2.1 基本实现

```python
class CustomError(Exception):
    """自定义异常类"""
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        super().__init__(message)
    
    def __str__(self):
        return f"[{self.code}] {self.message}" if self.code else self.message

# 使用
raise CustomError("用户名已存在", code=400)
```

### 2.2 异常继承体系

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ValueError
    ├── TypeError
    ├── ZeroDivisionError
    └── CustomError (你的异常)
```

### 2.3 多级自定义异常

```python
class ValidationError(Exception):
    """验证错误基类"""
    pass

class EmailFormatError(ValidationError):
    """邮箱格式错误"""
    pass

class PasswordWeakError(ValidationError):
    """密码强度不足"""
    def __init__(self, password, reason):
        self.password = password
        self.reason = reason
        super().__init__(f"密码强度不足: {reason}")
```

---

## 3. `__str__` 与 `__repr__`

### 3.1 区别对比

| 方法 | 目标观众 | 要求 | 示例输出 |
|------|---------|------|---------|
| `__str__` | 用户 | 可读性强 | `"用户名不存在"` |
| `__repr__` | 开发者 | 无歧义，最好能重建对象 | `"UserNotFoundError('张三')"` |

### 3.2 回退机制

- 未定义 `__str__` 时，`print(e)` 会调用 `__repr__`
- 未定义 `__repr__` 时，使用默认格式（内存地址）

```python
class MyError(Exception):
    def __repr__(self):
        return "MyError('调试信息')"
    # __str__ 未定义，print 会用 __repr__ 的结果

e = MyError()
print(e)  # 输出: MyError('调试信息')
```

### 3.3 完整示例

```python
class AgeError(Exception):
    def __init__(self, age):
        self.age = age
    
    def __str__(self):
        return f"年龄 {self.age} 不合法"  # 给用户看
    
    def __repr__(self):
        return f"AgeError({self.age})"   # 给程序员看

try:
    raise AgeError(150)
except AgeError as e:
    print(e)           # 输出: 年龄 150 不合法
    print(repr(e))     # 输出: AgeError(150)
```

---

## 4. `finally` 详解与陷阱

### 4.1 资源清理场景

```python
# 文件操作
f = open("file.txt", "w")
try:
    f.write("data")
finally:
    f.close()  # 保证文件一定会关闭

# 网络连接
sock = socket.socket()
try:
    sock.connect(("google.com", 80))
    sock.send(data)
finally:
    sock.close()

# 数据库连接
conn = mysql.connect()
try:
    conn.execute("UPDATE users SET money=money-100 WHERE id=1")
finally:
    conn.close()
```

### 4.2 陷阱1：`finally` 中的 `return` 会覆盖

```python
def test():
    try:
        return 1
    finally:
        return 2  # 覆盖了 return 1

print(test())  # 输出 2
```

### 4.3 陷阱2：`finally` 中的 `return` 会吞掉异常

```python
def test():
    try:
        raise ValueError("出错了")
    finally:
        return 99  # 异常被吞噬

print(test())  # 输出 99，没有报错
```

### 4.4 执行顺序示例

```python
def test():
    try:
        print("开始")
        return "结束"
    finally:
        print("清理")

print(test())
# 输出:
# 开始
# 清理
# 结束
```

**⚠️ 警告：永远不要在 `finally` 中使用 `return`**

---

## 5. 异常链

### 5.1 问题场景

底层异常需要包装成上层业务异常，同时保留原始信息。

### 5.2 三种写法对比

| 写法 | 属性 | 说明 |
|------|------|------|
| `raise NewError()` | `__context__` | 隐式链，自动记录 |
| `raise NewError() from e` | `__cause__` | 显式链，推荐 |
| `raise NewError() from None` | `__cause__ = None` | 禁用链，隐藏原始异常 |

### 5.3 隐式链（`__context__`）

```python
def get_profile():
    try:
        raise ValueError("原始错误：邮箱格式错误")
    except ValueError:
        raise RuntimeError("新错误：用户资料无效")

try:
    get_profile()
except RuntimeError as e:
    print(f"错误: {e}")
    print(f"原始异常: {e.__context__}")
```

### 5.4 显式链（`__cause__`）- 推荐

```python
def get_profile():
    try:
        raise ValueError("原始错误：邮箱格式错误")
    except ValueError as e:
        raise RuntimeError("新错误：用户资料无效") from e

try:
    get_profile()
except RuntimeError as e:
    print(f"错误: {e}")
    print(f"直接原因: {e.__cause__}")
```

**输出效果：**
```
Traceback (most recent call last):
  File "<stdin>", line 2, in get_profile
ValueError: 原始错误：邮箱格式错误

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: 新错误：用户资料无效
```

### 5.5 禁用链（`from None`）

```python
def login():
    try:
        verify_password()
    except InvalidPasswordError:
        raise LoginFailedError("登录失败") from None
```

### 5.6 实际应用场景

```python
class DatabaseError(Exception):
    pass

class UserNotFoundError(DatabaseError):
    pass

def find_user_by_email(email):
    try:
        result = db.query(f"SELECT * FROM users WHERE email='{email}'")
        if not result:
            raise UserNotFoundError(f"用户不存在: {email}")
        return result
    except db.ConnectionError as e:
        raise DatabaseError("数据库连接失败") from e
```

### 5.7 `__cause__` vs `__context__`

| 属性 | 触发方式 | 用途 |
|------|---------|------|
| `__cause__` | `raise ... from e` | 显式声明因果关系 |
| `__context__` | 隐式（except 里 raise） | 自动记录上下文 |

---

## 6. 常见内置异常

| 异常 | 触发条件 | 示例 |
|------|---------|------|
| `ValueError` | 值正确但类型不对 | `int("abc")` |
| `TypeError` | 类型错误 | `"1" + 1` |
| `KeyError` | 字典键不存在 | `d["key"]` |
| `IndexError` | 列表索引越界 | `lst[100]` |
| `AttributeError` | 对象没有该属性 | `None.name` |
| `FileNotFoundError` | 文件不存在 | `open("no.txt")` |
| `ZeroDivisionError` | 除零错误 | `10 / 0` |
| `TimeoutError` | 操作超时 | 网络请求超时 |

---

## 7. 断言 `assert`

```python
def divide(a, b):
    assert b != 0, "除数不能为零"  # 调试用
    return a / b

# 生产环境可用 -O 参数禁用断言
# python -O script.py
```

**注意：** `assert` 用于**调试**和**内部检查**，不要用于数据验证。

---

## 8. 上下文管理器 `with`

### 8.1 替代 `try-finally`

```python
# 传统写法
f = open("file.txt", "r")
try:
    content = f.read()
finally:
    f.close()

# with 语句
with open("file.txt", "r") as f:
    content = f.read()
# 自动调用 f.close()
```

### 8.2 自定义上下文管理器

```python
class ManagedFile:
    def __enter__(self):
        self.file = open("file.txt", "w")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# 使用
with ManagedFile() as f:
    f.write("hello")
```

### 8.3 使用 `contextlib` 简化

```python
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    f = open(name, "w")
    try:
        yield f
    finally:
        f.close()

with managed_file("test.txt") as f:
    f.write("hello")
```

---

## 9. 最佳实践

### ✅ 推荐做法

```python
# 1. 捕获具体异常
try:
    value = int(user_input)
except ValueError:
    print("请输入数字")

# 2. 异常携带有用信息
raise ValidationError(f"字段 '{field}' 不能为空")

# 3. 记录日志
import logging
try:
    risky_operation()
except Exception as e:
    logging.exception("操作失败")  # 自动记录异常堆栈

# 4. 保留异常链
try:
    low_level_operation()
except LowLevelError as e:
    raise HighLevelError("操作失败") from e
```

### ❌ 不推荐做法

```python
# 1. 捕获所有异常却不处理
try:
    process()
except:  # 会捕获 KeyboardInterrupt、SystemExit
    pass

# 2. 在 finally 中 return
def bad():
    try:
        return 1
    finally:
        return 2  # 灾难

# 3. 吞掉异常不记录
try:
    risky()
except:
    pass  # 什么都不知道，调试噩梦

# 4. 用异常做流程控制
try:
    get_value()
except KeyError:
    # 预期内的情况，应该用 if 判断
    pass
```

---

## 10. 面试常见问题

### Q1: `except Exception` 和 `except` 的区别？

| 写法 | 捕获范围 |
|------|---------|
| `except:` | 捕获所有异常（含 `KeyboardInterrupt`、`SystemExit`） |
| `except Exception:` | 不捕获系统级异常，更安全 |

### Q2: `raise` 和 `raise e` 的区别？

```python
try:
    1/0
except ZeroDivisionError as e:
    raise      # 保留原始堆栈 ✅
    raise e    # 可能丢失上下文 ⚠️
```

### Q3: `else` 子句什么时候执行？

`try` 块**没有抛出任何异常**时执行，常用于放置依赖 `try` 成功结果的代码。

### Q4: 如何创建不吞噬原始异常的异常链？

```python
raise NewError() from original_exception
```

### Q5: `__cause__` 和 `__context__` 有什么区别？

- `__cause__`：显式设置，语义为"直接原因"
- `__context__`：隐式记录，语义为"发生在此上下文中"

### Q6: 什么时候用 `from None`？

- 安全/隐私场景：不想暴露内部错误细节
- 异常已经足够明确，不需要底层信息
- 重构且想保持 API 兼容性

---

## 11. 记忆口诀

| 知识点 | 口诀 |
|--------|------|
| try-except-else-finally | try 干活，except 挡灾，else 成功时，finally 永在 |
| 自定义异常 | 继承 Exception，`__init__` 记数据，`__str__` 给人看 |
| finally 的 return | return 说走，finally 说不，走之前先收拾 |
| 异常链 | from 是绳子，把两个异常拴一起 |
| with 语句 | try-finally 的语法糖，自动帮你关门窗 |

---

## 12. 快速参考卡片

# 基本结构
try:
    ...
except ErrorType as e:
    ...
else:
    ...
finally:
    ...

# 自定义异常
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)

# 异常链
raise NewError() from original

# 抛出异常
raise ValueError("错误信息")

# 断言
assert condition, "错误信息"

# with 语句
with open("file.txt") as f:
    data = f.read()
