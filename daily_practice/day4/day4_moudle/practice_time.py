import time
from datetime import datetime

# 1. 获取时间戳（秒级，从1970-01-01至今）
timestamp = time.time()
print("当前时间戳：", timestamp)

# 2. 程序休眠
print("\n程序休眠3秒...")
time.sleep(3)
print("3秒结束，继续执行")

# 3. 获取当前时间的结构化时间对象
local_time = time.localtime()
print("\n当前时间的结构化对象：", local_time)

# 4. 格式化时间（最常用）
time_str = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("\n格式化后的时间字符串：", time_str)

#===============================datetime模块===============================
# 1. 当前时间
now = datetime.now()
print("当前时间：", now)

# 2. 格式化输出
print("格式化：", now.strftime("%Y-%m-%d %H:%M:%S"))

# 3. 字符串转时间
time_str = "2026-05-03 20:30:00"
dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
print("转成时间对象：", dt)


# 4. 时间戳 和 时间对象互转
# 时间对象转时间戳
ts = now.timestamp()
print("时间戳：", ts)

# 时间戳转时间对象
dt2 = datetime.fromtimestamp(ts)
print("时间戳转回时间：", dt2)