# -*- coding: utf-8 -*-#
"""
Created on  2020/7/5  12:45 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""

from collections import deque
# from queue import Queue
import queue


# 维护一个单调的双端队列

class MaxQueue1():
	def __init__(self):
		self.q = deque()

	def max_value(self):
		return max(self.q) if self.q else -1

	def push_back(self, value):
		self.q.append(value)

	def pop_left(self):
		return self.q.popleft() if self.q else -1


# 单调队列
class MaxQueue2(object):
	def __init__(self):
		self.t_q = deque()  # 辅助队列  存放
		self.data_q = queue.Queue()

	def max_value(self):
		return self.t_q[0] if self.t_q else -1

	def push_back(self, item):
		while self.t_q and self.t_q[-1] < item:
			self.t_q.pop()
		self.t_q.append(item)
		self.data_q.put(item)

	def pop_front(self):
		if not self.data_q: return -1
		ans = self.data_q.get()
		if ans == self.t_q[0]:
			self.t_q.popleft()
		return ans


class MaxQueue:
	def __init__(self):
		self.deque = deque()  # 单调递减队列
		self.queue = queue.Queue()

	def max_value(self) -> int:
		return self.deque[0] if self.deque else -1

	def push_back(self, value: int) -> None:
		while self.deque and self.deque[-1] < value:
			self.deque.pop()
		self.deque.append(value)
		self.queue.put(value)

	def pop_front(self) -> int:
		if not self.deque: return -1
		ans = self.queue.get()
		if ans == self.deque[0]:
			self.deque.popleft()
		return ans


if __name__ == '__main__':
	q = MaxQueue()
	q.push_back(1)
	assert q.max_value() == 1
	q.push_back(2)
	assert q.max_value() == 2
	q.push_back(1)
	assert q.max_value() == 2
	q.pop_front()
	q.pop_front()
	assert q.max_value() == 1
