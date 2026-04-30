2026/4/30
一、核心特性必背
列表 list
有序、可变、允许重复元素
可增删改查，支持索引、切片
不能做字典 key（可变类型不可哈希）
字典 dict
键值对结构 key: value
key 唯一不可重复、必须不可变类型（字符串 / 数字 / 元组）
value 任意类型、可重复
Python3.7+ 保留插入顺序
可变类型，可动态增删改
二、字典取值两种方式 & 区别
d['key']：不存在直接抛 KeyError
d.get(key, 默认值)：不存在不报错，返回 None 或默认值
开发 / 面试优先用 get() 更安全
三、字典增删改
新增 / 修改：d[key] = value 有则改，无则加
删除：
d.pop(key)：删指定 key，返回 value
d.popitem()：删最后一组键值对
del d[key]：删除无返回
d.clear()：清空字典
四、三大视图对象
d.keys()：所有键
d.values()：所有值
d.items()：所有 (k,v) 元组
考点：
返回视图对象，不是普通列表
动态跟随原字典变化
要固定快照：list(d.keys())
五、字典三种遍历
只遍历键：for k in d / for k in d.keys()
只遍历值：for v in d.values()
键值一起遍历：
python
运行
for k, v in d.items():
    pass
六、列表去重两种写法
无序去重：list(set(lst))
保序去重（面试标准答案）：list(dict.fromkeys(lst))
七、字典频次统计模板（必考）
python
运行
count = {}
for item in lst:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1
八、字典进阶陷阱口诀
fromkeys 赋可变，全员共享同一个；
键存列表直接挂，可变不能当钥匙；
浅拷只扒第一层，嵌套内容还共用；
推导循环建空值，单独内存不串通；
直接取值不存在，报错翻车没人救；
视图跟着原表走，静态列表不回头；
赋值只是起别名，一改全变不自由；
大小写键不通用，字符分毫不宽容。
九、fromkeys 大坑
错误：
python
运行
d = dict.fromkeys(['a','b'], [])  # 所有key共用同一个列表
正确：
python
运行
d = {k:[] for k in ['a','b']}  # 各自独立
十、Git 上传常用命令（以后记这三条）
bash
运行
git add .
git commit -m "备注说明"
git push
