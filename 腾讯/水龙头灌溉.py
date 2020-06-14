from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        nums = [0] * (n + 1)
        for i in range(n):
            left = max(i - ranges[i], 0)
            right = min(i + ranges[i], n)
            if (nums[left] < right - left):
                nums[left] = right - left
        print(nums) # 获得 能跳到最远的位置
        # [5, 2, 2, 0, 0, 0]
        return self.jump(nums)


    def jump(self, nums):
        n = len(nums)
        furthest = 0
        steps = 0
        end = 0
        for i in range(n):
            # 过去时刻包括当前i时刻 跳的最远的位置  尝试
            furthest = max(furthest, i + nums[i])
            if furthest >= n-1: # 如果能调到最远位置
                return steps + 1   # 跳
            if furthest <= i: # 如果最远的位置小于当前位置 则返回 -1
                return -1
            if i == end: # 必须要跳
                steps += 1
                end = furthest

    def test(self):
        nums = [3, 4, 1, 1, 0, 0]
        n = 5
        ans = self.minTaps(n, nums)
        # nums = [5, 2, 2, 0, 0, 0]
        return ans





