# -*- coding:utf-8 -*-
"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
"""
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row_cnt = len(array)
        col_cnt = len(array[0])
        i = 0
        j = col_cnt - 1
        while i <= row_cnt-1 and j >= 0:
            value = array[i][j]
            if value == target:
                return True
            elif value > target:
                j = j - 1
            else:
                i = i + 1
        return False
