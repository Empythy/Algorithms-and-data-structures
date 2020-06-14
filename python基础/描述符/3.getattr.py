class Animal(object):
    run = '我会跑'
    def die(self):
        return '我会死'
class Dog(Animal):
    color = 'Blue'
    def __init__(self, name, age):
        self.name=name
        self.age = age
    def _sing(self):
        return "sing"
    def __getattr__(self, key):
        if key == "sing":
            return self._sing  # 返回可调用的对象
        elif key == "name":
            return "No Name"
        elif key =='height':
            return 70
        elif key=='weight':
            return 30
        elif key=='sleep':
            return '我喜欢睡觉'
        else:
            return '还没有定义该属性或者是方法哦！'
            #这个地方也可以自定义的抛出某一种异常哦！
    def sound(self):
        return "汪汪汪"

dog=Dog('泰迪',4)
print(dog.height) #调用不存在的属性height
print(dog.weight) #调用不存在的属性weight
print(dog.sleep)  ##调用不存在的属性sleep
print(dog.laugh)  #调用不存在的属性laugh
print(dog.name)
print(dog.sing())

"""
__getattr__ 和 __getattribute__的详细区别总结：
（1）__getattribute__称之为“属性、方法拦截器”，不管是属性还是方法，
第一步就是先访问__getattribute__；而__getattr__仅仅针对的是属性，不针对方法，即访问未存在的方法的时候依然还是会报错。
（2）__getattribute__针对的是访问已经存在的（属性和方法）；__getattr__针对的是访问未存在的（属性和方法都行）。
（3）__getattribute__和__getattr__虽然针对每一个访问的key，一定要有对应的返回值（参见前文），
但是返回的东西却不是一样的，即__getattribute__返回父类的__getattribute__函数，
而__getattr__返回我希望为未知属性设置的那个值或者是异常信息。
"""