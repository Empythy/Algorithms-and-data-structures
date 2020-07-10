# -*- coding: utf-8 -*-#
"""
Created on  2020/7/8  23:51 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return - 1
        if len(nums) == 1:
            return -1 if nums[0] != target else 0
        index = self.findMin(nums)
        # [0-index) [index:] 为有序数组
        left = self.left_bound(nums[:index], target)
        right = self.left_bound(nums[index:], target)
        if left == -1 and right == -1:
            return -1
        elif left == -1 and right != -1:
            return right + index
        elif left != -1:
            return left

    # def search_rotate_point(self, nums):
    #     if len(nums) == 0: return -1
    #     if len(nums) == 1: return 0
    #     if len(set(nums)) == 1: return 0
    #     left = 0
    #     right = len(nums) - 1
    #     while left <= right:
    #         mid = left + (right - left) >> 1
    #         if nums[mid] > nums[right]:
    #             # 左侧为递增区间 旋转点在右边
    #             left = mid + 1
    #         elif nums[mid] < nums[right]:
    #             # 右侧为递增区间
    #             right = mid
    #         elif nums[mid] == nums[right]:
    #             # 无法判断
    #             right = right - 1
    #     return left
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 0: return -1
        if len(nums) == 1: return 0

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == nums[right]:
                right = right - 1

            elif nums[mid] > nums[right]:
                # 左边递增
                left = mid + 1

            elif nums[mid] < nums[right]:
                # 右边递增
                right = mid

        return left

    def left_bound(self, nums, target):
        if len(nums) == 0: return -1
        if len(nums) == 1: return -1 if nums[0] != target else 0
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) >> 1
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        if left == len(nums) or nums[left] != target:
            return -1

        return left


if __name__ == "__main__":
    # nums = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    # nums = [1, 1, 1, 1, 1, 2, 1, 1, 1]

    # nums = [5, 5, 5, 1, 2, 3, 4, 5]
    # nums = [-47, -42, -42, -42, -39, -36, -35, -33, -33, -32, -31, -28, -27, -26, -25, -24, -24, -19, -14, -7, -3, 1, 8,
    #         8, 13, 14, 14, 15, 16, 17, 19, 21, 24, 25, 27, 28, 32, 33, 36, 39, 39, 43, 46, 46, 49, 55, 56, 58, 62, 63,
    #         64, -62, -62, -60, -60, -58, -58, -57, -57, -53, -52, -51, -51, -47]
    s = Solution()
    nums = [1, 1, 1, 1, 1, 2, 1, 1, 1]
    ans = s.search(nums, 644986612)
    print(ans)
