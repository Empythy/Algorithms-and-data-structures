# -*- coding: utf-8 -*-#
"""
Created on  2020/7/4  15:45 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from collections import deque
from typing import List


class MonoQue():
	def __init__(self):
		self.data = deque()

	def push(self, item):

		while len(self.data) > 0 and self.data[-1] < item:  # 如果队尾的值小于 item 则弹出
			self.data.pop()
		self.data.append(item)

	def pop(self, item):
		if len(self.data) > 0 and self.data[0] == item:
			self.data.popleft()

	def max(self):
		if len(self.data) > 0:
			return self.data[0]


class Solution:
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

		q = MonoQue()
		for i in range(k - 1):
			q.push(nums[i])
		ans = []
		for i in range(k - 1, len(nums)):
			q.push(nums[i])
			ans.append(q.max())
			# 删除首个  # [1, 2, 3, 4, 5]  k = 3  i=2    0
			q.pop(nums[i - (k - 1)])

		return ans


s = Solution()
ans = s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(ans)
