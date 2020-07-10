# -*- coding: utf-8 -*-#
"""
Created on  2020/7/7  10:54 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        min_stack = []  # 从底向上递减
        res = []
        for item in nums2[::-1]:

            while len(min_stack) > 0 and min_stack[-1] <= item:
                # 只要值比当前的item小  就pop
                min_stack.pop()

            if len(min_stack) > 0:
                res.append(min_stack[-1])
            else:
                res.append(-1)
            min_stack.append(item)

        data = dict(zip(nums2, res[::-1]))
        return [data[item] for item in nums1]

import heapq
import bisect
bisect.