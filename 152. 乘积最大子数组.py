# -*- coding: utf-8 -*-#
"""
Created on  2020/7/10  13:49 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1: return nums[0]

        n = len(nums)
        min_val = [0] * n
        max_val = [0] * n
        min_val[0] = nums[0]
        max_val[0] = nums[0]

        self.ans = max_val[0]

        for i in range(1, n):
            if nums[i] > 0:
                max_val[i] = max(max_val[i - 1] * nums[i], nums[i])
                min_val[i] = min(min_val[i - 1] * nums[i], nums[i])
            elif nums[i] < 0:
                max_val[i] = max(min_val[i - 1] * nums[i], nums[i])
                min_val[i] = min(max_val[i - 1] * nums[i], nums[i])
            self.ans = max(max_val[i], self.ans)

        return self.ans


if __name__ == "__main__":
    nums = [2, -1, 1, 1]
    s = Solution()
    ans = s.maxProduct(nums)
    print(ans)
