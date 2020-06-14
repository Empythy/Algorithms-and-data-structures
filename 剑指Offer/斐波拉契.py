# -*- coding:utf-8 -*-

"""
大家都知道斐波那契数列，现在要求输入一个整数n，
请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)
"""
class Solution:
    def Fibonacci(self, n):
        # write code here
        a, b = 0, 1

        if n == 0:
            return 0
        if n == 1:
            return 1

        for i in range(2, n+1):
            a, b = b, a+b
        return b
