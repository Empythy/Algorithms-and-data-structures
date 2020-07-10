# -*- coding: utf-8 -*-#
"""
Created on  2020/6/28  21:30 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""

from functools import lru_cache
from typing import List


class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		if len(nums) <= 1:
			return len(nums)
		# dp[i] 代表以 i 结尾的最长子序列
		self.res = [1]

		@lru_cache(None)
		def dp(i: int):
			if i == 0:
				return 1
			tmp = 1
			for j in range(i):
				if nums[i] > nums[j]:
					tmp = max(tmp, 1 + dp(j))
			return tmp

		res = 1
		for i in range(len(nums)):
			res = max(res, dp(i))
		return res

	def method2(self, nums: List[int]):
		dp = [1] * len(nums)
		for i in range(1, len(nums)):
			for j in range(i):
				if nums[i] > nums[j]:
					dp[i] = max(dp[i], 1 + dp[j])
		return max(dp)


nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
s = Solution()
res = s.lengthOfLIS(nums)
print(res)

# 无重叠区间 435
# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
class Solution:
	# 超时
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		"""
		查找最长上升子序列 1 2 2 3 3 4
		"""
		if len(intervals) <= 1:
			return 0

		intervals.sort(key=lambda x: x[1])  # 按照第二维度升序
		dp = [1] * len(intervals)

		## 会超时
		# for i in range(1, len(intervals)):
		# 	for j in range(i):
		# 		if intervals[i][0] >= intervals[j][1]:
		# 			dp[i] = max(dp[i], 1 + dp[j])
		# 由于是按照 第二维排序
		for i in range(1, len(intervals)):
			for j in range(i - 1, -1, -1):
				if intervals[i][0] >= intervals[j][1]:
					dp[i] = max(dp[i], 1 + dp[j])
					break
			dp[i] = max(dp[i], dp[i - 1])
		return len(intervals) - max(dp)

# 452. 用最少数量的箭引爆气球
# 把气球看成区间，几个箭可以全部射爆，意思就是有多少不重叠的区间。
# 注意这里重叠的情况也可以射爆。
# 最长数对链