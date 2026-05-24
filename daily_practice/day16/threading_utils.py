"""
多线程工具模块
提供线程安全计数器、超时执行、生产者-消费者队列封装
"""

import threading
import queue
import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError

class ThreadSafeCounter:
    """线程安全的计数器"""

    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        """增加1，返回新值"""
        with self.lock:
            self.value += 1
        return self.value

    def decrement(self):
        """减少1，返回新值"""
        with self.lock:
            self.value -= 1
        return self.value

    def get_value(self):
        """获取当前值"""
        with self.lock:
            return self.value

def run_with_timeout(func, timeout, args=(), kwargs=None):
    """
    在限定时间内执行函数，超时则返回 None

    参数:
        func: 目标函数
        timeout: 超时秒数
        args: 位置参数元组
        kwargs: 关键字参数字典

    返回:
        函数返回值，超时返回 None
    """
    if kwargs is None:
        kwargs = {}
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(func, *args, **kwargs)
        try:
            return future.result(timeout=timeout)
        except TimeoutError:
            print("函数执行超时")
            return None

class ProducerConsumerQueue:
    """
    生产者-消费者队列封装（使用 queue.Queue）
    """

    def __init__(self, maxsize=0):
        """
        初始化

        参数:
            maxsize: 队列最大容量，0 表示无限
        """
        self.queue = queue.Queue(maxsize)
        self.stop_event = threading.Event()

    def produce(self, items):
        """
        生产者：将一系列项放入队列

        参数:
            items: 可迭代对象
        """
        for item in items:
            if self.stop_event.is_set():
                break
            self.queue.put(item)
            print(f"生产: {item}")
            time.sleep(0.5)

    def consume(self, callback):
        """
        消费者：从队列取出项并调用回调函数

        参数:
            callback: 处理每个项的函数，接收一个参数
        """
        while not self.stop_event.is_set():
            try:
                item = self.queue.get(timeout=1)
                callback(item)
                self.queue.task_done()
            except queue.Empty:
                continue

    def stop(self):
        """停止所有线程"""
        self.stop_event.set()