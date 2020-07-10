# -*- coding: utf-8 -*-#
"""
Created on  2020/7/4  11:59 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from typing import List


## 注意  left + ((right - left) >> 1)  需要加括号  有坑
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.find_left(nums, target)
        if left == -1:
            return [-1, -1]
        right = self.find_right(nums, target)
        return [left, right]

    def find_left(self, nums, target) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:  # [left, left+1] -- > stop
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        if left == len(nums) or nums[left] != target:
            return -1

        return left

    def find_right(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        while left <= right:  # [left, left+1] -- > stop
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if left == 0 or nums[left - 1] != target:
            return -1

        return left - 1


import bisect


def search_range(nums, target):
    def left():
        index = bisect.bisect_left(nums, target)
        if index == len(nums): return -1
        if nums[index] != target: return -1
        return index

    def right():
        index = bisect.bisect_right(nums, target)
        if index == 0: return -1
        if nums[index - 1] != target: return -1
        return index - 1

    return [left(), right()]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    solution = Solution()
    ans = solution.searchRange(nums, target)
    print(ans)
    ans = search_range(nums, target)
    print(ans)
