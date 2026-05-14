```markdown
# 今日学习笔记 - 生成器与迭代器

---

## 一、今天学会的内容

### 1. 迭代器协议

```python
class MyIterator:
    def __iter__(self):
        return self          # 返回迭代器对象本身
    
    def __next__(self):
        # 返回下一个值
        # 结束时抛出 StopIteration
        raise StopIteration
```

| 方法 | 作用 | 触发时机 |
|------|------|---------|
| `__iter__` | 返回迭代器对象 | `for` 循环开始时、`iter()` 调用时 |
| `__next__` | 返回下一个值 | 每次循环、`next()` 调用时 |

**关键点**：
- `StopIteration` 是结束标志（不是错误）
- 迭代器是**一次性**的，遍历完就耗尽

---

### 2. 生成器函数（yield）

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(5):
    print(x)  # 5 4 3 2 1
```

| 对比 | 普通函数 | 生成器函数 |
|------|---------|-----------|
| 返回值 | `return` | `yield` |
| 执行方式 | 一次性执行完 | 每次 `next()` 执行到下一个 `yield` |
| 状态保持 | 不保持 | 自动保持 |

**优势**：
- 自动实现迭代器协议（无需写 `__iter__` 和 `__next__`）
- 自动处理 `StopIteration`
- 代码更简洁

---

### 3. 生成器表达式

```python
# 列表推导式（方括号）
lst = [x * 2 for x in range(10)]

# 生成器表达式（圆括号）
gen = (x * 2 for x in range(10))
```

| 对比 | 列表推导式 | 生成器表达式 |
|------|-----------|-------------|
| 括号 | `[]` | `()` |
| 内存 | 一次性生成全部，O(n) | 惰性生成，O(1) |
| 重复使用 | ✅ 可以 | ❌ 一次性 |
| 随机访问 | ✅ 支持索引 | ❌ 不支持 |
| 语法 | `[表达式 for x in 可迭代]` | `(表达式 for x in 可迭代)` |

**使用建议**：
- 大数据集 → 生成器表达式
- 需要多次遍历 / 随机访问 → 列表推导式

---

### 4. 内存对比

```python
import sys

# 列表：100万元素 → 约8MB
list_count = [x for x in range(1000000)]
print(sys.getsizeof(list_count))  # ~8,000,000 字节

# 生成器：100万元素 → 约120字节（固定）
gen_count = (x for x in range(1000000))
print(sys.getsizeof(gen_count))   # ~120 字节
```

**结论**：生成器内存优势巨大，但只能遍历一次。

---

### 5. 大文件逐行读取

```python
def read_large_file(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as f:
        for line in f:
            yield line

# 使用
for line in read_large_file("big_file.txt"):
    print(line.strip())
```

**优势**：不会一次性加载整个文件到内存。

---

## 二、今天不会的地方（已解决）

| 问题 | 正确理解 |
|------|---------|
| `StopAsyncIteration` vs `StopIteration` | 普通迭代器用 `StopIteration`，异步才用 `StopAsyncIteration` |
| 生成器表达式语法 | 方括号 `[]` 是列表，圆括号 `()` 是生成器 |
| 生成器的一次性特性 | 遍历完就耗尽，再次遍历得到空 |
| 嵌套生成器 | `gen2 = (y*2 for y in gen1)` 从 `gen1` 取值计算 |
| `sys.getsizeof()` 局限性 | 只计算对象本身，不计算内部引用的对象 |

---

## 三、选择指南总结

| 场景 | 推荐 | 原因 |
|------|------|------|
| 无限序列（如斐波那契） | 生成器函数 | 表达式无法表达无限 |
| 逻辑复杂、需异常处理 | 生成器函数 | 可拆分多行，易调试 |
| 简单映射/过滤 | 生成器表达式 | 一行代码，简洁 |
| 需要多次遍历 | 列表 | 生成器一次性 |
| 需要随机访问 | 列表 | 生成器不支持索引 |
| 大数据处理 | 生成器 | 内存优势巨大 |

---

## 四、常见错误提醒

```python
# ❌ 错误1：生成器重复使用
gen = (x for x in range(5))
print(list(gen))  # [0,1,2,3,4]
print(list(gen))  # []（已耗尽）

# ✅ 正确：需要时重新创建
print(list(x for x in range(5)))
print(list(x for x in range(5)))

# ❌ 错误2：迭代器类中用错异常
raise StopAsyncIteration  # 错误

# ✅ 正确
raise StopIteration       # 正确

# ❌ 错误3：生成器表达式括号省略错误
sum(x for x in range(100), 10)  # 错误

# ✅ 正确
sum((x for x in range(100)), 10)
```

---

## 五、记忆口诀

> **迭代器：iter 取对象，next 拿值，StopIteration 结束**
> **生成器函数：yield 返回值，状态自动存，代码更简洁**
> **生成器表达式：括号替方框，惰性省内存，一次就耗尽**
> **大文件逐行读：for line in f，yield 吐出去，内存永不爆**

---

## 六、下一步计划

- [ ] 用生成器实现斐波那契数列
- [ ] 用生成器实现管道处理（多个生成器串联）
- [ ] 学习 `itertools` 模块（无限迭代器工具集）
- [ ] 学习协程（`yield` 接收值，`send()` 方法）

---

*笔记日期：2026-05-14*
