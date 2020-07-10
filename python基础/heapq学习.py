# -*- coding: utf-8 -*-#
"""
Created on  2020/7/1  22:35 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from common import RandomArr
import heapq


arr = RandomArr.arr_random_int(end=4)
heapq._heapify_max(arr)
print(arr)

