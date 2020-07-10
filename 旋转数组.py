# -*- coding: utf-8 -*-#
"""
Created on  2020/7/8  21:38 
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
            return -1
        left, right = 0, len(nums) - 1
        while left < right:  # 循环结束条件left==right
            mid = (left + right) >> 1
            if nums[left] < nums[mid]:  # 如果左值小于中值，说明左边区间升序
                if nums[left] <= target <= nums[mid]:  # 如果目标在左边的升序区间中，右边界移动到mid
                    right = mid
                else:  # 否则目标在右半边，左边界移动到mid+1
                    left = mid + 1
            elif nums[left] > nums[mid]:  # 如果左值大于中值，说明左边不是升序，右半边升序
                if nums[left] <= target or target <= nums[mid]:  # 如果目标在左边，右边界移动到mid
                    right = mid
                else:  # 否则目标在右半边的升序区间中，左边界移动到mid+1
                    left = mid + 1
            elif nums[left] == nums[mid]:  # 如果左值等于中值，可能是已经找到了目标，也可能是遇到了重复值
                if nums[left] != target:  # 如果左值不等于目标，说明还没找到，需要逐一清理重复值
                    left += 1
                else:  # 如果左值等于目标，说明已经找到最左边的目标值
                    right = left  # 将右边界移动到left，循环结束
        return left if nums[left] == target else -1  # 返回left，或者-1


def left_bound(arr, target):
    if len(arr) == 0: return -1

    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) >> 1
        if arr[mid] == target:
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1

    if left == len(arr): return -1

    return left if arr[left] == target else -1

