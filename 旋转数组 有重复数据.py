# -*- coding: utf-8 -*-#
"""
Created on  2020/7/9  15:50 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""


class Solution():

    def search(self, nums, target):

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target: return True

            if nums[mid] < nums[right] or \
                    nums[mid] == nums[right] and nums[left] > nums[mid]:
                # 右边有序

                if nums[mid] <= target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            elif nums[mid] > nums[right] or \
                    nums[mid] == nums[right] and nums[left] < nums[mid]:
                # 左边有序
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right = right - 1

        return False
