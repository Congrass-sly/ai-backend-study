```markdown
1.今天学习了：利用threading模块中threading.Thread(target, args=(), kwargs={}, daemon=None)函数来创造线程创建Thread类的实例；
target：线程将要执行的目标函数。
args：目标函数的参数，以元组形式传递（注意单元素元组需加逗号，如 `args=("A",)`）。
kwargs：目标函数的关键字参数，以字典形式传递。
daemon：指定线程是否为守护线程，守护线程在主线程退出时自动终止。
threading模块来创造一个新线程子类包括初始化和run方法，正确写法：
```python
class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__(name=name)   # 只传父类支持的参数（如name, daemon）
        self.delay = delay
    def run(self):
        # 线程执行的内容
```

利用循环来把多线程用join()结束时间，确保主线程等待所有子线程完成。

利用锁来保证线程运行时的数据安全，锁应只保护共享资源的读写，不要把耗时操作放在锁内。

线程优先级队列：`queue.PriorityQueue`，元素为(priority, data)，priority越小优先级越高。

2.今天的错误：
- 目标参数用元组传参时格式错误：忘记单元素元组的逗号 `args=(value,)`。
- 利用super().__init__传承时，记错了父类threading.Thread里的参数，错误传递了`threadID`、`delay`等不支持的参数；正确做法：只传`name`、`daemon`等合法参数。
- 对锁的作用对象有理解偏差：锁应该保护**多个线程共享的变量**（如计数器、队列），而不是把`time.sleep`等模拟操作包在里面，否则导致串行执行。
- 线程优先级队列自己写的时候除了初始化队列以外没有思路，不熟练如何配合多线程消费。

**错误示例（锁内包含耗时操作）**：
```python
lock = threading.Lock()
def worker():
    with lock:
        # 错误：模拟耗时操作放在锁内，导致其他线程必须等待
        time.sleep(1)
        shared_var += 1
```

**错误示例（父类初始化传递非法参数）**：
```python
class BadThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        super().__init__(threadID=threadID, name=name, delay=delay)  # threadID 和 delay 不是合法参数
```

3.还不会的：
- **线程优先级队列的完整实践**：包括如何使用 `PriorityQueue` 结合多线程消费任务，并正确控制线程退出。

**补充学习：优先级队列 + 多线程示例**
```python
import threading
import queue
import time

# 创建优先级队列
pq = queue.PriorityQueue()
stop_event = threading.Event()   # 用于通知线程退出

def worker():
    while not stop_event.is_set():
        try:
            # 等待最多1秒，避免空转
            priority, task = pq.get(timeout=1)
            print(f"{threading.current_thread().name} 处理 {task} (优先级{priority})")
            time.sleep(0.5)           # 模拟处理
            pq.task_done()
        except queue.Empty:
            continue

# 启动工作线程
threads = []
for i in range(3):
    t = threading.Thread(target=worker, name=f"Worker-{i}")
    t.start()
    threads.append(t)

# 放入任务 (优先级越小越优先)
tasks = [(2, "写报告"), (1, "紧急修复"), (3, "日常检查"), (1, "客户投诉")]
for p, task in tasks:
    pq.put((p, task))

# 等待所有任务处理完毕
pq.join()
# 通知线程退出
stop_event.set()
for t in threads:
    t.join()
print("所有任务完成")
```

- **生产者-消费者模式中如何优雅地停止工作线程**：除 `threading.Event` 外，也可用哨兵 `None` 值，每个线程取到 `None` 时退出。

**哨兵方式示例**：
```python
import queue

q = queue.Queue()
STOP = object()

def worker():
    while True:
        item = q.get()
        if item is STOP:
            break
        # 处理任务
        print(item)
        q.task_done()

# 启动线程
t = threading.Thread(target=worker)
t.start()
# 放入任务...
# 最后放入与线程数量相同的 STOP 对象
q.put(STOP)
t.join()
```

**仍不熟练的**：多线程调试技巧、线程池 `ThreadPoolExecutor` 的使用、避免死锁的方法。后续继续练习。
2026/5/22