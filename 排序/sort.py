# -*- coding: utf-8 -*-#
"""
Created on  2020/6/8  17:42 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""

import random

def create_random_arr(length):
    arr = [random.randint(0,10)
            for _ in range(length)]
    return arr
def test(func):
    for _ in range(10000):
        arr = create_random_arr(5)
        arr2 = arr.copy()
        arr1 = arr.copy()
        res = func(arr2)
        try:
            assert sorted(arr1) == res
        except AssertionError as e:
            print(f"bad cases: {arr}, result = {res}")
    print("OK")



def bubble_sort(arr):
    new_arr = arr.copy()
    n = len(new_arr)
    if n < 2:
        return new_arr
    for i in range(n):
        for j in range(0, n-i-1):
            if new_arr[j+1] < new_arr[j]: # 如果后面的值小
                new_arr[j+1], new_arr[j] = new_arr[j], new_arr[j+1]
    return new_arr





test(bubble_sort)
