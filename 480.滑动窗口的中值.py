class Solution(object):

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.res = []
        super().__init__()

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

        heapq.heappush(self.max_heap, -value)
        max_heap_top = -heapq.heappop(self.max_heap)

        heapq.heappush(self.min_heap, max_heap_top)
        if len(self.max_heap) + len(self.min_heap) & 1:  # 是否是奇数
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def get_middle(self):
        window_l = len(self.min_heap) + len(self.max_heap)
        if window_l & 1:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


import heapq


class Solution1(object):

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.res = []
        super().__init__()

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

        heapq.heappush(self.max_heap, -value)
        max_heap_top = -heapq.heappop(self.max_heap)

        heapq.heappush(self.min_heap, max_heap_top)
        if len(self.max_heap) + len(self.min_heap) & 1:  # 是否是奇数
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def get_middle(self):
        window_l = len(self.min_heap) + len(self.max_heap)
        if window_l & 1:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    s = Solution()
    s.medianSlidingWindow(nums, k)
