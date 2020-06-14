from collections import Counter, defaultdict

"""
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
"""


class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        n = len(s)
        l, r = 0, 0
        target = Counter(t)
        counter = defaultdict(lambda: 0)
        ans = s + s

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
                    # 如果当前长度小于 之前的ans的长度 更新ans
                    ans = s[l:r + 1]
                if s[l] in target:
                    # 如果left的字符在target中 删除
                    counter[s[l]] -= 1
                l += 1

        return "" if ans == s + s else ans
