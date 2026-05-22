"""
生产者-消费者模式示例（多线程队列）
- 工作线程从队列中获取任务并处理
- 队列自动处理线程安全
- 使用 timeout 让线程在队列空时自动退出
"""

import queue
import threading
import time

# 创建一个容量为20的队列（任务缓冲区）
workQueue = queue.Queue(20)

# 用于存放所有工作线程对象的列表
threads = []

def worker():
    """
    工作线程的主函数
    持续从队列中获取任务，直到队列空且超时
    """
    while True:
        try:
            # 从队列中获取一个任务，最多等待2秒
            # 如果2秒内队列仍为空，抛出 queue.Empty 异常
            task = workQueue.get(timeout=2)
        except queue.Empty:
            # 队列已空且无新任务，退出循环，结束线程
            break
        # 处理任务（模拟业务逻辑）
        print(f"{threading.current_thread().name}正在处理{task}")
        # 模拟耗时操作
        time.sleep(0.5)
        # 通知队列该任务已完成（内部计数器减1）
        workQueue.task_done()

# 创建工作线程数量
num_workers = 3
for i in range(num_workers):
    # 创建线程，指定目标函数和线程名称
    t = threading.Thread(target=worker, name=f'Worker-{i + 1}')
    t.start()          # 启动线程
    threads.append(t)  # 保存线程对象，以便后续 join

# 主线程向队列中放入 20 个任务
for i in range(20):
    workQueue.put(f"task{i + 1}")

# 等待队列中所有任务都被处理完毕（即每个 task_done 都被调用）
workQueue.join()

# 等待所有工作线程正常退出（此时线程已因超时退出，但仍需 join 确保资源回收）
for t in threads:
    t.join()

print("所有任务处理完毕")