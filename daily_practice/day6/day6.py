class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我是{self.name}, 今年{self.age}岁")

s1 = Student("小李", 18)
s2 = Student("小芳", 20)
s1.introduce()
s2.introduce()

