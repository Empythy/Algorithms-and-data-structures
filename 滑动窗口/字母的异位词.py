# -*- coding: utf-8 -*-#
"""
Created on  2020/7/3  22:29 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。


@version: V1
"""
from collections import Counter, defaultdict
from typing import List

class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:

		ans = []
		window = defaultdict(lambda : 0)
		needs = Counter(p)
		left, right = 0, 0
		match = 0
		while right < len(s):
			ch1 = s[right]
			if ch1 in needs:
				window[ch1] += 1
				if window[ch1] == needs[ch1]:
					match += 1
			right += 1

			while match == len(needs): # 如果满足要求  左指针往右移动
				if right - left == len(p):
					ans.append(left)

				ch2 = s[left]
				if ch2 in needs:
					window[ch2] -= 1
					if window[ch2] < needs[ch2]:
						match -= 1
				left += 1
		return ans

	def findAnagrams(self, s: str, p: str) -> List[int]:
		needs = Counter(p)
		window = defaultdict(lambda: 0)
		left, right = 0, 0
		ans = []
		match = 0

		while right < len(s):
			ch1 = s[right]
			if ch1 in needs:
				window[ch1] += 1

				if window[ch1] == needs[ch1]:
					match += 1
			right += 1

			while match == len(needs):
				if right - left == len(p):
					ans.append(left)

				ch2 = s[left]
				if ch2 in needs:
					window[ch2] -= 1

					if window[ch2] < needs[ch2]:
						match -= 1
				left += 1

		return ans


if __name__ == "__main__":
	s = "cbaebabacd"
	p = "abc"
	solution = Solution()
	ans = solution.findAnagrams(s, p)
	print(ans)