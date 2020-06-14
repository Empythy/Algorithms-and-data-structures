from typing import List

import bisect
"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，
返回它将会被按顺序插入的位置。你可以假设数组中无重复元素。"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """

        :param nums:
        :param target:
        :return:
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1

        return left

    def searchInsert_v1(self, nums: List[int], target: int) -> int:
        index = bisect.bisect(nums, target)
        return index


s = Solution()
# nums, target = [1, 3, 5, 6], 2
nums, target = [1, 3, 5, 6], 5
res1 = s.searchInsert(nums, target)
res2 = s.searchInsert_v1(nums, target)
print(res1)
print(res2)
