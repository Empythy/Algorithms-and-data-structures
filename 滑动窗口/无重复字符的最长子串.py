# -*- coding: utf-8 -*-#
"""
Created on  2020/7/3  22:46 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from collections import defaultdict


class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		if len(s) <= 1:
			return len(s)
		left, right = 0, 0
		ans = 0
		window = defaultdict(lambda :0)

		while right < len(s):
			ch1 = s[right]
			window[ch1] += 1
			right += 1  # 右指针往右移动
			while window[ch1] > 1:  # 如果有重复字符
				ch2 = s[left]
				window[ch2] -= 1  # 将字符个数 -1
				left += 1  # 指针往左移动
			ans = max(ans, right-left)

		return ans


if __name__ == '__main__':
	s = "abcabcbb"
	solution = Solution()
	ans = solution.lengthOfLongestSubstring(s)
	print(ans)


