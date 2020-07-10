# -*- coding: utf-8 -*-#
"""
Created on  2020/7/8  14:41 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from functools import lru_cache
from typing import List, Union


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> Union[int, float]:
#         if len(nums) == 0: return 0
#         if len(nums) == 1: return nums[0]
#
#         self.ans = float("-inf")
#
#         @lru_cache(None)
#         def dp(i):  # 返回 以 i 结尾的 子数组的最大和
#             if i == 0: return nums[0]
#             max_val = max(nums[i], nums[i] + dp(i - 1))
#             self.ans = max(self.ans, max_val)
#             return max_val
#         dp(len(nums) - 1)
#         return self.ans

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]

        self.ans = float("-inf")

        @lru_cache(None)
        def dp(i):  # 返回 以 i 结尾的 子数组的最大和
            if i == 0:
                return nums[0]
            max_val = max(nums[i], nums[i] + dp(i - 1))
            # self.ans = max(self.ans, max_val)
            return max_val

        for i in range(len(nums)):
            self.ans = max(self.ans, dp(i))
        return self.ans


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)


if __name__ == "__main__":
    nums = [-1, -2]
    # -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    ans = s.maxSubArray(nums)
    print(ans)
