#检验标识符是否合法
# def is_valid_identifier(name):
#     try:
#         exec(f"{name} = None")
#         return True
#     except:
#         return False
    
# print(is_valid_identifier("Var2"))
# print(is_valid_identifier("2Var"))

#偶数筛查函数
n = [1,2,3,4,5,6,7,8,9,10] #定义一个列表，包含1到10的整数

def filter_even_numbers(n):
    return [i for i in n if i% 2 == 0] #使用列表推导式，遍历列表n中的每个元素i，如果i是偶数（即i%2等于0），则将其添加到新的列表中并返回

print(filter_even_numbers(n))#调用函数filter_even_numbers，并将列表n作为参数传递，输出结果为[2, 4, 6, 8, 10]，即列表n中的偶数元素。

#------------------------------------------------字典操作
emptydict = {}

print(emptydict) #输出空字典{}
print(type(emptydict)) #输出空字典的类型<class 'dict'>
print(len(emptydict)) #输出空字典的长度0 

emptydict = dict() #使用dict()函数创建一个空字典

student = {"name": "sly", "age": 21, "gender": "男", "major": "计算机科学与技术"} #创建一个包含学生信息的字典
print("student['name']:", student['name']) #输出学生的名字sly
print(student) #输出学生信息字典{'name': 'sly', 'age': 21
student["name"] = "xzw"
student['school'] = "华中科技大学"
print(student) #输出更新后的学生信息字典{'name': 'xzw', 'age': 21, '

del student['age'] #删除学生信息字典中的年龄键值对
print(student) #输出删除年龄键值对后的学生信息字典{'name': '
student.clear() #清空学生信息字典中的所有键值对
print(student) #输出清空后的学生信息字典{}
del student #删除学生信息字典对象

tinydict = {"a": 1, "b": 2, "c": 3} #创建一个包含三个键值对的字典
len(tinydict) #输出字典tinydict的长度3
str(tinydict) #输出字典tinydict的字符串表示形式"{'a': 1, 'b': 2, 'c': 3}"
welldict = tinydict.copy() #创建一个字典tinydict的副本
betterdict = {}.fromkeys(tinydict,[0,1,2])#使用fromkeys()方法创建一个新字典betterdict，其中键来自字典tinydict的键，值为列表[0, 1, 2]，输出新创建的字典{'a': [0, 1, 2], 'b': [0, 1, 2], 'c': [0, 1, 2]}
print(betterdict) #创造出的新字典中所有键的值是共享的，即它们都指向同一个列表对象[0, 1, 2]，因此修改其中一个键的值会影响到所有键的值。
j = ["a","b","c"]
k = ["x","y","z"]
betterdict = {k : [1,2,3] for k in j} #使用字典推导式创建一个新字典betterdict，其中键来自列表j，值为列表[1, 2, 3]，输出新创建的字典{'a': [1, 2, 3], 'b': [1, 2, 3], 'c': [1, 2, 3]}
print(betterdict) #输出新创建的字典{'a': [1, 2, 3], 'b': [1, 2, 3], 'c': [1, 2, 3]}
print(tinydict.get("a")) #使用get()方法获取键"a"对应的值1
print(betterdict.get("a", None)) #使用getb()方法获取键"a"对应的值，如果键不存在则返回None
print("a" in tinydict) #使用in运算符检查键"a"是否在字典tinydict中，输出True
print(tinydict.items()) #使用items()方法获取字典tinydict中的所有键值对，输出dict_items([('a', 1), ('b', 2), ('c', 3)])
print(tinydict.keys()) #使用keys()方法获取字典tinydict中的所有键，输出dict_keys(['a', 'b', 'c'])
print(tinydict.values()) #使用values()方法获取字典tinydict中的所有值，输出dict_values([1, 2, 3])
print(tinydict.pop("a")) #使用pop()方法删除键"a"并返回其对应的值1
print(tinydict.popitem()) #使用popitem()方法删除字典tinydict中的最后一个键值对并返回该键值对('c', 3)
print(tinydict.setdefault("a", 4)) #使用setdefault()方法获取键"a"对应的值，如果键不存在则将其设置为4并返回4
print(welldict.update(betterdict)) #使用update()方法将字典betterdict中的键值对更新到字典welldict中，输出None


#------------------------------------------------统计字符串中每个字符出现的次数
s = "abracadabra"
count = {}
for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print(count) #输出字符串s中每个字符出现的次数{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1} 


#------------------------------------------------列表推导式和生成器表达式
squares = [x**2 for x in range(10)] #使用列表推导式创建一个包含0到9的平方数的列表squares，输出[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares) #输出列表squares 

nums = [1,3,2,3,1,5,2,6,5]

res = (i for i in list(dict.fromkeys(nums)) if i > 3)