import heapq
class MedianFinder:
    """
    如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
    那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
    那么中位数就是所有数值排序之后中间两个数的平均值。
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []


    def addNum(self, num: int) -> None:
        if self.max_heap and num >= -self.max_heap[0]:
            # 如果大堆不为空且num>大碓顶  应该小堆插入
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        self.balance()

    def balance(self):
        if len(self.min_heap) > len(self.max_heap):
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_heap_top)

        elif len(self.max_heap) - len(self.min_heap) > 1:
            max_heap_top = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, max_heap_top)


    def findMedian(self) -> float:
        if len(self.min_heap) != len(self.max_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2