# -*- coding: utf-8 -*-#
"""
Created on  2020/6/28  23:28 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""

# class Person(object):
# 	def __init__(self, age, height):
# 		self.age = age
# 		self.height = height
#
# 	# 按照 age 升序  height 降序
# 	def __le__(self, other):
#
# 		if self.age > other.age:
# 			return 1
# 		elif self.age == other.age:
# 			if self.height < other.height:
# 				return 1
# 		else:
# 			return -1
import heapq


class Car():
	def __init__(self, carname, oilcp100km, price):
		self.carname, self.oilcp100km, self.price = carname, oilcp100km, price

	def __lt__(self, other):
		if self.price == other.price:
			return self.oilcp100km > other.oilcp100km
		return self.price < other.price

	def __str__(self):
		return self.carname

car1 = Car('爱丽舍', 8, 10)
car2 = Car('凯美瑞', 7, 27)
car3 = Car('宝马', 9, 10)
car4 = Car('途观', 12, 27)

# 调用内置函数
for item in sorted([car1, car2, car3, car4]):
	print(item)


# 使用堆
cars = [car1, car2, car3, car4]
heapq.heapify(cars)
while len(cars) > 0:
	print(heapq.heappop(cars))
