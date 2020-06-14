from typing import List

"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合
https://leetcode-cn.com/problems/subsets/solution/hui-su-si-xiang-tuan-mie-pai-lie-zu-he-zi-ji-wen-t/
"""

class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if (k <= 0 or n <= 0): return res

        def backtrack(n, k, start, track):
            if len(track) == k:
                res.append(track.copy())
                return
            for i in range(start, n+1):
                # 做选择
                track.append(i)
                backtrack(n, k, i + 1, track)
                track.pop()

        track = []
        backtrack(n, k, 1, track)
        return res



