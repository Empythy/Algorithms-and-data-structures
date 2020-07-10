# -*- coding: utf-8 -*-#
"""
Created on  2020/7/8  23:12 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from typing import List


# class Solution:
#     def minArray(self, numbers: List[int]) -> int:
#
#         if len(numbers) == 1: return numbers[0]
#         if len(numbers) == 2: return min(numbers)
#         left = 0
#         right = len(numbers) - 1
#         mid = left + (right - left) >> 1
#         if numbers[left] < numbers[mid]:  # 左半部分 上升
#             return min(numbers[left], self.minArray(numbers[mid:]))
#
#         if numbers[left] > mid:  # 右半部分是上升的
#             return min(numbers[mid], self.minArray(numbers[:mid]))
#
#         if numbers[left] == numbers[mid]:
#             return min(self.minArray(numbers[left + 1:]), numbers[left])
class Solution:
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

if __name__ == "__main__":
    # arr = [2, 2, 2, 0, 1]  # l=0 right=4 mid=2
    arr = [2, 2, 2, 0, 0, 1, 2, 2]
    s = Solution()
    ans = s.findMin(arr)
    print(ans)