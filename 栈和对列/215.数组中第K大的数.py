"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
"""
from typing import List

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = len(nums)
        if k >= n:
            min_heap = nums[:]
            heapq.heapify(min_heap)
            return min_heap[0]
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for i in range(k, n):
            if min_heap[0] < nums[i]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[i])
        return min_heap[0]