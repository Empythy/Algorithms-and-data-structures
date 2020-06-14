from functools import lru_cache

"""
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，
从而将其表示为二叉树。
"""


class Solution:
    @lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                # 未交换节点
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                # 交换节点
                return True
        return False
