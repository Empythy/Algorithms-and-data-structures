# -*- coding: utf-8 -*-#
"""
Created on  2020/7/4  16:36 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""

import bisect
from collections import deque
class Solution():

	def midWindow(self, nums, k):
		ans = []
		is_odd = (k % 2) == 1
		windows = []  # 是拍好序的
		for i in range(k-1):
			bisect.insort(windows, nums[i])

		for i in range(k-1, len(nums)):
			bisect.insort(windows, nums[i])
			if is_odd:
				ans.append(windows[k//2])
			else:
				ans.append(
					(windows[k//2] + windows[(k-1)//2]) * 0.5
				)
			pop_item = nums[i-(k-1)]
			pop_index = bisect.bisect_left(windows, pop_item)
			windows.pop(pop_index)
		return ans

class Solution(object):

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.res = []

    def medianSlidingWindow(self, nums, k):
        for i in range(len(nums)):
            self.addnum(nums[i])
            if i >= k:
                if nums[i - k] in self.min_heap:
                    self.heap_delete(self.min_heap, nums[i - k])
                elif -nums[i - k] in self.max_heap:
                    self.heap_delete(self.max_heap, -nums[i - k])
                self.balance()
            if i >= k - 1:
                self.res.append(self.get_middle())
        return self.res

    def heap_delete(self, heap, value):
        if value == heap[-1]:
            return heap.pop()
        node_index = heap.index(value)

        heap[node_index] = heap[-1]
        heap.pop()
        heapq._siftup(heap, node_index)
        heapq._siftdown(heap, 0, node_index)

    def balance(self):
        odd = (len(self.max_heap) + len(self.min_heap)) & 1
        if odd:
            if len(self.max_heap) > len(self.min_heap):
                while len(self.max_heap) != len(self.min_heap) + 1:
                    heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            else:
                while len(self.max_heap) != len(self.min_heap) + 1:
                    heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        else:
            if len(self.max_heap) > len(self.min_heap):
                while len(self.max_heap) != len(self.min_heap):
                    heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            else:
                while len(self.max_heap) != len(self.min_heap):
                    heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def addnum(self, value):

        heapq.heappush(self.max_heap, -value) # 往最大堆加数据
        max_heap_top = -heapq.heappop(self.max_heap) # 最大堆顶的数字
        heapq.heappush(self.min_heap, max_heap_top)
        if len(self.max_heap) + len(self.min_heap) & 1: # 是否是奇数
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def get_middle(self):
        window_l = len(self.min_heap) + len(self.max_heap)
        if window_l & 1:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
solution = Solution()
ans = solution.midWindow(nums, k)
print(ans)