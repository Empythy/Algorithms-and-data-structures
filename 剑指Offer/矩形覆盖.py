# -*- coding:utf-8 -*-
"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""

class Solution:
    def rectCover(self, number):
        # write code here
        arr = [0, 1, 2]
        if number < 0:
            return None
        if number == 0:
            return arr[0]
        if number == 1:
            return arr[1]
        if number == 2:
            return arr[2]
        for i in range(3, number+1):
            arr.append(arr[i-1] + arr[i-2])
        return arr[number]

