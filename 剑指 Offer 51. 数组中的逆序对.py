# -*- coding: utf-8 -*-#
"""
Created on  2020/7/6  16:16 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from typing import List


class Solution:

    def __init__(self):
        self.ans = 0

    def reversePairs(self, nums: List[int]) -> int:
        print(self.merge_sort(nums))
        return self.ans

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            mid = len(nums) // 2
            left = self.merge_sort(nums[:mid])
            right = self.merge_sort(nums[mid:])
            return self.merge(left, right)

    def merge(self, nums1, nums2):
        left = 0
        right = 0
        new_arr = []
        while left < len(nums1) and right < len(nums2):
            if nums1[left] > nums2[right]:
                new_arr.append(nums2[right])  # 右边的值小
                self.ans += (len(nums1) - left)  # 注意坑
                right += 1
            else:
                new_arr.append(nums1[left])
                left += 1

        if left < len(nums1):
            new_arr.extend(nums1[left:])

        if right < len(nums2):
            new_arr.extend(nums2[right:])
        return new_arr


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0

        def merge(nums, start, mid, end):
            i, j, temp = start, mid + 1, []
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    self.cnt += mid - i + 1
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1

            for i in range(len(temp)):
                nums[start + i] = temp[i]

        def mergeSort(nums, start, end):
            if start >= end: return
            mid = (start + end) >> 1
            mergeSort(nums, start, mid)
            mergeSort(nums, mid + 1, end)
            merge(nums, start, mid, end)

        mergeSort(nums, 0, len(nums) - 1)
        return self.cnt

# class Solution():
#     def mergeSort(self, nums):
#
#         if len(nums) <= 1:
#             return nums
#         mid = len(nums) >> 1
#         left = self.mergeSort(nums[:mid])
#         right = self.mergeSort(nums[mid:])
#         return self.merge(left, right)
#
#     def merge(self, nums1, nums2):
#         new_arr = []
#         i, j = 0, 0
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] < nums2[j]:
#                 new_arr.append(nums1[i])
#                 i += 1
#             else:
#                 new_arr.append(nums2[j])
#                 j += 1
#
#         while i < len(nums1):
#             new_arr.append(nums1[i])
#             i += 1
#         while j < len(nums2):
#             new_arr.append(nums2[j])
#             j += 1
#         return new_arr


s = Solution()
ans = s.reversePairs([7, 5, 6, 4])
print(ans)
# ans = s.reversePairs([1, 3, 2, 3, 1])
print(ans)
