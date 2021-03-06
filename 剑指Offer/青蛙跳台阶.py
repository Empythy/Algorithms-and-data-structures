# -*- coding:utf-8 -*-
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""
class Solution:
    def jumpFloor(self, number):
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
