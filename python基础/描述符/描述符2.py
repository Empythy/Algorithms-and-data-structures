class Quantity:
    __counter = 0
    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        print(owner.__name__) # 类的名字
        # 存储属性和托管属性名称不同
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')

class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

item = LineItem("1", 1, 1)
print(item.subtotal())
print(vars(item)) # {'description': '1', '_Quantity#0': 1, '_Quantity#1': 1}
print(item.price)
print(LineItem.weight) # 会报错
print(vars(LineItem))