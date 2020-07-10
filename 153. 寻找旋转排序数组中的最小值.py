# -*- coding: utf-8 -*-#
"""
Created on  2020/7/9  16:08 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""

"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
请找出其中最小的元素。
你可以假设数组中不存在重复元素。
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 0: return -1
        if len(nums) == 1: nums[0]

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left +(right - left) // 2
            if nums[mid] == nums[right]:
                right = right - 1
            elif nums[mid] > nums[right]:
                # 左边递增
                left = mid + 1
            elif nums[mid] < nums[right]:
                # 右边递增
                right = mid

        return nums[left]

    def findMin1(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if left == right: return nums[left] # left 和 right 位置重合
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]: right = mid
            elif nums[mid] > nums[right]: left = mid + 1
            elif nums[mid] == nums[right]: right = right - 1
        return -1
