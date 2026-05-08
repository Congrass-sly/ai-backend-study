from stack_queue import Stack, Queue
from counter_demo import count_word_frequency, display_result

    # 测试1：直接文本
text = "Hello world! hello python. Hello WORLD"
result = count_word_frequency(text)
display_result(result)

    #测试2：文件
result2 = count_word_frequency('daily_practice/day8/sample.txt')
display_result(result2)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(f"弹出最后一个进栈的元素：{s.pop()}")    # 3
print(f"栈顶元素：{s.peek()}")   # 2  # 2
print(f"栈的尺寸：{s.size()}")   # 2

# 测试队列
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(f"弹出第一个进队列的元素：{q.dequeue()}")  # 1
print(f"队列的顶部元素：{q.peek()}")     # 2
print(f"队列的尺寸{q.size()}")     # 2