
"""
python 对象的__dict__ 属性

python 的类属性和类方法 既可以通过类名访问 也可以通过实例访问
"""

class Animal(object):
    name = "Tiger"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return "I want to eat"

    @classmethod
    def sleep(cls):
        return "I want to sleep"

a = Animal("老虎", 5)
print(a.name) # 优先访问实例属性
print(a.age)
print(a.eat()) # 访问实例方法
print(a.sleep()) # 访问类方法

print(Animal.name)
print(Animal.sleep())

class Dog(Animal):
    #name_='小狗'

    def __init__(self, age):
        self.age = age

d = Dog(8)
print(d.name)
print(d.age)
##
# 实例是可以访问类的成员的，但是类不能访问实例成员；
# 对于关系二而言，子类继承父类的类成员和实例成员
##

print(Animal.__dict__.keys())
print(a.__dict__.keys())
print(Dog.__dict__.keys())
print(d.__dict__.keys())
"""
由此可见，实例a最先直接访问的属性就只有name,age,weight，并不包含类属性name，
我们可以这么，name、age、weight是属于a的，但是类属性name是不属于a的。
那么，对象对属性的访问到底遵循怎样一个优先级呢？先告诉你答案！
①.实例属性
②.类属性
③.父类的类属性
④.__getattr__()方法（访问一个不存在的属性的时候发生的行为）
注意：这里的优先级只是最基本的，没有涉及到任何的属性设置和属性控制，
后面还会讲到属性的优先级。
"""

class AnimalTest():
    name = "老虎"
    def __init__(self):
        pass

class DogTest(AnimalTest):
    age = 10
    def __init__(self, height):
        self.height = height

    def __getattr__(self, item):
        if item == "weight":
            return 200
        else:
            raise AttributeError
d = DogTest(150)
print(d.height)
print(d.age)
print(d.name)
print(d.weight)