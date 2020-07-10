# -*- coding: utf-8 -*-#
"""
Created on  2020/7/5  12:09 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""


class MyQue():
	def __init__(self):
		self.head = -1
		self.end = -1
		self.size = 0
		self.max_size = 3
		self.data = [None] * self.max_size


	def push(self, item) -> None:
		if self.size >= self.max_size:
			raise ValueError('Error')
		if self.head == -1 and self.end==-1:
			self.head = 0
		self.end = (self.end + 1) % self.max_size
		self.data[self.end] = item
		self.size += 1

	def pop(self) -> int:
		if self.size > 0:
			pop_item = self.data[self.head]
			self.head = (self.head + 1) % self.max_size
			self.size -= 1
			return pop_item

	def empty(self) -> bool:
		return self.size == 0

	def top(self) -> int:
		if self.size > 0:
			return self.data[self.head]
		else:
			raise ValueError('que is empty')

if __name__ == "__main__":
	q = MyQue()
	assert q.empty() == True

	q.push(1)
	q.push(2)
	q.push(3)
	try:
		q.push(4)
	except:
		pass
	assert q.pop() == 1
	assert q.pop() == 2
	q.push(4)
	assert q.pop() == 3
	assert q.top() == 4
	assert q.pop() == 4
	assert q.empty() == True
