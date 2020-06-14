"""
（1）描述符：某个类，只要是内部定义了方法 __get__, __set__, __delete__ 中的一个或多个，就可以称为描述符，描述符的本质是一个类。
（2）描述符协议:描述符本质就是一个新式类,在这个新式类中,至少实现了__get__(),__set__(),__delete__()中的一个,这些魔术方法也被称为描述符协议
（3）非数据描述符：一个类，如果只定义了 __get__() 或者是__delete__()方法，而没有定义 __set__()方法，则认为是非数据描述符(即没有定义__set__)
（4）数据描述符：一个类，不仅定义了 __get__() 方法，还定义 __set__(), __delete__() 方法，则认为是数据描述符(即定义了__get__和__set__)
（5）描述符对象：描述符（即一个类，因为描述符的本质是类）的一个对象，一般是作为其他类对象的属性而存在
"""


# 人的性格描述，悲观的？开朗的？敏感的？多疑的？活泼的？等等
class CharacterDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        """
        :param self: 描述符类的实例
        :param instance: 使用描述符的那个类的实例
        :param owner: 使用描述符的那个类
        :return:
        """
        print("访问性格属性\t", self.value)
        return self.value

    def __set__(self, instance, value):
        print("设置性格属性值")
        self.value = value


# 人的体重描述，超重？过重？肥胖？微胖？合适？偏轻？太瘦？等等
class WeightDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print("访问体重属性\t", self.value)
        return self.value

    def __set__(self, instance, value):
        print("设置体重属性值")
        self.value = value


class Person:
    character = CharacterDescriptor('乐观的')
    weight = WeightDescriptor(150)


print("======================Person==================================")
p = Person()  # 没有调用__set__方法
print(vars(p)) # {}
print(p.character)
print(p.weight)  # print(Person.__dict__["character"].__get__(None, Person))


class Person1:
    def __init__(self):
        self.character = CharacterDescriptor('乐观的')
        self.weight = WeightDescriptor(150)


print("======================Person1==================================")
p = Person1()  # 不能将属性描述符 用于实例属性
print(p.character)  # 属性的访问
print(p.weight)  #
p.weight = 200  # 修改属性
print(p.weight)
# del p.weight  # 删除属性  报错
print(p.weight)

"""
描述符是一个类属性，必须定义在类的层次上, 而不能单纯的定义为对象属性。
通过上面的这几个例子，现在应该可以好好体会到“描述符”的两个层面的作用了：
绑定行为：在访问类属性的时候，会打印出很多的额外信息，这不就是在添加额外的行为吗？
属性代理(托管属性)：将某个属性专门用一个描述符（描述类）加以托管，实现任意的定制化，一对一的定制属性。
"""
print("======================Person2==================================")
# 实例属性和描述符属性相同
class Person2:
    character = CharacterDescriptor('乐观的')
    weight = WeightDescriptor(150)

    def __init__(self, character, weight):
        self.character = character
        self.weight = weight


p = Person2('悲观的', 200)
print(vars(p))  # {}
print(p.character)  # 属性的访问
print(p.weight)
print(Person2.weight)
"""
从上面的运行结果可以看出，首先是访问了描述符的__set__方法，这是因为在构建对象的时候，
相当于为character和weight赋值，然后再调用__get__方法，这是因为访问了类属性character和weight，
"""
"""
没有设置描述符属性，则属性的优先访问顺序和我们前面文章里面所讲的是一样的，
（1） __getattribute__()， 无条件调用，任何时候都先调用
（2）实例属性
（3）类属性
（4）父类属性
（5）__getattr__() 方法  #如果所有的属性都没有搜索到，则才会调用该函数
"""

print("====================Person2===============================")


class Person2:
    a2 = CharacterDescriptor('乐观的')
    def __init__(self):
        self.a2 = '悲观的'  # 给描述符变量赋值

    def __getattribute__(self, key):
        print('__getattribute__')
        return super(Person2, self).__getattribute__(key)

    def __getattr__(self, key):
        print('__getattr__')


p = Person2()
print(vars(p))
print(p.a2)
print(Person2.a2)

class Person3:
    a2 = CharacterDescriptor('乐观的')
    a2 = '沮丧的'  # 覆盖了

    def __init__(self):
        pass

    def __getattribute__(self, key):
        print('__getattribute__')
        return super(Person3, self).__getattribute__(key)
print("======================Person3=============================")
p = Person3()
print(p.a2)
