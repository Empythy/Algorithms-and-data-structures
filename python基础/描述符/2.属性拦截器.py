"""
当一个属性被访问的时候发生的行为，称之为“属性拦截器”。其实这是对属性的一种高级控制，我们也常称之为“为属性绑定行为”。

Python中只要定义了继承object的类，就默认存在属性拦截器，只不过是拦截后没有进行任何操作，而是直接返回。所以我们可以自己改写__getattribute__方法来实现相关功能，
比如查看权限、打印log日志等
Python的属性访问方式很直观，使用点属性运算符。在新式类中，对对象属性的访问，都会调用特殊方法__getattribute__。__getattribute__允许我们在访问对象属性时自定义访问行为，
但是使用它特别要小心无限递归的问题。
"""

class Animal():
    run = "I can run"

    def die(self):
        return "I cant die"

class Dog(Animal):
    color = "Blue"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 重写__getattribute__。需要注意的是重写的方法中不能
    # 使用对象的点运算符访问属性，否则使用点运算符访问属性时，
    # 会再次调用__getattribute__。这样就会陷入无限递归。
    # 可以使用super()方法避免这个问题。
    # def __getattribute__(self, item):
    #     print("调用了__getattribute__属性")
    #     return super(Dog, self).__getattribute__(item)
    # def sound(self):
    #     return "wang wang wang"

    def __getattribute__(self, key):
        if key == 'name':
            print('name属性被调用了')
            return super(Dog, self).__getattribute__(key)
        elif key == 'age':
            print('age属性被调用了')
            return super(Dog, self).__getattribute__(key)
        elif key == 'color':
            print('color属性被调用了')
            return super(Dog, self).__getattribute__(key)
        elif key == 'run':
            print('run属性被调用了')
            return super(Dog, self).__getattribute__(key)
        elif key == 'sound':
            print('sound方法被调用了')
            return super(Dog, self).__getattribute__(key)
        elif key == 'die':
            print('die方法属性被调用了')
            return super(Dog, self).__getattribute__(key)
        else:
            print('调用了__getattribute__属性')
            return super(Dog, self).__getattribute__(key)

    def sound(self):
        return "汪汪汪"
dog = Dog('泰迪', 5)

print(dog.name)
print(dog.age)
print(dog.color)
print(dog.run)
print(dog.sound())
print(dog.die())

"""
（1）一定要在每一个需要访问的属性里面设置返回值，否则会返回None，一般有两种做法：
即：return super(Dog, self).__getattribute__(key)这种形式或：return object.__getattribute__(self,key)
即返回父类的__getattribute__方法。
（2）不要再在__getattribute__方法的定义内部显示使用self.成员 这种方法，这样可能会造成无限递归，导致系统崩溃。
"""