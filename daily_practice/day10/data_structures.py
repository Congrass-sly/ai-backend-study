from collections import deque

class Stack:
    """栈：后进先出（LIFO），基于列表实现"""
    
    def __init__(self):
        self.stack = []

    def __str__(self):
        return f"Stack({self.stack})"
    
    def push(self, item):
        """将元素压入栈顶"""
        self.stack.append(item)
    
    def pop(self):
        """弹出栈顶元素并返回"""
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("空栈无法弹出")
    
    def peek(self):
        """查看栈顶元素，不取出"""
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("空栈无栈顶")
    
    def is_empty(self):
        """判断栈是否为空"""
        return len(self.stack) == 0
    
    def size(self):
        """返回栈中元素个数"""
        return len(self.stack)
    
    def __len__(self):
        """支持 len() 函数"""
        return len(self.stack)
    
    def __repr__(self):
        return f"Stack({self.stack})"


class Deque:
    """双端队列：基于 collections.deque 实现，支持两端操作"""
    
    def __init__(self, iterable=None):
        """
        初始化双端队列
        
        参数:
            iterable: 可迭代对象（可选），用于初始化队列
        """
        if iterable:
            self.queue = deque(iterable)
        else:
            self.queue = deque()

    def __str__(self):
        return f"Deque({self.queue})"
    
    # ========== 添加元素 ==========
    
    def append(self, num):
        """右侧添加元素（队尾）"""
        self.queue.append(num)
    
    def appendleft(self, num):
        """左侧添加元素（队首）"""
        self.queue.appendleft(num)
    
    # ========== 移除元素 ==========
    
    def pop(self):
        """右侧弹出元素（队尾）"""
        if not self.queue:
            raise IndexError("空队列无法弹出")
        return self.queue.pop()
    
    def popleft(self):
        """左侧弹出元素（队首）"""
        if not self.queue:
            raise IndexError("空队列无法弹出")
        return self.queue.popleft()
    
    # ========== 查看元素 ==========
    
    def peek_left(self):
        """查看左侧元素（不移除）"""
        if not self.queue:
            return None
        return self.queue[0]
    
    def peek_right(self):
        """查看右侧元素（不移除）"""
        if not self.queue:
            return None
        return self.queue[-1]
    
    def get(self, index):
        """按索引获取元素"""
        try:
            return self.queue[index]
        except IndexError:
            raise IndexError(f"索引 {index} 超出范围")
    
    # ========== 扩展操作 ==========
    
    def extend(self, lst):
        """右侧扩展"""
        self.queue.extend(lst)
    
    def extendleft(self, lst):
        """左侧扩展（注意顺序会反转）"""
        self.queue.extendleft(lst)
    
    # ========== 其他操作 ==========
    
    def rotate(self, num=1):
        """旋转队列（原地操作）"""
        self.queue.rotate(num)
    
    def clear(self):
        """清空队列"""
        self.queue.clear()
    
    # ========== 查看状态 ==========
    
    def is_empty(self):
        """判断是否为空"""
        return len(self.queue) == 0
    
    def size(self):
        """获取队列长度"""
        return len(self.queue)
    
    def __len__(self):
        """支持 len() 函数"""
        return len(self.queue)
    
    def __repr__(self):
        """打印显示"""
        return f"Deque({list(self.queue)})"


# ========== 测试代码 ==========
if __name__ == "__main__":
    # 测试 Stack
    print("=" * 40)
    print("测试 Stack")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"栈: {s}")
    print(f"弹出: {s.pop()}")
    print(f"栈顶: {s.peek()}")
    print(f"大小: {s.size()}")
    
    # 测试 Deque
    print("\n" + "=" * 40)
    print("测试 Deque")
    q = Deque([1, 2, 3])
    print(f"初始: {q}")
    q.append(4)
    q.appendleft(0)
    print(f"添加后: {q}")
    print(f"左侧弹出: {q.popleft()}")
    print(f"右侧弹出: {q.pop()}")
    print(f"最终: {q}")