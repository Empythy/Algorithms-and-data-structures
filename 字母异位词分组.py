# -*- coding: utf-8 -*-#
"""
Created on  2020/7/3  13:05 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description: leetcode 49 字母异分位词分组
			所有输入均为小写字母 
@version: V1
"""
import collections
from typing import List

from collections import defaultdict, Counter


class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		# 以某个字符串为 key  效率不高
		ans = defaultdict(list)
		for item in strs:
			for k, v in ans.items():
				if Counter(item) == Counter(k):  # 如果判断已经出现过
					ans[k].append(item)
					break
			else:  # 如果没有执行过 for循环里面的语句
				ans[item].append(item)
		return list(ans.values())

	# 重点在于根据字符串生成 key 使得get操作的为O(1)
	def groupAnagrams1(self, strs):
		"""可行解"""
		ans = collections.defaultdict(list)
		for s in strs:
			ans[tuple(sorted(s))].append(s) # n * k log k
		return ans.values()

	def groupAnagrams2(self, strs):
		ans = collections.defaultdict(list)
		for s in strs:
			count = [0] * 26
			for c in s:
				count[ord(c) - ord('a')] += 1
			ans[tuple(count)].append(s) # 将其转换为tuple变成可hash的对象
		return ans.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
ans = solution.groupAnagrams1(strs)
print(ans)
