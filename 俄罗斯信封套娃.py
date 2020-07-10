# -*- coding: utf-8 -*-#
"""
Created on  2020/6/28  23:46 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from typing import List


class Envelope(object):
	def __init__(self, w, h):
		self.w = w
		self.h = h

	# 重载 <
	# w1 < w2  True
	# w1 = w2
	def __lt__(self, other):
		if self.w == other.w:
			return self.h > other.h
		return self.w < other.w


class Solution:
	def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

		if len(envelopes) <= 1:
			return len(envelopes)
		new_envelopes = []
		for e in envelopes:
			new_envelopes.append(Envelope(*e))

		# envelopes.sort(key=lambda x: (x[0], -x[1]))

		new_envelopes.sort()
		dp = [1] * len(new_envelopes)

		max_cnt = 1
		for i in range(1, len(new_envelopes)):
			for j in range(i - 1, -1, -1):
				if new_envelopes[i].h > new_envelopes[j].h and dp[j] + 1 > dp[i]:
					dp[i] = 1 + dp[j]
			max_cnt = max(max_cnt, dp[i])

		return max_cnt


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
s = Solution()

res = s.maxEnvelopes(envelopes)
print(res)
