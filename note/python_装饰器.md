```markdown
# 装饰器学习笔记 - 2026-05-19

## 一、今天学会的内容

### 1. 装饰器基础概念

- 装饰器本质是一个**函数**，接收一个函数作为参数，返回一个新函数
- `@` 语法糖：`@deco` 等价于 `func = deco(func)`

### 2. 计时装饰器（任务一）

- 用 `time.time()` 或 `datetime.now()` 记录开始/结束时间
- 计算耗时并打印
- 关键：`datetime` 时间差需用 `.total_seconds()` 转换

### 3. 日志装饰器（任务二）

- 记录函数调用前后的状态
- 打印函数的返回值

### 4. 多个装饰器叠加（任务三）

- 从下往上执行：离函数近的先执行
- 等价于：`func = outer(inner(func))`

### 5. 类装饰器（单例模式）

- `__init__` 接收被装饰的类
- `__call__` 使实例可调用，控制实例创建次数

### 6. 闭包原理

- 闭包 = 函数 + 它引用的外部变量
- 外部函数执行完后，内部函数仍能记住外部变量
- Python 把外部变量保存在 `__closure__` 属性中

### 7. 手动调用装饰器的场景

- 装饰器参数需要动态决定
- 条件性装饰（if/else 判断）
- 运行时替换/移除装饰器
- 批量装饰多个函数

---

## 二、今天犯的错误（附代码）

### 错误1：导入模块大小写错误

```python
# ❌ 错误
import Datetime
datetime.now()

# ✅ 正确
import datetime
datetime.datetime.now()

# 或
from datetime import datetime
datetime.now()
```

---

### 错误2：`datetime` 时间差格式化错误

```python
# ❌ 错误
end = datetime.now()
start = datetime.now()
print(f"耗时：{end - start:.4f}秒")

# ✅ 正确
print(f"耗时：{(end - start).total_seconds():.4f}秒")

# ✅ 更简单：用 time.time()
import time
start = time.time()
end = time.time()
print(f"耗时：{end - start:.4f}秒")
```

**原因**：`end - start` 是 `timedelta` 对象，不是数字，不能直接用 `:.4f` 格式化。

---

### 错误3：装饰器忘记返回 wrapper

```python
# ❌ 错误
def decorator_log(func):
    def wrapper(*args, **kwargs):
        print("调用前")
        result = func(*args, **kwargs)
        print("调用后")
        return result
    return   # 没有返回 wrapper

@decorator_log
def say_hello():
    print("Hello")

say_hello()  # TypeError: 'NoneType' object is not callable

# ✅ 正确
def decorator_log(func):
    def wrapper(*args, **kwargs):
        print("调用前")
        result = func(*args, **kwargs)
        print("调用后")
        return result
    return wrapper
```

---

### 错误4：`wrapper` 拼写错误

```python
# ❌ 错误
def warpper(*args, **kwargs):

# ✅ 正确
def wrapper(*args, **kwargs):
```

---

### 错误5：多个装饰器的执行顺序理解反了

```python
# 代码
@log
@timer
def func():
    pass

# ❌ 错误理解：先执行 log，再执行 timer
# ✅ 正确理解：从下往上执行，先 timer，后 log

# 等价于：
func = log(timer(func))
```

---

## 三、还没完全学会的（附代码示例）

### 1. 带参数的装饰器

```python
# 目标：实现 @repeat(3) 这样的装饰器
@repeat(3)
def say_hello():
    print("Hello")

# 输出：
# Hello
# Hello
# Hello

# 模板
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator
```

### 2. 类装饰器的 `__call__` 原理

```python
class CountDecorator:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"第 {self.count} 次调用")
        return self.func(*args, **kwargs)

@CountDecorator
def say_hello():
    print("Hello")

say_hello()  # 第 1 次调用 \n Hello
say_hello()  # 第 2 次调用 \n Hello
```

### 3. `functools.wraps` 保留原函数元数据

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # ← 加上这行
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello():
    """这是 say_hello 的文档"""
    print("Hello")

print(say_hello.__name__)  # 不加 @wraps: 'wrapper'
print(say_hello.__doc__)   # 不加 @wraps: None
# 加上 @wraps 后：'say_hello' 和 '这是 say_hello 的文档'
```

### 4. 装饰器在类中装饰类方法

```python
def log_method(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"调用方法: {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

class MyClass:
    @log_method
    def say_hello(self):
        print("Hello")

obj = MyClass()
obj.say_hello()
# 输出：
# 调用方法: say_hello
# Hello
```

### 5. 多个装饰器的数据传递

```python
# 场景：外层装饰器需要内层装饰器返回的数据
def add_hello(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Hello, {result}"
    return wrapper

def add_exclamation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{result}!"
    return wrapper

@add_hello
@add_exclamation
def get_name():
    return "World"

print(get_name())  # Hello, World!
# 执行顺序：add_exclamation 先加 "!"，然后 add_hello 加 "Hello, "
```

---

## 四、记忆口诀

> **装饰器：函数包函数，@ 号语法糖**
> **计时装饰器：开始结束减一减，total_seconds 来转换**
> **日志装饰器：调用前后都打印，返回值也要看**
> **多个装饰器：从下往上执行，离得近的先包装**
> **闭包：函数记变量，外部结束也不忘**

---

## 五、速查模板

| 需求 | 代码模板 |
|------|---------|
| 无参数装饰器 | `def deco(func):\n    def wrapper(*a,**kw):\n        ...\n        return func(*a,**kw)\n    return wrapper` |
| 带参数装饰器 | `def deco(param):\n    def outer(func):\n        def wrapper(*a,**kw):\n            ...\n        return wrapper\n    return outer` |
| 类装饰器 | `class Deco:\n    def __init__(self,func):\n        self.func = func\n    def __call__(self,*a,**kw):\n        return self.func(*a,**kw)` |
| 保留元数据 | `@wraps(func)` 放在 wrapper 上面 |

---

*笔记日期：2026-05-19*
```