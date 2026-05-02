#函数打印“hello world”
def print_hello():
    print("hello world")

print_hello()

#比较大小
def Max(a,b):
    if a > b:
        return a
    else:
        return b
    
print(Max(4,5))

#---------------------lambda匿名函数---------------------
#sorted函数的key参数可以接受一个函数作为参数，lambda匿名函数可以用来定义这个函数,来排序
lst = [(1,7),(3,4),(5,6)]
res = sorted(lst, key = lambda x: x[1]) #按照每个元组的第二个元素进行排序
print(res)

lst = [-1,-5,0,3,4]
res =sorted(lst, key = lambda x: abs(x), reverse = True) #按照绝对值进行倒序排序
print(res)

user = [{"name":"张三","age":20},
        {"name":"李四","age":18},]
res = sorted(user, key = lambda x: x["age"]) #按照年龄进行排序
print(res)

#map函数可以接受一个函数和一个可迭代对象作为参数，lambda匿名函数可以用来定义这个函数,来对可迭代对象中的每个元素进行操作
lst = [1,2,3,4,5]
res = list(map(lambda x: x*2, lst)) #将lst中的每个元素乘以2
print(res)

res = list(map(lambda x: str(x), lst)) #将lst中的每个元素转换为字符串
print(res)

a = [1,2,3]
b = [4,5,6]
res = list(map(lambda x,y: x+y, a, b)) #将a和b中的元素对应相加
print(res)

#filter 筛选过滤
lst = [1,2,3,4,5]
res = list(filter(lambda x: x%2 == 0,lst))
print(res) #筛选出lst中的偶数

res = list(filter(lambda x: x <4,lst))
print(res) #筛选出lst中小于4的元素

#带条件表达式（lambda 里做判断） 只能用三元表达式，不能用普通 if
f = lambda x: x**2 if x % 2 == 0 else x
print(f(4)) #如果x是偶数，返回x的平方，否则返回x本身
print(f(5)) #如果x是偶数，返回x的平方，否则返回x本身

#字典分支映射（替代 if 多分支）
cal = {
    "add": lambda x,y: x+y,
    "sub": lambda x,y: x-y,
    "mul": lambda x,y: x*y,
    "div": lambda x,y: x/y if y != 0 else "除数不能为0"
}
print(cal["add"](3, 4))  # 输出 7
print(cal["div"](10, 2))  # 输出 5.0
print(cal["div"](10, 0))  # 输出 "除数不能为0"

#带必传参数的计算函数
def calculate(op, x, y):
    ops ={                          #如果用op做字典名会改变传入的形参op的值，所以用ops做字典名
        "add": lambda x,y: x+y,
        "sub": lambda x,y: x-y,
        "mul": lambda x,y: x*y,
        "div": lambda x,y: x/y if y != 0 else "除数不能为0"
    }
    if op in ops:
        return ops[op](x,y)
    else:   
        return "不支持的操作"
print(calculate("add", 3, 4))  # 输出 7
print(calculate("div", 10, 2))  # 输出 5.0

#带默认函数的函数
def add_accumulate(x, y, /, c=1, *args):
    total = x + y + c
    for arg in args:
        total += arg
    return total
print(add_accumulate(1, 2))  # 输出 4 (1 + 2 + 默认值 1)

#带返回值的工具函数
def list_deduplicate(lst, /):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst
print(list_deduplicate([1, 2, 2, 3, 4, 4, 5]))  # 输出 [1, 2, 3, 4, 5]