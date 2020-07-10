# -*- coding: utf-8 -*-#
"""
Created on  2020/7/9  20:02 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return self.getKthElement(nums1, nums2, (totalLength + 1) // 2)
        else:
            return (
                           self.getKthElement(nums1, nums2, (totalLength + 1) // 2) +
                           self.getKthElement(nums1, nums2, (totalLength + 2) // 2)
                   ) / 2

    # def getKthElement(self, nums1, nums2, k):
    #     """
    #     - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
    #     - 这里的 "/" 表示整除
    #     - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
    #     - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
    #     - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
    #     - 这样 pivot 本身最大也只能是第 k-1 小的元素
    #     - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
    #     - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
    #     - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
    #     """
    #     m, n = len(nums1), len(nums2)
    #     index1, index2 = 0, 0
    #     while True:
    #         # 特殊情况
    #         if index1 == m:
    #             return nums2[index2 + k - 1]
    #         if index2 == n:
    #             return nums1[index1 + k - 1]
    #         if k == 1:
    #             return min(nums1[index1], nums2[index2])
    #
    #         # 正常情况
    #         newIndex1 = min(index1 + k // 2 - 1, m - 1)
    #         newIndex2 = min(index2 + k // 2 - 1, n - 1)
    #
    #         pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
    #         if pivot1 <= pivot2:
    #             k -= newIndex1 - index1 + 1
    #             index1 = newIndex1 + 1
    #         else:
    #             k -= newIndex2 - index2 + 1
    #             index2 = newIndex2 + 1
    def getKthElement(self, nums1, nums2, k):
        """
        - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
        - 这里的 "/" 表示整除
        - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
        - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
        - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
        - 这样 pivot 本身最大也只能是第 k-1 小的元素
        - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
        - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
        - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
        """
        m, n = len(nums1), len(nums2)
        if m == 0: return nums2[k - 1]

        if n == 0: return nums1[k - 1]
        if k == 1: return min(nums1[0], nums2[0])

        middle = min(0, k // 2 - 1)

        pivot1, pivot2 = nums1[middle], nums2[middle]
        if pivot1 <= pivot2:
            return self.getKthElement(nums1[middle + 1:], nums2, k - middle - 1)
        else:
            return self.getKthElement(nums1, nums2[middle + 1:], k - middle - 1)


nums1 = [1]
nums2 = [2, 3, 4, 5, 6]
s = Solution()
ans = s.findMedianSortedArrays(nums1, nums2)
print(ans)
