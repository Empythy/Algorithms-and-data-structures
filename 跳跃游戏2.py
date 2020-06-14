from typing import List


class Solution:

    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        n = len(nums)
        step = 0
        furthest = 0
        end = 0
        for i in range(n):
            furthest = max(furthest, i + nums[i])
            # 计算在i位置上最远的位置
            if furthest >= n - 1:
                return step + 1  # 跳
            if furthest <= i:
                return -1
            if i == end:
                step += 1  # 跳
                end = furthest