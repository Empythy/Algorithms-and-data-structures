# -*- coding: utf-8 -*-#
"""
Created on  2020/7/9  19:16 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from typing import List


def middle(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)

    left_k = (n1 + n2 + 1) // 2
    right_k = (n1 + n2 + 2) // 2
    left = findKth(nums1, nums2, left_k)
    if left_k == right_k:
        return left
    else:
        right = findKth(nums1, nums2, right_k)
        return (left + right) / 2.0


def findKth(nums1, nums2, k):
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 == 0 and n2 == 0:
        return
    elif n1 == 0:
        return nums2[k - 1]
    elif n2 == 0:
        return nums1[k - 1]
    if n1 > n2:
        return findKth(nums2, nums1, k - 1)
    if k == 1:
        return min(nums1[0], nums2[0])
    left = 0
    right = n1 - 1
    i = (left + right) // 2
    j = min(k - i, n2 - 1)
    if nums1[i] > nums2[j]:
        return findKth(nums1, nums2[j:], k - j)
    elif nums1[i] < nums2[j]:
        return findKth(nums1[i:], nums2, k - i)
    elif nums1[i] == nums2[j]:
        return nums1[i]


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
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

            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


def getKthElement(nums1, nums2, k):
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
    m = len(nums1)
    n = len(nums2)
    if m == 0:
        return nums2[k - 1]
    if n == 0:
        return nums1[k - 1]
    if k == 1:
        return min(nums1[0], nums2[0])

    pivot1 = nums1[k / 2 - 1]
    pivot2 = nums2[k / 2 - 1]
    pivot = min(pivot1, pivot2)
    if pivot == pivot1:
        return  getKthElement(nums1[k//2:], nums2, k - (k//2))

    if pivot == pivot2:
        return getKthElement(nums1, nums2[k//2:], k-( k//2))


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3]
    ans = middle(nums1, nums2)
    print(ans)
