"""
多线程模拟并发请求（带锁保护输出和计数器，耗时统计放在锁外）
- 演示了如何用 Lock 保证 print 输出不交错且计数器安全
- 观察锁内锁外代码对并发性能的影响
"""

import threading
import time
import random

# ========== 注释掉的部分：早期无锁/粗锁示例 ==========
# Lock = threading.Lock()
# def work(name):
#     for i in range(3):
#         Lock.acquire()
#         print(f'名字：{name}，打印：{i}')
#         Lock.release()
#         time.sleep(0.5)
# threads = []
# for i in range(5):
#     t = threading.Thread(target=work, args=(f'Thread：{i}', ))
#     t.start()
#     print("进入线程")
#     threads.append(t)
# for t in threads:
#     t.join()
# print("退出主线程")
# ==================================================

# 创建一个全局锁，用于保护共享资源（print 和 count）
Lock = threading.Lock()
count = 0          # 统计完成的请求数量

def send_request(threadID):
    """模拟一个请求任务：输出开始和完成（锁内），然后模拟耗时（锁外）"""
    global count
    start = time.time()                     # 记录请求开始时间

    # 临界区：两个 print 和 count 递增被锁保护，保证输出原子性
    with Lock:
        print(f"[线程{threadID}]开始发送请求....")
        print(f"[线程{threadID}]请求完成")   # 注意：“完成”打印在真实处理之前，仅演示锁的用法
        count += 1

    # 模拟耗时操作（如网络IO、计算等）—— 放在锁外，实现真正的并发
    time.sleep(random.uniform(0.1, 0.5))

    end = time.time()                       # 记录结束时间
    print(f"[线程{threadID}],耗时：{end - start:.4f}")

# 创建并启动 10 个线程
threads = []
for i in range(10):
    t = threading.Thread(target=send_request, args=(f'{i}',))
    t.start()
    threads.append(t)

# 等待所有线程执行完毕
for t in threads:
    t.join()

# 输出最终完成的请求数量（应为 10）
print(f"完成的请求数量{count}")
print("退出主线程")

