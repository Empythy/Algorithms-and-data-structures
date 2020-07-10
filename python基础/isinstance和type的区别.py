# -*- coding: utf-8 -*-#
"""
Created on  2020/6/30  22:45 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""

class A():
	pass

class B(A):
	pass

class C(B):
	pass


a = A()
b = B()
print(isinstance(a, A))
print(isinstance(b, B))
print(type(a) is A)
print(type(a) == A)
print(type(b) is A)
print(B.__base__)
print(B.__bases__)
print(A.__bases__)
print(C.__bases__)
print(C.__mro__)
print(type(object)) # object 是type的实例
print(type(type)) # type 是type的实例
print(type.__bases__) # type 继承自object
print(object.__bases__)
# object的基类为空 object是最顶层的基类