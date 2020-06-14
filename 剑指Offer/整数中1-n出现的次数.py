# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        preceise = 1
        highVal = 1
        count = 0
        sumNum = 0
        while highVal:
            highVal = n // (preceise * 10)
            midVal = (n // preceise) % 10
            lowVal = n % preceise

            preceise *= 10

            if midVal == 0:
                num = (highVal - 1 + 1) * pow(10, count)
            elif midVal > 1:
                num = (highVal + 1) * pow(10, count)
            else:
                num = highVal * pow(10, count) + lowVal + 1
            sumNum += num
            count += 1

        return sumNum
