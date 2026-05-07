# Python 面向对象进阶 - 面试级笔记（含实战错误记录）

## 目录
1. [self 的作用](#1-self-的作用)
2. [私有属性与名称修饰](#2-私有属性与名称修饰)
3. [单下划线与双下划线的区别](#3-单下划线与双下划线的区别)
4. [多态](#4-多态)
5. [鸭子类型](#5-鸭子类型)
6. [方法重写](#6-方法重写)
7. [多继承与 MRO](#7-多继承与-mro)
8. [@property 装饰器](#8-property-装饰器)
9. [继承中的 `__init__` 与 `super()`](#9-继承中的-__init__-与-super)
10. [实战代码及错误记录](#10-实战代码及错误记录)
11. [面试高频问题](#11-面试高频问题)
12. [记忆口诀](#12-记忆口诀)

---

## 1. self 的作用

### 核心理解

```python
class Person:
    def __init__(self, name):
        self.name = name   # self 代表当前正在创建的对象
    
    def greet(self):
        print(f"你好，我是 {self.name}")

p1 = Person("小明")
p2 = Person("小红")
p1.greet()  # self 是 p1
p2.greet()  # self 是 p2
```

### self 的本质

| 问题 | 答案 |
|------|------|
| self 是什么 | 实例对象本身的引用 |
| self 是关键字吗 | **不是**，是约定俗成的参数名 |
| 可以改名吗 | 可以（如 `this`），但**永远不要** |
| 需要手动传参吗 | 不需要，Python 自动传递 |

### ⚠️ 常见错误

```python
# ❌ 错误：方法定义时忘了写 self
class Test:
    def method():  # 缺少 self
        print("hello")

t = Test()
t.method()  # TypeError: method() takes 0 positional arguments but 1 was given

# ✅ 正确
class Test:
    def method(self):
        print("hello")
```

### 面试回答

> self 是实例方法的第一个参数，代表调用该方法的实例对象本身。Python 在调用方法时会自动将实例对象作为第一个参数传入。self 不是关键字，但社区强约定使用这个名字。

---

## 2. 私有属性与名称修饰

### 单下划线 `_var`

```python
class Bank:
    def __init__(self, balance):
        self._balance = balance   # "保护"属性，约定勿直接访问
```

- **作用**：告诉其他开发者"这是内部实现，不要直接使用"
- **Python 是否阻止访问**：❌ 不阻止，全靠自觉

### 双下划线 `__var`（名称修饰 Name Mangling）

```python
class Bank:
    def __init__(self):
        self.__money = 100   # 实际变成 _Bank__money

b = Bank()
print(b.__money)           # ❌ AttributeError
print(b._Bank__money)      # ✅ 100
```

- **作用**：防止子类意外覆盖父类属性
- **Python 是否阻止访问**：❌ 不阻止，但名字变了

### ⚠️ 常见错误

```python
# ❌ 错误：误以为双下划线是完全私有的
class Parent:
    __value = 10

class Child(Parent):
    def show(self):
        print(self.__value)  # AttributeError

# ✅ 正确：通过名称修饰后的名字访问（但不推荐）
print(Child()._Parent__value)  # 10
```

### 名称修饰规则

| 原始名称 | 修饰后名称 |
|---------|-----------|
| `__money` | `_ClassName__money` |
| `__value` | `_ClassName__value` |

**注意**：`__init__`、`__str__` 等特殊方法不会被修饰。

---

## 3. 单下划线与双下划线的区别

| 特性 | `_var` | `__var` |
|------|--------|---------|
| 名称 | 单下划线 | 双下划线 |
| 作用 | 约定"保护" | 名称修饰（伪私有） |
| Python 是否阻止访问 | ❌ 不阻止 | ❌ 不阻止（但名字变了） |
| 外部直接访问 | ✅ 可以 | ❌ 需要知道修饰后的名字 |
| 子类同名会覆盖吗 | ✅ 会 | ❌ 不会 |
| 本质 | 程序员之间的约定 | Python 语法特性 |

### 面试回答

> Python 没有真正的私有属性。单下划线 `_var` 是约定，表示"保护"属性，外部不应直接访问。双下划线 `__var` 会触发名称修饰，Python 将其改名为 `_ClassName__var`，主要目的是防止子类意外覆盖。

---

## 4. 多态

### 定义

**同一个方法名，在不同对象中有不同的行为。**

### 继承多态

```python
class Animal:
    def sound(self):
        return "动物叫声"

class Dog(Animal):
    def sound(self):
        return "汪汪"

class Cat(Animal):
    def sound(self):
        return "喵喵"

def make_sound(animal):
    print(animal.sound())

make_sound(Dog())  # 汪汪
make_sound(Cat())  # 喵喵
```

### 好处

- **开闭原则**：对扩展开放，对修改关闭
- 函数只需依赖父类类型，新增子类无需修改函数

---

## 5. 鸭子类型

### 核心思想

> "如果它走起来像鸭子，叫起来像鸭子，那它就是鸭子"

**不关心对象类型，只关心它有没有需要的方法。**

```python
class Bird:
    def fly(self):
        return "鸟在飞"

class Airplane:
    def fly(self):
        return "飞机在飞"

def take_off(obj):
    print(obj.fly())   # 不关心类型，只关心有没有 fly 方法

take_off(Bird())      # 鸟在飞
take_off(Airplane())  # 飞机在飞
```

### 多态 vs 鸭子类型

| 类型 | 说明 | 是否需要继承 |
|------|------|-------------|
| 继承多态 | 子类重写父类方法 | ✅ 需要 |
| 鸭子类型 | 只要对象有同名方法即可 | ❌ 不需要 |

---

## 6. 方法重写

### 基本语法

```python
class Parent:
    def greet(self):
        return "父类问候"

class Child(Parent):
    def greet(self):           # 重写父类方法
        return "子类问候"

c = Child()
print(c.greet())  # 子类问候
```

### 重写中调用父类方法

```python
class Child(Parent):
    def greet(self):
        parent_msg = super().greet()  # 调用父类
        return f"{parent_msg} + 子类问候"
```

### ⚠️ 常见错误：重写时参数写死

```python
# ❌ 错误：忽略了传入的参数
def sorted_numbers(self, reverse=False):
    return sorted(self.numbers, reverse=False)  # 写死了 False

# ✅ 正确：使用传入的参数
def sorted_numbers(self, reverse=False):
    return sorted(self.numbers, reverse=reverse)
```

### 参数扩展（重写时增加参数）

```python
class Parent:
    def filter(self, data):
        return [x for x in data if x > 0]

class Child(Parent):
    def filter(self, data, threshold=0):  # 增加默认参数
        return [x for x in data if x > threshold]
```

---

## 7. 多继承与 MRO

### 基本语法

```python
class Father:
    pass

class Mother:
    pass

class Child(Father, Mother):  # 多继承
    pass
```

### MRO（方法解析顺序）

Python 使用 **C3 线性化算法** 确定方法查找顺序。

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

### 菱形继承

```python
class A:
    def test(self):
        print("A")

class B(A):
    def test(self):
        print("B")
        super().test()

class C(A):
    def test(self):
        print("C")
        super().test()

class D(B, C):
    pass

d = D()
d.test()
# 输出：
# B
# C
# A
```

### MRO 规则

| 规则 | 说明 |
|------|------|
| 子类优先 | 子类在父类前面 |
| 左优先 | 左边父类的链先于右边 |
| 不重复 | 每个类只出现一次 |
| `super()` | 按 MRO 顺序调用下一个 |

---

## 8. @property 装饰器

### 基本用法

```python
class Student:
    def __init__(self, score):
        self._score = score
    
    @property
    def score(self):           # getter
        return self._score
    
    @score.setter
    def score(self, value):    # setter
        if 0 <= value <= 100:
            self._score = value
        else:
            raise ValueError("分数必须在0-100之间")

s = Student(60)
print(s.score)   # 像属性一样访问
s.score = 95     # 像属性一样赋值
```

### 只读属性

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def area(self):
        return 3.14 * self._radius ** 2
    # 没有 setter，不能赋值

c = Circle(5)
print(c.area)   # 78.5
# c.area = 100  # ❌ AttributeError
```

### 装饰器总结

| 装饰器 | 作用 | 触发时机 |
|--------|------|---------|
| `@property` | 方法变属性 | 读取属性时 |
| `@xxx.setter` | 设置属性值 | 赋值时 |
| `@xxx.deleter` | 删除属性时触发 | `del` 时 |

---

## 9. 继承中的 `__init__` 与 `super()`

### 子类不重写 `__init__`

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    pass

c = Child("小明")  # 自动调用父类的 __init__
```

### 子类重写 `__init__`

```python
class Child(Parent):
    def __init__(self, name, grade):
        super().__init__(name)  # 必须手动调用父类
        self.grade = grade
```

### `super()` 的好处

| 方式 | 代码 | 问题 |
|------|------|------|
| 硬编码父类名 | `Parent.__init__(self, name)` | 多继承时可能重复调用 |
| `super()` | `super().__init__(name)` | 自动处理 MRO，避免重复 |

### ⚠️ 常见错误：调用父类方法时多余传参

```python
# ❌ 错误：mean_numbers 不需要参数，却传了 self.numbers
mean_val = self.mean_numbers(self.numbers)

# ✅ 正确：实例方法内部直接用 self 获取数据
mean_val = self.mean_numbers()
```

---

## 10. 实战代码及错误记录

### `AdvancedProcessor` 完整代码（含错误记录）

```python
"""
AdvancedProcessor 类 - DataProcessor 的子类
功能：扩展了统计分析、数据清洗、排序过滤等功能
"""

from data_processor import DataProcessor


class AdvancedProcessor(DataProcessor):
    """高级数据处理器，继承自 DataProcessor"""
    
    def __init__(self, file_name=None, numbers=None, write_data=""):
        """
        初始化方法，兼容两种传参方式
        
        【错误记录1】最初忘记调用 super()，导致父类属性未初始化
        【错误记录2】super() 调用时参数顺序写错
        【错误记录3】没有处理 file_name 和 numbers 的互斥关系
        """
        # 调用父类初始化
        super().__init__(
            numbers=numbers if numbers is not None else [],
            file_name=file_name,
            write_data=write_data
        )
        
        # 如果提供了文件名但没有提供数字列表，从文件加载
        if file_name is not None and numbers is None:
            self.numbers = self._load_numbers()
        
        # 新增私有属性：标记文件是否已被处理
        self.__processed = False
    
    def open_file(self):
        """
        重写 open_file 方法
        
        【错误记录】最初忘记调用父类方法，直接自己实现了
        """
        result = super().open_file()  # 调用父类的 open_file
        self.__processed = True       # 标记为已处理
        return result
    
    def is_processed(self):
        """检查文件是否已被处理"""
        return self.__processed
    
    def _load_numbers(self):
        """
        私有方法：从文件加载数字
        
        【错误记录1】忘了加 self 参数
        【错误记录2】没有处理空行，int("") 会报错
        【错误记录3】没有处理文件不存在的情况
        """
        try:
            with open(self.file_name, 'r', encoding='utf-8') as f:
                # line.strip() 去除换行符和空白，if line.strip() 过滤空行
                return [int(line.strip()) for line in f if line.strip()]
        except FileNotFoundError:
            print("文件不存在！")
            return []
    
    def median(self):
        """
        计算中位数
        
        【错误记录1】偶数长度时索引算错：写了 n//2 + 1
        【错误记录2】忘记排序
        【错误记录3】空列表没有处理
        """
        if not self.numbers:
            return 0
        sorted_list = sorted(self.numbers)
        n = len(sorted_list)
        if n % 2 == 0:
            # 偶数长度：中间两个数的平均值
            # 错误：最初写成 (sorted_list[n//2 - 1] + sorted_list[n//2 + 1]) / 2
            return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
        else:
            # 奇数长度：中间那个数
            return sorted_list[n // 2]
    
    def std_dev(self):
        """
        计算标准差
        
        【错误记录1】变量 sum_squared_diff 忘记初始化
        【错误记录2】调用父类 mean_numbers 时错误地传了参数
        【错误记录3】空列表返回 []，与其他方法不一致，后改为 0.0
        """
        if not self.numbers:
            return 0.0
        
        n = len(self.numbers)
        # 错误：最初写成 self.mean_numbers(self.numbers)
        mean_val = self.mean_numbers()  # 复用父类方法
        
        sum_squared_diff = 0  # 错误：最初忘记初始化
        for x in self.numbers:
            sum_squared_diff += (x - mean_val) ** 2
        
        variance = sum_squared_diff / n
        std_deviation = variance ** 0.5
        return std_deviation
    
    def count_above(self, threshold):
        """
        统计大于阈值的元素个数
        
        【错误记录】最初返回的是过滤后的列表，不是个数
        """
        if not self.numbers:
            return 0
        # 错误：最初写的是 return [x for x in self.numbers if x > threshold]
        return len([x for x in self.numbers if x > threshold])
    
    def unique(self):
        """
        列表去重（保持原顺序）
        
        【错误记录】最初用 set()，不保证顺序
        """
        if not self.numbers:
            return []
        # dict.fromkeys() 保持插入顺序（Python 3.7+）
        return list(dict.fromkeys(self.numbers))
    
    def sorted_numbers(self, reverse=False):
        """
        排序列表
        
        【错误记录】参数 reverse 写死为 False，忽略了传入的值
        """
        if not self.numbers:
            return []
        # 错误：最初写成 sorted(self.numbers, reverse=False)
        return sorted(self.numbers, reverse=reverse)
    
    def filter_numbers(self, filter_func=None):
        """
        过滤数字列表（重写父类方法）
        
        【错误记录1】没有处理 filter_func 为 None 的情况
        【错误记录2】默认行为是 x>0，漏了 0，应该是 x>=0
        """
        if not self.numbers:
            return []
        
        if filter_func is None:
            # 错误：最初写成 x > 0，应该是 x >= 0
            return [x for x in self.numbers if x >= 0]
        else:
            return list(filter(filter_func, self.numbers))


# ========== 测试代码 ==========
if __name__ == "__main__":
    # 测试1：从文件读取数字
    print("=" * 40)
    print("测试1：从文件读取")
    ap = AdvancedProcessor("num.txt")
    print(f"中位数：{ap.median():.2f}")
    print(f"标准差：{ap.std_dev():.2f}")
    
    # 测试2：直接传入数字列表
    print("\n" + "=" * 40)
    print("测试2：直接传入列表")
    ap2 = AdvancedProcessor(numbers=[-1, -5, 0, 4, 3])
    print(f"原始数据: {ap2.numbers}")
    print(f"中位数: {ap2.median():.2f}")
    print(f"标准差: {ap2.std_dev():.2f}")
    print(f"大于3的个数: {ap2.count_above(3)}")
    print(f"去重: {ap2.unique()}")
    print(f"降序排序: {ap2.sorted_numbers(reverse=True)}")
    print(f"默认过滤(>=0): {ap2.filter_numbers()}")
    print(f"自定义过滤(偶数): {ap2.filter_numbers(lambda x: x % 2 == 0)}")
```

### 实战错误汇总表

| 错误类型 | 错误代码 | 正确写法 | 出现位置 |
|---------|---------|---------|---------|
| 忘记 `super()` | 直接写 `self.numbers = ...` | `super().__init__(...)` | `__init__` |
| 索引计算错误 | `n//2 + 1` | `n//2` | `median` |
| 变量未初始化 | `sum_squared_diff += ...` | `sum_squared_diff = 0` | `std_dev` |
| 多余传参 | `self.mean_numbers(self.numbers)` | `self.mean_numbers()` | `std_dev` |
| 参数写死 | `reverse=False` | `reverse=reverse` | `sorted_numbers` |
| 忘记调用父类 | 自己实现全部 | `super().open_file()` | `open_file` |
| 返回值类型不一致 | 空列表返回 `[]` | 返回 `0.0` | `std_dev` |
| 边界条件漏处理 | `x > 0` | `x >= 0` | `filter_numbers` |

---

## 11. 面试高频问题

### Q1：Python 如何实现私有属性？

> Python 没有真正的私有属性。通过双下划线 `__var` 触发名称修饰，将属性名改为 `_ClassName__var`，防止子类意外覆盖。仍然可以通过修饰后的名字访问。

### Q2：`self` 是什么？可以改名吗？

> `self` 是实例方法的第一个参数，代表调用该方法的实例对象本身。可以改名（如 `this`），但强约定使用 `self`。

### Q3：单下划线和双下划线有什么区别？

> 单下划线 `_var` 是约定，表示"保护"，不强制。双下划线 `__var` 触发名称修饰，实现"伪私有"。

### Q4：什么是 MRO？

> MRO 是方法解析顺序，Python 用 C3 线性化算法确定多继承时方法的查找顺序。可以通过 `类.__mro__` 查看。

### Q5：`super()` 的作用是什么？

> `super()` 返回 MRO 中的下一个类，用于调用父类方法，避免硬编码父类名，在多继承时能正确按 MRO 顺序调用。

### Q6：`@property` 的作用是什么？

> 将方法变成属性调用，可以在获取和设置时添加逻辑（如验证、计算），同时保持属性调用的简洁语法。

### Q7：多态和鸭子类型有什么区别？

> 多态指同一方法在不同对象中有不同行为；鸭子类型是动态语言的特性，不关心对象类型，只关心它是否有需要的方法。鸭子类型是多态的一种实现方式。

### Q8：重写方法时如何调用父类方法？

> 使用 `super().方法名()` 调用，避免硬编码父类名，在多继承时能正确按 MRO 顺序调用。

### Q9：为什么 `self.mean_numbers()` 不需要传参？

> 实例方法的第一个参数 `self` 已经代表当前对象，数据存储在 `self.numbers` 中，方法内部可以直接访问，不需要额外传参。

---

## 12. 记忆口诀

| 概念 | 口诀 |
|------|------|
| self | 谁调用我，我就是谁 |
| 单下划线 | 君子协议，外人勿碰 |
| 双下划线 | 名称修饰，防子覆盖 |
| 多态 | 同一方法，不同表现 |
| 鸭子类型 | 像鸭就是鸭，不管它爸妈 |
| MRO | 左父优先，子前父后，super 按序走 |
| @property | 方法穿马甲，看起来像属性 |
| super() | 别把父名写硬，MRO 帮我认定 |
| 重写方法 | 参数莫写死，super 要调用 |

---

## 13. 代码速查卡片

```python
# 属性类型
class Demo:
    public = "公开"
    _protected = "保护（约定）"
    __private = "私有（名称修饰）"

# 多态
class Dog: def sound(self): return "汪汪"
class Cat: def sound(self): return "喵喵"

def make_sound(obj): print(obj.sound())

# @property
class Circle:
    @property
    def area(self): return 3.14 * self.r ** 2

# 继承与 super
class Child(Parent):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

# 查看 MRO
print(Child.__mro__)

# 重写时使用参数
def sorted_numbers(self, reverse=False):
    return sorted(self.numbers, reverse=reverse)  # 不要写死
```

---

*最后更新: 2026-05-07*
