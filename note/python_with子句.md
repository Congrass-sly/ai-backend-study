```markdown
# 上下文管理器完整学习笔记 - 2026-05-20

## 一、with 语句工作原理

`with` 语句本质上是对 `try-finally` 的封装，用于自动管理资源。

```python
# with 语句
with open("test.txt", "r") as f:
    data = f.read()

# 等价的手动实现
mrg = open("test.txt", "r")
f = mrg.__enter__()
try:
    data = f.read()
finally:
    mrg.__exit__(None, None, None)
```

**执行顺序**：
1. 调用 `__enter__()` 获取资源
2. 执行 with 块内的代码
3. 无论是否发生异常，都会调用 `__exit__()` 释放资源

---

## 二、上下文管理器协议

需要实现两个特殊方法：

| 方法 | 触发时机 | 作用 |
|------|---------|------|
| `__enter__(self)` | 进入 with 块时 | 申请资源/准备环境，返回给 `as` 变量 |
| `__exit__(self, exc_type, exc_val, exc_tb)` | 退出 with 块时 | 释放资源/清理环境 |

### `__exit__` 参数详解

```python
def __exit__(self, exc_type, exc_val, exc_tb):
    # exc_type: 异常类型（如 ValueError、TypeError），无异常时为 None
    # exc_val: 异常实例（如 ValueError("错误信息")），无异常时为 None
    # exc_tb: traceback 调用栈信息，无异常时为 None
    return False  # False: 异常继续抛出 / True: 抑制异常
```

### `__exit__` 返回值的作用

| 返回值 | 效果 | 使用场景 |
|--------|------|---------|
| `False`（或不写 return） | 异常继续向上抛出 | 大多数情况 |
| `True` | 异常被抑制，不向外抛出 | 需要自己处理所有异常时 |

**注意**：返回 `True` 会吞掉异常，调用者无法知道发生了错误，一般不推荐。

---

## 三、Timer 计时上下文管理器

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()  # 高精度计时
        return self
    
    def __exit__(self, exc_type, exc, tb):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"耗时：{self.elapsed:.4f} 秒")
        return False

# 使用
with Timer() as t:
    # 要计时的代码
    pass
print(f"耗时：{t.elapsed:.4f} 秒")
```

### `time.perf_counter()` vs `time.time()`

| 函数 | 精度 | 用途 |
|------|------|------|
| `time.time()` | 秒级，可能受系统时间调整影响 | 普通时间获取 |
| `time.perf_counter()` | 纳秒级（高精度），不受系统时间影响 | 性能测试、计时 |

---

## 四、contextlib 常用工具

### 1. @contextmanager 装饰器（生成器写法）

用生成器简化上下文管理器的编写：

```python
from contextlib import contextmanager

@contextmanager
def open_file(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    try:
        yield f      # yield 返回的对象给 as 变量
    finally:
        f.close()    # 无论是否异常，都会执行

# 使用
with open_file('sample.txt') as f:
    print(f.readline())
```

**生成器写法要点**：
- `yield` 之前：相当于 `__enter__`（申请资源）
- `yield` 返回的值：给 `as` 变量
- `yield` 之后（finally）：相当于 `__exit__`（释放资源）
- 异常会回到 `yield` 处，可用 `try-finally` 或 `try-except` 处理

### 2. nullcontext（什么都不做的上下文管理器）

```python
from contextlib import nullcontext

# 什么都不做，只是语法占位
with nullcontext():
    print("正常执行")
```

**使用场景**：条件性需要上下文管理器时，统一语法

```python
from threading import Lock

def process(need_lock):
    lock = Lock() if need_lock else None
    cm = lock if lock else nullcontext()
    
    with cm:
        # need_lock=True 时加锁，False 时什么都不做
        return read_file()
```

### 3. ExitStack（动态管理多个资源）

```python
from contextlib import ExitStack

paths = ['a.txt', 'b.txt', 'c.txt']

with ExitStack() as stack:
    # 动态进入多个上下文（数量在运行时才知道）
    files = [stack.enter_context(open(p, 'r')) for p in paths]
    contents = [f.read() for f in files]
# 退出时按"先进后出"（LIFO）顺序自动关闭
```

**方法**：
| 方法 | 作用 |
|------|------|
| `enter_context(obj)` | 进入上下文，登记退出动作 |
| `callback(func, *args)` | 注册回调函数，退出时执行 |

**退出顺序**：按进入的**相反顺序**（先进后出）清理

```python
with ExitStack() as stack:
    stack.enter_context(open('a.txt'))  # 第1个进入
    stack.enter_context(open('b.txt'))  # 第2个进入
    # 退出时：先关闭 b.txt，再关闭 a.txt
```

### 4. suppress（忽略特定异常）

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    # 文件不存在时不会报错，什么都不发生
    open('not_exist.txt')
```

### 5. closing（包装只有 close 方法的对象）

```python
from contextlib import closing
import urllib.request

with closing(urllib.request.urlopen('http://example.com')) as page:
    content = page.read()
# 自动调用 page.close()
```

---

## 五、contextlib 工具对比

| 工具 | 作用 | 使用场景 |
|------|------|---------|
| `@contextmanager` | 生成器写上下文管理器 | 简化自定义 |
| `nullcontext` | 什么都不做 | 条件性 with |
| `ExitStack` | 管理动态数量资源 | 循环打开文件 |
| `suppress` | 忽略特定异常 | 预期内可忽略的错误 |
| `closing` | 包装 close() 对象 | 网络连接等 |

---

## 六、加锁 vs 不加锁

```python
from threading import Lock

lock = Lock()

# 不加锁（多线程会出问题）
counter += 1

# 加锁（安全）
with lock:
    counter += 1
```

| 对比项 | 不加锁 | 加锁 |
|--------|--------|------|
| 数据安全 | ❌ 可能出错（竞争条件） | ✅ 安全 |
| 执行速度 | 快 | 慢（有获取/释放锁的开销） |
| 适用场景 | 单线程 | 多线程写共享数据 |

### 为什么 `counter += 1` 不安全？

`counter += 1` 实际分三步：
1. 读取 counter 的值
2. 计算 +1
3. 写回 counter

多线程时可能被打断，导致数据错误。

---

## 七、资源自动释放的好处

| 好处 | 说明 |
|------|------|
| 防止资源泄漏 | 无论是否异常，资源都能被释放 |
| 降低心智负担 | 不用手动 try-finally，专注业务逻辑 |
| 统一管理策略 | 文件、锁、数据库用同一套语法 |
| 避免嵌套地狱 | 多个资源可以一行 with 搞定 |

---

## 八、常用代码模板

### 类方式上下文管理器

```python
class MyContext:
    def __enter__(self):
        # 申请资源
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        return False
```

### @contextmanager 方式

```python
@contextmanager
def my_context():
    # 申请资源
    try:
        yield 对象
    finally:
        # 释放资源
```

### 条件性上下文

```python
cm = lock if need_lock else nullcontext()
with cm:
    # 加锁或不加锁
```

### 动态多个资源

```python
with ExitStack() as stack:
    resources = [stack.enter_context(open(p)) for p in paths]
```

---

## 九、面试常见问题

**Q1：`with` 语句和 `try-finally` 有什么区别？**

> `with` 只能用于实现了上下文管理器协议的对象，代码更简洁；`try-finally` 更通用，可用于任何需要清理的场景。

**Q2：`__exit__` 返回 `True` 会怎样？**

> 会抑制异常，异常不会向外抛出，调用者无法感知。

**Q3：`nullcontext` 有什么用？**

> 提供一个"什么都不做"的上下文管理器，用于条件性 with 语句，避免写 if-else 分支。

**Q4：`ExitStack` 什么场景用？**

> 当需要管理的资源数量在运行时才能确定时（比如循环打开多个文件），用 `ExitStack` 统一管理。

**Q5：`@contextmanager` 装饰器如何实现异常处理？**

> 在 `yield` 外使用 `try-finally` 或 `try-except`，异常会回到 `yield` 处。


## 今天犯的错误

### 错误1：ExitStack 忘记加括号

```python
# ❌ 错误
with ExitStack as stack:

# ✅ 正确
with ExitStack() as stack:
```

### 错误2：实例化类时忘记传参数

```python
# ❌ 错误
with DataBaseConnection as dbc:

# ✅ 正确
with DataBaseConnection("test_db") as dbc:
```

### 错误3：把实例当成函数调用

```python
# ❌ 错误
dbc('test.txt')

# ✅ 正确
dbc.query('SELECT * FROM users')
```

### 错误4：`__exit__` 参数不完整

```python
# ❌ 错误
def __exit__(self, exc_type, exc):

# ✅ 正确
def __exit__(self, exc_type, exc_val, exc_tb):
```

### 错误5：`__exit__` 参数名字理解混淆

```python
# exc_type：异常类型（如 ValueError）
# exc_val：异常实例
# exc_tb：traceback 调用栈信息
```

---

*笔记日期：2026-05-20*
```