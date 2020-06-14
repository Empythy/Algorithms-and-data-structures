class Quantity:

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value > 0:
            # setattr(instance, self.storage_name, value) 不可以使用
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')
class LineItem:
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

item = LineItem("1", 2, 3)
print(vars(item))
# {'description': '1', 'weight': 2, 'price': 3}
item.__dict__["weight"] = -1
print(vars(LineItem))

LineItem.weight = None # 特性会覆盖实例属性
print(vars(item))  #
