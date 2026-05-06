```markdown
# Python 类与对象 - 面试级笔记（完整版）

## 目录
1. [类和对象的基本概念](#1-类和对象的基本概念)
2. [构造方法 `__init__`](#2-构造方法-__init__)
3. [实例属性](#3-实例属性)
4. [实例方法](#4-实例方法)
5. [self 的作用](#5-self-的作用)
6. [类与函数的区别](#6-类与函数的区别)  <!-- 新增 -->
7. [面试常见问题](#7-面试常见问题)
8. [记忆口诀](#8-记忆口诀)
9. [代码模板速查](#9-代码模板速查)

---

## 1. 类和对象的基本概念

### 核心定义

| 概念 | 定义 | 生活类比 |
|------|------|---------|
| **类 (Class)** | 模板、蓝图、设计图 | 做月饼的模具 |
| **对象 (Object)** | 根据类创建出来的具体实例 | 用模具做出来的月饼 |
| **实例化** | 从类创建对象的过程 | 用模具做出月饼的动作 |

### 代码示例

```python
class Dog:
    """类：狗的模板"""
    pass

# 实例化：根据类创建对象
dog1 = Dog()  # 对象1
dog2 = Dog()  # 对象2

print(type(dog1))  # <class '__main__.Dog'>
print(dog1 is dog2)  # False（两个不同的对象）
```

### 关键理解

- 类只有一个，对象可以有无数个
- 对象会占用内存空间，类不直接占用（只是定义）
- 类定义的是**共同特征**，对象拥有的是**具体值**

---

## 2. 构造方法 `__init__`

### 定义和作用

```python
class Student:
    def __init__(self, name, age):
        """构造方法：创建对象时自动执行"""
        self.name = name
        self.age = age
```

| 特性 | 说明 |
|------|------|
| 触发时机 | 创建对象时**自动调用**，不需要手动调用 |
| 主要用途 | 初始化对象的实例属性 |
| 返回值 | 不能返回任何值（返回 None） |
| 名称固定 | 必须是 `__init__`（双下划线开头和结尾） |

### 执行流程详解

```python
class Person:
    def __init__(self, name):
        print(f"__init__ 被调用，参数是 {name}")
        self.name = name

# 下面这行代码做了两件事：
# 1. 创建了一个 Person 对象（分配内存）
# 2. 自动调用 __init__ 方法，传入 "小明"
p = Person("小明")

# 输出：__init__ 被调用，参数是 小明
```

### 面试点：`__init__` 不是构造函数

```python
# Python 中真正的构造函数是 __new__
# __init__ 是初始化方法，不是构造方法

class Test:
    def __new__(cls, *args, **kwargs):
        print("__new__ 被调用：创建对象")
        return super().__new__(cls)
    
    def __init__(self, value):
        print("__init__ 被调用：初始化对象")
        self.value = value

# 执行顺序：__new__ → __init__
t = Test(100)
# 输出：
# __new__ 被调用：创建对象
# __init__ 被调用：初始化对象
```

**面试回答：** `__init__` 是初始化方法，在对象创建后执行，用来设置初始状态。真正的构造函数是 `__new__`。

---

## 3. 实例属性

### 定义和特点

```python
class Student:
    def __init__(self, name, score):
        self.name = name      # 实例属性
        self.score = score    # 实例属性
```

| 特点 | 说明 |
|------|------|
| 归属 | 属于**单个对象**，每个对象独立 |
| 访问方式 | 通过 `self.属性名` 或 `对象名.属性名` |
| 生命周期 | 跟随对象，对象销毁时属性随之消失 |

### 实例属性 vs 类属性

```python
class Dog:
    species = "犬科"  # 类属性（所有实例共享）
    
    def __init__(self, name):
        self.name = name  # 实例属性（每个实例独立）

d1 = Dog("旺财")
d2 = Dog("小黑")

print(d1.species)  # 犬科
print(d2.species)  # 犬科（同一个值）

print(d1.name)  # 旺财
print(d2.name)  # 小黑（不同的值）

# 修改类属性会影响所有实例
Dog.species = "哺乳动物"
print(d1.species)  # 哺乳动物（受影响）
```

### 面试点：实例属性的查找顺序

```python
class Test:
    value = 10  # 类属性
    
    def __init__(self):
        self.value = 20  # 实例属性

t = Test()
print(t.value)  # 20（优先找到实例属性）

# 访问规则：实例属性 > 类属性
```

**查找顺序：** 对象先找自己的实例属性，找不到才去类里找。

---

## 4. 实例方法

### 定义和调用

```python
class Calculator:
    def __init__(self, name):
        self.name = name
    
    def add(self, x, y):
        """实例方法：第一个参数必须是 self"""
        return x + y
    
    def greet(self):
        return f"我是计算器 {self.name}"

# 调用方式1：通过对象
calc = Calculator("小明计算器")
print(calc.add(3, 5))  # 8

# 调用方式2：通过类（不推荐，需要手动传 self）
print(Calculator.add(calc, 3, 5))  # 8
```

### 实例方法的特征

| 特征 | 说明 |
|------|------|
| 第一个参数 | 必须是 `self`（代表实例本身） |
| 调用方式 | 通常通过对象调用 `obj.method()` |
| 访问权限 | 可以通过 `self` 访问实例属性和其他实例方法 |

### 三种方法对比

```python
class Example:
    class_attr = "类属性"
    
    def __init__(self, value):
        self.value = value  # 实例属性
    
    def instance_method(self):
        """实例方法：需要 self，能访问实例属性和类属性"""
        return f"实例属性: {self.value}, 类属性: {self.class_attr}"
    
    @classmethod
    def class_method(cls):
        """类方法：需要 cls，只能访问类属性"""
        return f"类属性: {cls.class_attr}"
    
    @staticmethod
    def static_method(x, y):
        """静态方法：不需要 self/cls，相当于普通函数"""
        return x + y
```

| 方法类型 | 装饰器 | 第一参数 | 能否访问实例属性 | 调用方式 |
|---------|--------|---------|----------------|---------|
| 实例方法 | 无 | `self` | ✅ | `obj.method()` |
| 类方法 | `@classmethod` | `cls` | ❌ | `cls.method()` 或 `obj.method()` |
| 静态方法 | `@staticmethod` | 无 | ❌ | 两种都可以 |

---

## 5. self 的作用

### 核心理解

```python
class Person:
    def __init__(self, name):
        self.name = name  # self 代表"当前正在创建的对象"
    
    def say_hello(self):
        print(f"你好，我是 {self.name}")

p1 = Person("小明")
p2 = Person("小红")

p1.say_hello()  # 你好，我是小明（self 是 p1）
p2.say_hello()  # 你好，我是小红（self 是 p2）
```

### self 的本质

| 问题 | 答案 |
|------|------|
| self 是什么 | 实例对象本身的引用 |
| self 是关键字吗 | **不是**，是约定俗成的参数名（可以用其他名字，但千万别改） |
| self 需要手动传参吗 | **不需要**，Python 自动传递 |
| self 的作用域 | 只存在于实例方法内部，用于区分"谁的属性/方法" |

### 验证 self 的真实身份

```python
class Test:
    def method(self):
        print(f"self 的内存地址: {id(self)}")

t = Test()
print(f"t 的内存地址: {id(t)}")
t.method()
# 输出相同的地址，证明 self 就是 t
```

### 面试陷阱：self 不是必须叫 self

```python
# 下面代码语法正确，但强烈不推荐
class Wrong:
    def say_hello(this, name):  # 把 self 改成 this
        print(f"你好，{name}")

# 建议：永远使用 self，这是 Python 社区的通用规范
```

---

## 6. 类与函数的区别

### 核心区别表

| 对比项 | 函数 | 类 |
|--------|------|-----|
| **定位** | 解决一个具体问题 | 描述一类事物的模板 |
| **返回值** | 必须用 `return` 返回（或隐式返回 None） | 返回一个对象（实例） |
| **数据存储** | 调用结束局部变量销毁 | 对象可以长期保存数据（实例属性） |
| **代码复用** | 直接调用 | 先实例化，再调用方法 |
| **状态** | 无状态（每次调用独立） | 有状态（属性在多次方法调用间保持） |
| **作用域** | 函数执行完毕，内部变量消失 | 对象存活期间，属性一直存在 |

### 代码对比：函数 vs 类

```python
# ========== 函数方式 ==========
def calculate_area(radius):
    """计算圆面积：函数每次传入半径，返回结果"""
    pi = 3.14
    area = pi * radius ** 2
    return area

# 每次调用都要传参数，无法保存状态
print(calculate_area(5))  # 78.5
print(calculate_area(6))  # 113.04

# ========== 类方式 ==========
class Circle:
    """圆类：可以保存半径，多次计算不同属性"""
    
    def __init__(self, radius):
        self.radius = radius  # 状态被保存
        self.pi = 3.14
    
    def get_area(self):
        """计算面积"""
        return self.pi * self.radius ** 2
    
    def get_circumference(self):
        """计算周长"""
        return 2 * self.pi * self.radius

# 一次传入半径，可以反复使用
c = Circle(5)
print(c.get_area())           # 78.5
print(c.get_circumference())  # 31.4（不需要再传半径）
print(c.get_area())           # 78.5（第二次调用，半径还在）
```

### 关键区别详解

#### 区别1：状态保持能力

```python
# 函数：无状态
def counter_func():
    count = 0
    count += 1
    return count

print(counter_func())  # 1
print(counter_func())  # 1（每次都从0开始）

# 类：有状态
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count

c = Counter()
print(c.increment())  # 1
print(c.increment())  # 2（状态被保留）
```

#### 区别2：数据封装

```python
# 函数：数据和处理分离
def deposit(balance, amount):
    return balance + amount

balance = 100
balance = deposit(balance, 50)  # 必须手动传递和接收

# 类：数据和处理绑定在一起
class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount  # 直接修改自己的状态

acc = Account(100)
acc.deposit(50)  # 不需要返回值，不需要重新赋值
print(acc.balance)  # 150
```

#### 区别3：多个独立实例

```python
# 函数：每次都要传所有数据
def describe_person(name, age, city):
    return f"{name},{age},{city}"

print(describe_person("小明", 18, "北京"))
print(describe_person("小红", 20, "上海"))

# 类：每个对象携带自己的数据
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def describe(self):
        return f"{self.name},{self.age},{self.city}"

p1 = Person("小明", 18, "北京")
p2 = Person("小红", 20, "上海")
print(p1.describe())
print(p2.describe())
```

### 函数的特殊形式（与类相关）

```python
# 1. 类中的函数称为"方法"
class MyClass:
    def instance_method(self):   # 实例方法
        pass
    
    @classmethod
    def class_method(cls):       # 类方法
        pass
    
    @staticmethod
    def static_method():         # 静态方法（最接近普通函数）
        pass

# 2. 普通函数
def normal_function():
    pass
```

| 类型 | 定义位置 | 是否属于类 | 能否访问实例属性 |
|------|---------|-----------|----------------|
| 普通函数 | 模块顶层 | ❌ | ❌ |
| 实例方法 | 类内部 | ✅ | ✅ |
| 类方法 | 类内部 | ✅ | ❌ |
| 静态方法 | 类内部 | ✅ | ❌ |

### 何时用函数，何时用类？

| 场景 | 推荐 | 原因 |
|------|------|------|
| 输入 → 输出，无副作用 | **函数** | 简单直接 |
| 需要在多次调用间记住数据 | **类** | 用实例属性保存状态 |
| 需要创建多个相似对象 | **类** | 用同一个模板 |
| 纯工具方法，不依赖状态 | **函数** 或 **静态方法** | 不需要实例化 |
| 需要封装数据和操作 | **类** | 面向对象的核心优势 |

### 一句话总结

> **函数是做一件事的工具，类是一类事物的模板。函数无状态，类有状态；函数用完即毁，类可以长期存活。**

---

## 7. 面试常见问题

### Q1：类变量和实例变量的区别？

| 对比项 | 类变量 | 实例变量 |
|--------|--------|---------|
| 定义位置 | 直接在类下 | `__init__` 中用 `self.xxx` |
| 归属 | 类本身 | 每个对象独立 |
| 修改方式 | `ClassName.var = new_value` | `self.var = new_value` |
| 内存占用 | 一份 | 每个对象一份 |

### Q2：`self` 可以省略吗？

**不能。** 实例方法的第一个参数必须接收实例本身，如果省略，方法就无法访问实例属性。

```python
class Test:
    def method():  # ❌ 缺少 self
        print("hello")

t = Test()
t.method()  # TypeError: method() takes 0 positional arguments but 1 was given
```

### Q3：`__init__` 可以返回值吗？

**不能。** 如果 `__init__` 返回非 None 的值，会抛出 `TypeError`。

```python
class Test:
    def __init__(self):
        return 100  # ❌ TypeError: __init__() should return None

# 正确：不写 return，或 return None
```

### Q4：为什么实例方法的第一个参数叫 self？

这是**社区约定**，不是语法要求。用 `self` 是所有 Python 程序员都遵循的规范，提高代码可读性。

### Q5：如何让一个属性不被外部直接访问？

使用单下划线 `_name`（约定私有）或双下划线 `__name`（名称修饰）。

```python
class Account:
    def __init__(self, balance):
        self._balance = balance    # 约定私有
        self.__password = "123"    # 名称修饰（变成 _Account__password）
```

### Q6：什么时候用函数，什么时候用类？

| 场景 | 推荐 |
|------|------|
| 纯计算，无状态 | 函数 |
| 需要保存多次调用间的数据 | 类 |
| 需要创建多个相似对象 | 类 |
| 工具方法集合 | 静态方法或普通函数 |

---

## 8. 记忆口诀

| 概念 | 口诀 |
|------|------|
| 类和对象 | 类是模具，对象是产品，一个模具无数产品 |
| `__init__` | 对象出生时，自动来报到，初始化属性，不能乱返回 |
| 实例属性 | 十个手指十个样，每个对象自己藏 |
| 实例方法 | 函数放类里，self 当第一，调用用对象，自动传自己 |
| self | 自家人不认生，谁调用我我就是谁 |
| 函数 vs 类 | 函数是一次性工具，类是可复用的模板 |

---

## 9. 代码模板速查

```python
# 类的基本结构（面试手写用）
class ClassName:
    """类文档字符串"""
    
    class_attr = "类属性"
    
    def __init__(self, param1, param2):
        """初始化方法"""
        self.instance_attr1 = param1
        self.instance_attr2 = param2
    
    def instance_method(self):
        """实例方法"""
        return f"操作 {self.instance_attr1}"
    
    @classmethod
    def class_method(cls):
        """类方法"""
        return f"操作 {cls.class_attr}"
    
    @staticmethod
    def static_method(x, y):
        """静态方法"""
        return x + y

# 普通函数模板
def normal_function(param1, param2):
    """普通函数：无状态，输入输出"""
    result = param1 + param2
    return result
```
