"""
__setattr__方法允许定义为某个属性赋值的时候所发生
行为，不管这个属性存在与否，都可以对任意属性的任何
变化都定义自己的规则。
"""

class Animal():
    run = "我会跑"

    def die(self):
        return "我会死"
class Dog(Animal):
    color = "Blue"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, key, value):
        print("我被赋值了")
        super(Dog, self).__setattr__(key, value)

    def __delattr__(self, key):
        print('我被删除啦！')
        super(Dog, self).__delattr__(key)

    def sound(self):
        return "wang wang wang"

dog = Dog("泰迪", 4)
dog.age = 6
dog.color = "Yellow"
dog.height = 70

print(dog.name)
print(dog.age)
print(dog.color)
print(dog.height)
print(dog.sound())
# 添加额外的方法
def say_hello(self):
    return "hello"
dog.say_hello = say_hello

print(dog.say_hello(dog))


"""
关于__setattr__有一点需要说明，使用它时必须小心，
不能写成类似self.name = “张三”这样的形式，
因为这样的赋值语句会调用__setattr__方法，这样会让其陷入无限递归，
参见前文的__getattribute__方法出现无限递归的情况，二者是一样的

"""

del dog.say_hello
print(dog.say_hello)