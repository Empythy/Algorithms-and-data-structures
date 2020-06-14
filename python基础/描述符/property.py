class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')

class LineItem1:

    def __init__(self, des, weight, price):
        self.des = des
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    def get_weight(self):
        return self.__weight

    def set_weight(self, val):
        if val > 0:
            self.__weight = val
        else:
            raise ValueError("value must be > 0")
    weight = property(get_weight, set_weight)


class Class:
    data = "the class data attr"

    @property
    def prop(self):
        return 'the prop value'



obj = Class()
print(vars(obj)) # {}
print(obj.data) # "the class data attr"
obj.data = "bar"
print(vars(obj)) # {'data': 'bar'}
print(Class.data) # "the class data attr"
print(Class.prop) # <property object at 0x0000025689C4CDB8>

print(obj.prop) # the prop value
# obj.prop = 'foo'  # 尝试设置 prop 实例属性， 结果失败。
obj.__dict__["prop"] = 'foo' # 可以修改__dict__
print(vars(obj)) #obj 现在有两个实例属性： data 和 prop
print(obj.prop) # the prop value 特性没被实例属性遮盖
Class.prop = "baz" # 将类特性覆盖了
print(obj.prop)
print(obj.data) # 'bar' 获取实例属性
print(Class.data) # 类属性

# 使用property
Class.data = property(lambda self: 'the "data" prop value')
# obj.data 会被class.data 特性遮盖
print(obj.data)
del Class.data
print(obj.data)


"""
本节的主要观点是， obj.attr 这样的表达式不会从 obj 开始寻找
attr， 而是从 obj.__class__ 开始， 而且， 仅当类中没有名为 attr
的特性时， Python 才会在 obj 实例中寻找。 这条规则不仅适用于特性，
还适用于一整类描述符——覆盖型描述符（overriding descriptor） 。 第
20 章会进一步讨论描述符， 那时你会发现， 特性其实是覆盖型描述
符。
"""


def quantity(storage_name):
    """
    特性工厂函数
    :param storage_name:
    :return:
    """
    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('value must be > 0')
    return property(qty_getter, qty_setter)


class LineItem3:
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

item = LineItem3("1", 10, 20)
print(vars(item))


class LineItem4:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
    def subtotal(self):
        return self.weight * self.price