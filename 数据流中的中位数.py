# -*- coding: utf-8 -*-#
"""
Created on  2020/7/4  17:22 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""

import bisect


class MedianFinder_v1:

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.data = []

	def addNum(self, num: int) -> None:
		bisect.insort(self.data, num)

	def findMedian(self) -> float:
		n = len(self.data)
		if n == 0:
			return
		if n % 2 == 1:
			return self.data[n // 2]
		else:
			return (self.data[n // 2] + self.data[(n - 1) // 2]) * 0.5


import heapq


class MedianFinder:

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.max_heap = []  # 左边
		self.min_heap = []  # 右边

	def addNum(self, num: int) -> None:
		# 注意插入数据有坑
		if len(self.min_heap) > 0:  # 当最小堆中有值
			if num < self.min_heap[0]:  # 当前值小于最小堆堆顶
				heapq.heappush(self.max_heap, -num)  # 往最大堆插入
			else:  # 当前值大于最小堆堆顶  往最小堆插入
				heapq.heappush(self.min_heap, num)
		else:
			heapq.heappush(self.max_heap, -num)
		self.balance()

	def balance(self):

		if len(self.max_heap) - len(self.min_heap) > 1:
			pop_item = -heapq.heappop(self.max_heap)  # 最大堆里面抛出一个数
			heapq.heappush(self.min_heap, pop_item)

		if len(self.min_heap) - len(self.max_heap) >= 1:
			pop_item = heapq.heappop(self.min_heap)
			heapq.heappush(self.max_heap, -pop_item)

	def findMedian(self) -> float:
		n = len(self.min_heap) + len(self.max_heap)
		if n == 0:
			return
		if n % 2 == 1:
			return self.max_heap[0] * -1
		else:
			return (-1 * self.max_heap[0] + self.min_heap[0]) * 0.5


s = MedianFinder()

s.addNum(1)
print(s.findMedian())
s.addNum(2)
s.addNum(3)
print(s.findMedian())
