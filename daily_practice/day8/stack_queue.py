class Stack:
    """栈：后进先出（LIFO）"""
    def __init__(self):
        self.stack = []

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


class Queue:
    """队列：先进先出（FIFO）"""
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """将元素加入队尾"""
        self.queue.append(item)

    def is_empty(self):
        """判断队列是否为空"""
        return len(self.queue) == 0

    def dequeue(self):
        """取出队首元素并返回"""
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("空队列无法弹出")

    def peek(self):
        """查看队首元素，不取出"""
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("空队列没有队首")

    def size(self):
        """返回队列中元素个数"""
        return len(self.queue)


# 测试栈
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(f"弹出最后一个进栈的元素：{s.pop()}")    # 3
print(f"栈顶元素：{s.peek()}")   # 2
print(f"栈中元素个数：{s.size()}")   # 2

# 测试队列
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(f"取出队首元素：{q.dequeue()}")  # 1
print(f"队首元素：{q.peek()}")     # 2
print(f"队列中元素个数：{q.size()}")     # 2
