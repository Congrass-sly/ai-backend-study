Python 列表+字典 面试终极笔记
一、列表 list 面试考点（必背）
（一）列表基础（必问）
- 有序、可变、可重复、可嵌套
- 可存任意类型：数字、字符串、列表、对象
- 底层是动态数组
（二）最常用 10 个方法（必考）
- append(x)：末尾加1 个元素
- extend(iter)：末尾加多个元素（打散添加）
- insert(i, x)：指定位置i插入元素x
- remove(x)：删除第一个等于x的元素（按值删除）
- pop(i)：删除下标i对应的元素，返回被删值（默认删最后一个）
- del list[i]：直接删除下标i的元素，无返回值
- clear()：清空列表所有元素，保留列表对象
- index(x)：查找第一个x的下标，不存在报错
- sort()：原地升序排列；sort(reverse=True) 原地降序
- reverse()：原地反转列表元素顺序
（三）切片（高频）
语法：[start:end:step]，核心规则：左闭右开
- [:]：复制整个列表（浅拷贝的一种）
- [::-1]：快速反转列表（返回新列表，不改变原列表）
- 步长step为负：倒着截取元素
（四）深浅拷贝（高频必问）
1. 赋值 =：完全共用内存地址，一改全改（本质是给原列表起别名，共用同一份数据）
2. 浅拷贝：copy() / list() / [:]，第一层元素独立，嵌套层（如列表里的列表）仍共用
3. 深拷贝：完全独立，互不影响（开辟新的内存空间，复制所有层级的元素）
深拷贝代码示例：
import copy
a = [1, [2, 3]]
b = copy.deepcopy(a)  # 完全独立，修改b的嵌套列表不影响a
（五）列表推导式（高频考点）
- 单层推导式：[x for x in lst if 条件]（简洁高效）
- 双层展平（二维列表转一维）：[num for item in lst for num in item]（顺序：先外后内）
（六）列表去重（面试常写）
- 简单去重（乱序）：list(set(lst))（利用set不可重复特性，缺点是打乱原顺序）
- 保持顺序（推荐，面试标准答案）：list(dict.fromkeys(lst))（利用字典key唯一且3.7+保序特性）
（七）遍历 3 种写法
# 写法1：直接遍历元素
for x in lst:
    pass

# 写法2：通过下标遍历（不推荐）
for i in range(len(lst)):
    print(lst[i])

# 写法3：最优（同时获取下标和元素）
for idx, val in enumerate(lst):
    pass
（八）高频对比（面试易混点）
- list vs tuple：list 可变（可增删改），tuple 不可变（一旦创建无法修改）
- list vs set：list 可重复、有序；set 不可重复、无序
- append vs extend：append 加整体（如append([1,2])会把列表作为一个元素添加），extend 打散添加（如extend([1,2])会添加1和2两个元素）
- remove vs pop vs del：remove(值)（按值删，删第一个）；pop(下标)（按下标删，有返回值）；del(下标)（按下标删，无返回值）
（九）8 道面试真题答案（直接背）
- 反转列表：lst[::-1]（返回新列表）或 lst.reverse()（原地反转）
- 合并列表：lst1 + lst2（返回新列表）、lst1.extend(lst2)（原地合并）
- 去重保序：list(dict.fromkeys(lst))
- 深浅拷贝：浅拷只独立第一层，深拷全独立（用copy.deepcopy()）
- 展平二维列表：[n for i in lst for n in i]
- append/extend区别：append加一个元素（可是任意类型），extend加多个元素（需是可迭代对象）
- 遍历推荐：enumerate(lst)（同时获取下标和元素）
- 推导式优点：简洁、高效、可读性强（比for循环代码更简洁，执行速度更快）
（十）万能一句话（面试结束语）
列表是 Python 最常用的有序可变序列，核心考点：方法、切片、推导式、深浅拷贝、去重、遍历。
二、字典 dict 面试考点（必背）
（一）核心特性必背
- 键值对结构：key: value
- key 唯一不可重复、必须是不可变类型（字符串/数字/元组），不能用列表（可变不可哈希）
- value 任意类型、可重复
- Python3.7+ 保留插入顺序，3.6及以前不保证
- 可变类型，可动态增删改键值对
（二）字典取值两种方式 & 区别（必考）
- d['key']：key不存在直接抛 KeyError（程序崩溃，不推荐）
- d.get(key, 默认值)：key不存在不报错，返回 None 或指定的默认值（开发/面试优先用，更安全）
（三）字典增删改
- 新增/修改：d[key] = value（key存在则修改，不存在则新增）
- 删除：
        
  - d.pop(key)：删除指定key，返回对应的value
  - d.popitem()：删除最后一组键值对（3.7+ 按插入顺序）
  - del d[key]：删除指定key，无返回值
  - d.clear()：清空字典所有键值对，保留字典对象
（四）三大视图对象（高频）
- d.keys()：返回所有key的视图对象
- d.values()：返回所有value的视图对象
- d.items()：返回所有 (key, value) 元组的视图对象
考点：
- 视图对象不是普通列表，不能直接切片
- 动态跟随原字典变化（原字典修改，视图对象也会同步变化）
- 要固定快照（不跟随变化）：list(d.keys()) / list(d.values()) / list(d.items())
（五）字典三种遍历（必考）
# 1. 只遍历键（默认遍历键）
for k in d:
    pass
# 等价于
for k in d.keys():
    pass

# 2. 只遍历值
for v in d.values():
    pass

# 3. 键值一起遍历（最常用）
for k, v in d.items():
    pass
（六）字典频次统计模板（必考，面试常写）
# 场景：统计列表/字符串中每个元素的出现次数
count = {}
for item in 待统计对象:  # 待统计对象可以是列表、字符串等可迭代对象
    if item in count:
        count[item] += 1  # 存在则计数+1
    else:
        count[item] = 1  # 不存在则初始化为1
（七）字典进阶陷阱口诀（背会避坑，面试高频）
1. fromkeys赋可变，全员共享同一个；
2. 键存列表直接挂，可变不能当钥匙；
3. 浅拷只扒第一层，嵌套内容还共用；
4. 推导循环建空值，单独内存不串通；
5. 直接取值不存在，报错翻车没人救；
6. 视图跟着原表走，静态列表不回头；
7. 赋值只是起别名，一改全变不自由；
8. 大小写键不通用，字符分毫不宽容。
（八）fromkeys 大坑（面试易错点）
错误写法（所有key共用同一个可变对象）：
d = dict.fromkeys(['a','b'], [])  # 所有key共用同一个空列表，改一个全改
正确写法（每个key对应独立的可变对象）：
d = {k:[] for k in ['a','b']}  # 每个key都有独立的空列表，互不影响
三、Git 上传常用命令（日常必备，同步笔记/代码）
# 1. 将本地修改的文件加入暂存区
git add .

# 2. 提交暂存区文件，备注修改内容（备注要简洁明了）
git commit -m "备注说明"  # 示例：git commit -m "更新列表+字典面试笔记"

# 3. 将提交的内容推送到GitHub仓库（同步更新）
git push
补充：首次配置Git（仅第一次需要）
git config --global user.email "2831246694@qq.com"
git config --global user.name "Congrass-sly"