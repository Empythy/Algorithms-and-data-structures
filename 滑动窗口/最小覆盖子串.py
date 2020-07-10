# -*- coding: utf-8 -*-#
"""
Created on  2020/7/3  9:19 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description: leetcode 76 最小覆盖子串
@version: V1
"""
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        needs = defaultdict(lambda: 0)
        window = defaultdict(lambda: 0)
        for ch in t: needs[ch] += 1
        left = 0
        right = 0

        match = 0   # 单词匹配的个数
        ans = 2 * len(s)  # 初始值

        while right < len(s):
            ch = s[right]   # 右边界字母
            if ch in needs:
                window[ch] += 1   # 如果字母在needs中
                if window[ch] == needs[ch]:  # 如果字母已经满足要求
                    match += 1

            right += 1  # 注意直接先 +1
            while match == len(needs):  # 如果满足要求
                if right - left < ans:  # 如果小于长度
                    start = left   # 记录起点
                    ans = right - left

                ch2 = s[left]  # 左指针往右移动
                if ch2 in needs:  # 如果属于子串字母
                    window[ch2] -= 1  # 将其个数-1
                    if window[ch2] < needs[ch2]: # 如果个数已经小于了
                        match -= 1  # 匹配的字母长度为1
                left += 1

        return s[start: start+ans] if ans < 2 * len(s) else ''

    def minWindow1(self, s: str, t: str) -> str:
        l = 0
        ans = s + s
        n = len(s)
        target = Counter(t)
        counter = defaultdict(lambda: 0)

        def contains(counter, target):
            if len(counter) < len(target):
                return False
            for k in counter:
                if k not in target or counter[k] < target[k]:
                    return False
            return True

        for r in range(n):
            if s[r] in target:
                counter[s[r]] += 1
            while l < n and contains(counter, target):
                if r - l + 1 < len(ans):
                    ans = s[l:r + 1]
                if s[l] in target:
                    counter[s[l]] -= 1
                l += 1
        return "" if ans == s + s else ans

s = 'abc'

t = 'abc'

solution = Solution()
ans = solution.minWindow(s, t)
print(ans)


dic = {
   'a' :2 ,
    'b' :1
}

dic1 = Counter('aab')
print(dic == dic1)