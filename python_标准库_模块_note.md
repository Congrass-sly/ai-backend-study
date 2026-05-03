# 一、纯文本版（无格式，可直接复制保存）
# Python 标准库 & 模块包 & 核心知识点笔记（含面试例题+答案）
## 一、__name__ 属性 核心考点
1.  每个 .py 文件（模块）都有内置属性 __name__
2.  两个核心值：
    - 直接运行该文件（程序入口）：__name__ = "__main__"
    - 被 import 导入（工具模块）：__name__ = 模块名（文件名，不带 .py）
3.  经典规范写法：if __name__ == "__main__": main()
    作用：区分入口程序与工具模块，避免导入时执行测试代码

## 二、dir() 内置函数
1.  作用：查看对象/模块的属性、方法，判断可用成员
2.  三种用法：
    - dir()：查看当前全局作用域变量、成员
    - dir(模块名)：查看模块内函数、变量、类
    - dir(对象)：查看实例/类的属性、方法
3.  特点：返回字符串列表；__xx__ 开头为魔法属性/方法，无需手动调用

## 三、模块与包 核心考点
1.  模块：单个 .py 文件，作用是代码拆分、复用，避免全局变量冲突
2.  包：含 __init__.py 的文件夹，无 __init__.py 无法作为包导入
3.  三种导入方式：
    - 绝对导入：完整路径，工作首选，稳定清晰
    - 相对导入：.（当前）、..（上级），仅包内部使用，不能单独运行脚本
    - 集中导入：__init__.py 统一暴露接口，简化外部导入
    实操示例：__init__.py 中写 from .math_tools import add, subtract，外部可直接 from 包名 import add
4.  避坑要点：
    - 文件名/文件夹不与系统模块（sys、os、json）重名
    - 禁止中文、空格命名，否则跨平台导入失败
    - 导入失败优先查：命名冲突、sys.path、目录层级

## 四、OS 标准库
1.  核心常用：
    - os.getcwd()：获取当前工作目录
    - os.listdir()：列出目录下所有文件/文件夹
    - os.path.exists()：判断路径是否存在
    - os.path.join()：跨平台路径拼接（必用）
2.  项目路径万能公式：
    import os
    self_dir = os.path.dirname(os.path.abspath(__file__))  # 当前文件所在目录
    root_dir = os.path.dirname(self_dir)  # 项目根目录

## 五、JSON 标准库
1.  四大核心方法：
    - json.dumps()：字典 → JSON 字符串
    - json.loads()：JSON 字符串 → 字典
    - json.dump()：字典写入 JSON 文件
    - json.load()：读取 JSON 文件 → 字典
2.  关键参数：ensure_ascii=False（中文不转义），indent=4（格式化排版）
3.  注意：JSON 不支持存储函数、对象，仅支持字符串、数字、布尔、列表、字典、null

## 六、Random 标准库
1.  核心方法：
    - random.random()：0~1 随机小数
    - random.randint(a,b)：[a,b] 随机整数
    - random.choice(seq)：随机选一个元素
    - random.shuffle(seq)：打乱列表顺序
    - random.sample(seq, n)：选 n 个不重复元素
2.  工作常用：6位数字验证码
    import random
    code = [str(random.randint(0,9)) for _ in range(6)]
    verification_code = "".join(code)

## 七、Time & Datetime 时间库
1.  time 常用：
    - time.time()：获取时间戳（秒，浮点数，1970-01-01 至今）
    - time.sleep(n)：程序休眠 n 秒
    - time.strftime("%Y-%m-%d %H:%M:%S", 时间对象)：格式化时间
2.  datetime 常用：
    - datetime.now()：获取当前时间
    - datetime.strptime(字符串, 格式)：字符串转时间对象
    - 时间戳转时间：datetime.fromtimestamp(ts)（自动转本地时区）
3.  常用格式符：%Y（年）、%m（月）、%d（日）、%H（时）、%M（分）、%S（秒）

## 八、面试例题 + 标准答案（高频必考）
### 例题1：简述 __name__ 属性的两个核心值及对应场景
答：1. 当文件被直接运行（作为程序入口）时，__name__ = "__main__"；2. 当文件被 import 导入（作为工具模块）时，__name__ = 模块名（文件名，不带 .py）。作用是区分入口程序和工具模块，避免导入时执行内部测试代码。

### 例题2：简述 os 模块中路径拼接为什么要用 os.path.join()，而不是直接用字符串拼接？
答：因为不同操作系统的路径分隔符不同（Windows 用 \，Linux 用 /），os.path.join() 会自动适配当前系统的分隔符，避免路径错误，保证跨平台兼容性。

### 例题3：JSON 转换中，为什么要加 ensure_ascii=False？如果不加会有什么问题？
答：ensure_ascii=False 的作用是保留中文不转义，正常显示中文；如果不加，中文会被转义成 Unicode 编码（如 \u4e2d\u6587），导致显示混乱，不符合实际使用需求。

### 例题4：简述相对导入和绝对导入的区别，以及各自的使用场景
答：1. 绝对导入：从项目根目录写完整路径，清晰稳定，适用于外部导入、跨包调用，是工作中首选；2. 相对导入：用 .（当前）、..（上级）表示路径，仅适用于包内部文件之间的调用，不能单独运行脚本，优势是简洁，不用写完整路径。

### 例题5：如何生成一个6位数字验证码？请写出核心代码
答：核心代码如下：
import random
code_list = [str(random.randint(0, 9)) for _ in range(6)]
verification_code = "".join(code_list)
print(verification_code)
原理：循环6次，每次生成0-9随机数字，转成字符串存入列表，最后拼接成6位验证码，避免0开头被自动省略。

### 例题6：简述 dir() 函数的作用及常用用法
答：dir() 函数用于查看对象的属性和方法，返回字符串列表。常用用法：1. dir()：查看当前全局作用域的变量、成员；2. dir(模块名)：查看模块内的函数、变量、类；3. dir(对象)：查看实例或类的属性、方法。其中 __xx__ 开头的是魔法属性/方法，无需手动调用。

### 例题7：简述包和模块的区别，以及 __init__.py 的作用
答：1. 模块是单个 .py 文件，包是含 __init__.py 的文件夹；2. 模块用于功能拆分复用，包用于分类管理多个模块（更具工程化）；3. __init__.py 的作用：标记该文件夹为 Python 包，同时可集中导入内部模块，对外暴露接口，简化外部导入写法。

### 总结
核心重点：掌握 __name__ 属性、模块包导入、OS/JSON/Random 基础用法，牢记面试例题标准答案，可应对大部分 Python 基础面试场景，同时适配实际项目开发需求。