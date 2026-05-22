import _thread
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{threadName}：{time.ctime(time.time())}")


# try:
#     _thread.start_new_thread(print_time, ('Thread-1', 2,))
#     _thread.start_new_thread(print_time, ('Thread-2', 4,))

# except:
#     print("Error：无法启动线程")

import threading

try:
    t1 = threading.Thread(target=print_time, args=('Thread-1', 2))                             
    t2 = threading.Thread(target=print_time, args=('Thread-2', 4))
except:
    print("Error：启动线程失败")

# t1.start()
# t2.start()
# t1.join()
# t2.join()

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        super().__init__(name = name)
        self.threadID = threadID
        self.delay = delay

    def run(self):
        print(f"开始线程：{self.name}")
        #获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.delay, 5)
        threadLock.release()
        print("退出线程")

threadLock = threading.Lock()
threads = []

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print(f"{threadName}：{time.ctime(time.time())}")
        counter -= 1

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# # 开启新线程
# thread1.start()
# thread2.start()
# threads.append(thread1)
# threads.append(thread2)
# for t in threads:
#     t.join()
# print ("退出主线程")

import queue
exitFlag = 0

class MyThread(threading.Thread):
    def __init__(self, threadID, name, q):
        super().__init__(name = name)
        self.threadID = threadID
        self.q = q

    def run(self):
        print(f"开始线程：{self.name}")
        process_data(self.name, self.q)
        print(f"退出线程：{self.name}")

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print(f"{threadName} processing {data}")
        else:
            queueLock.release()
        time.sleep(1)

queueLock = threading.Lock()
workQueue = queue.Queue(10)
threadlist = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
threads = []
threadID = 1

for tName in threadlist:
    thread = MyThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()
print("退出主线程")