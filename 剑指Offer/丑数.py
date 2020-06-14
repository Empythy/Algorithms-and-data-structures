# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0

        uglyList = [1]
        count = 1
        twoPointer = 0
        threePointer = 0
        fivePointer = 0
        while count != index:
            minVal = min(2 * uglyList[twoPointer],
                         3 * uglyList[threePointer],
                         5 * uglyList[fivePointer])

            if minVal == 2 * uglyList[twoPointer]:
                twoPointer += 1
            if minVal == 3 * uglyList[threePointer]:
                threePointer += 1
            if minVal == 5 * uglyList[fivePointer]:
                fivePointer += 1
            count += 1
            uglyList.append(minVal)

        return uglyList[index-1]
