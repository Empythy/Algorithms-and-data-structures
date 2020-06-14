from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = float('-inf')
        i = 0
        j = n-1
        while i<j and i>=0:
            res = max(res,
                min(height[i], height[j]) * (j - i)
                )
        return res
