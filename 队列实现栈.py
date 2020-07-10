from collections import deque


class MyStack():
	"""
	push(x) -- 元素 x 入栈
	pop() -- 移除栈顶元素
	top() -- 获取栈顶元素
	empty() -- 返回栈是否为空
	"""
	def __init__(self):
		# 用两个队列实现
		self.data_q = deque()
		self.t_q = deque()

	def push(self, item):
		self.t_q.append(item)

		while len(self.data_q) > 0:
			self.t_q.append(self.data_q.popleft())

		while len(self.t_q) > 0:
			self.data_q.append(self.t_q.popleft())

	def pop(self):
		if len(self.data_q) >0 :
			return self.data_q.popleft()

	def top(self):
		if len(self.data_q) >0:
			return self.data_q[0]

	def empty(self):
		return len(self.data_q) > 0


class MyStack1():
	def __init__(self):
		self.data = deque()

	def push(self, item):
		size = len(self.data)

		self.data.append(item)
		while size > 0:
			self.data.append(self.data.popleft())
			size -= 1

	def pop(self):
		if len(self.data) > 0:
			return self.data.popleft()

	def top(self):
		if len(self.data) > 0:
			return self.data[0]

	def empty(self):
		return len(self.data) == 0