# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.littleValMaxHeap = []
        self.bigValMinHeap = []
        self.maxHeapCnt = 0
        self.minHeapCnt = 0

    def Insert(self, num):
        # write code here
        print("insert data", num)
        if self.minHeapCnt < self.maxHeapCnt:
            """最小堆插入数据 先要比较插入值与最大堆堆顶的"""
            self.minHeapCnt += 1
            print("self.minHeapCnt", self.minHeapCnt)
            if num < self.littleValMaxHeap[0]:
                tmpNum = self.littleValMaxHeap[0]  # 获取最大堆的堆顶
                print("最大堆堆顶数据为:", self.littleValMaxHeap[0])
                print("调整最大堆的数据", num)
                self.adjustMaxHeap(num)
                num = tmpNum
            print("插入最小堆", num)
            self.createMinHeap(num)

        else:
            self.maxHeapCnt += 1
            # 最大堆为空 直接插入最大堆
            if len(self.littleValMaxHeap) == 0:
                self.createMaxHeap(num)
            else:
                """最大堆插入数据 先要比较插入值与最小堆堆顶的"""
                if self.bigValMinHeap[0] < num:
                    tmpNum = self.bigValMinHeap[0]
                    print("最小堆堆顶数据为:", self.bigValMinHeap[0])
                    print("调整最小堆的数据", num)
                    self.adjustMinHeap(num)
                    self.createMaxHeap(tmpNum)
                else:
                    self.createMaxHeap(num)

    def GetMedian(self):
        # write code here
        if self.maxHeapCnt == self.minHeapCnt:
            return (self.littleValMaxHeap[0] + self.bigValMinHeap[0]) / 2
        else:
            return self.littleValMaxHeap[0]

    def createMaxHeap(self, num):
        self.littleValMaxHeap.append(num)
        tmpIndex = len(self.littleValMaxHeap) - 1
        while tmpIndex:
            parentIndex = (tmpIndex - 1) >> 1
            if self.littleValMaxHeap[parentIndex] < self.littleValMaxHeap[tmpIndex]:
                self.littleValMaxHeap[parentIndex], self.littleValMaxHeap[tmpIndex] = self.littleValMaxHeap[tmpIndex], \
                                                                                      self.littleValMaxHeap[parentIndex]
            else:
                break
            tmpIndex = parentIndex

    def adjustMaxHeap(self, num):

        if num < self.littleValMaxHeap[0]:
            self.littleValMaxHeap[0] = num
        index = 0

        while index < len(self.littleValMaxHeap):
            leftIndex = 2 * index + 1
            rightIndex = 2 * index + 2
            largerIndex = 0

            if rightIndex < len(self.littleValMaxHeap):
                if self.littleValMaxHeap[leftIndex] < self.littleValMaxHeap[rightIndex]:
                    largerIndex = rightIndex

                elif self.littleValMaxHeap[rightIndex] < self.littleValMaxHeap[leftIndex]:
                    largerIndex = leftIndex

            elif leftIndex < len(self.littleValMaxHeap):
                # rightIndex >= len(self.littleValMaxHeap) and
                largerIndex = leftIndex
            else:
                break

            if self.littleValMaxHeap[index] < self.littleValMaxHeap[largerIndex]:
                self.littleValMaxHeap[index], self.littleValMaxHeap[largerIndex] = \
                    self.littleValMaxHeap[largerIndex], self.littleValMaxHeap[index]
            index = largerIndex

    def createMinHeap(self, num):
        self.bigValMinHeap.append(num)
        tmpIndex = len(self.bigValMinHeap) - 1
        while tmpIndex:
            parentIndex = (tmpIndex - 1) >> 1
            if self.bigValMinHeap[tmpIndex] < self.bigValMinHeap[parentIndex]:
                self.bigValMinHeap[parentIndex], self.bigValMinHeap[tmpIndex] = self.bigValMinHeap[tmpIndex], \
                                                                                self.bigValMinHeap[parentIndex]
            else:
                break
            tmpIndex = parentIndex

    def adjustMinHeap(self, num):
        print("adjustMinHeap of num is", num)
        if self.bigValMinHeap[0] < num:
            self.bigValMinHeap[0] = num

        tmpIndex = 0
        while tmpIndex < len(self.bigValMinHeap):
            leftIndex = (tmpIndex << 1) + 1
            rightIndex = (tmpIndex << 1) + 2
            smallerIndex = 0
            if rightIndex < len(self.bigValMinHeap):
                if self.bigValMinHeap[rightIndex] < self.bigValMinHeap[leftIndex]:
                    smallerIndex = rightIndex
                else:
                    smallerIndex = leftIndex

            elif leftIndex < len(self.bigValMinHeap):
                smallerIndex = leftIndex

            else:
                break

            if self.bigValMinHeap[smallerIndex] < self.bigValMinHeap[tmpIndex]:
                self.bigValMinHeap[tmpIndex], self.bigValMinHeap[smallerIndex] = self.bigValMinHeap[smallerIndex], \
                                                                                 self.bigValMinHeap[tmpIndex]
            tmpIndex = smallerIndex


if __name__ == '__main__':
    ls = [5, 2, 3, 4, 1, 6, 7, 0, 8]
    s = Solution()
    for i in range(len(ls)):
        s.Insert(ls[i])
        print(ls[:i + 1])
        print(s.GetMedian())
        print("最大堆:\t", s.littleValMaxHeap)
        print("最小堆:\t", s.bigValMinHeap)
        print("*" * 30)
