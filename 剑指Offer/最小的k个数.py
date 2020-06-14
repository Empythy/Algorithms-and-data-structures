# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here

        def createMaxHeap(num):
            maxHeap.append(num)
            curIndex = len(maxHeap) - 1
            while curIndex != 0:
                parentIndex = (curIndex - 1) >> 1
                if maxHeap[parentIndex] < maxHeap[curIndex]:
                    maxHeap[parentIndex], maxHeap[curIndex] = maxHeap[curIndex], maxHeap[parentIndex]
                    curIndex = parentIndex
                else:
                    break

        def adjustMaxHeap(num):
            if num < maxHeap[0]:
                maxHeap[0] = num
            index = 0

            while index < len(maxHeap):
                leftIndex = 2 * index + 1
                rightIndex = 2 * index + 2
                largerIndex = 0
                if rightIndex < len(maxHeap):
                    if maxHeap[leftIndex] < maxHeap[rightIndex]:
                        largerIndex = rightIndex
                    elif maxHeap[rightIndex] < maxHeap[leftIndex]:
                        largerIndex = leftIndex

                elif rightIndex >= len(maxHeap) and leftIndex < len(maxHeap):
                    largerIndex = leftIndex

                else:
                    break

                if maxHeap[index] < maxHeap[largerIndex]:
                    maxHeap[index], maxHeap[largerIndex] = maxHeap[largerIndex], maxHeap[index]

                index = largerIndex

        if k <= 0 or len(tinput) < k:
            return []

        maxHeap = []

        for i in range(len(tinput)):
            if i < k:
                createMaxHeap(tinput[i])
            else:
                num = tinput[i]
                if num < maxHeap[0]:
                    adjustMaxHeap(num)

        return sorted(maxHeap)

if __name__ == '__main__':
    tinput = [4, 5, 1, 6, 2, 7, 3, 8]
    k = 4
    s = Solution()
    ret = s.GetLeastNumbers_Solution(tinput, k)
    print(ret)
