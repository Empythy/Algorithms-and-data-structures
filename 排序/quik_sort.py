# -*- coding: utf-8 -*-#
"""
Created on  2020/7/7  16:03 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""

import random
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    index = random.randint(0, len(arr))
    povit = arr[index]
    left = [item for item in arr if item < povit]
    mid = [item for item in arr if item == povit]
    right = [item for item in arr if item < povit]
    return quick_sort(left) + mid + right


def heap_insert(arr, index):
    parent = (index - 1) // 2

    while index > 0 and arr[index] > arr[parent]:
        arr[index], arr[parent] = arr[parent], arr[index]
        index = parent
        parent = (index - 1) // 2


def heapify(arr, size, index):  #
    # 从 index arr[index] 开始调整位置
    left = 2 * index + 1
    while left < size:
        right = left + 1
        largest = index
        if arr[left] > arr[index]:
            largest = left
        if right < size and arr[right] > arr[left] and arr[right] > arr[index]:
            largest = right

        if largest == index:
            break
        elif largest == left:
            arr[index], arr[left] = arr[left], arr[index]
            index = left
        else:
            arr[index], arr[right] = arr[right], arr[index]
            index = right

        left = index * 2 + 1


def heap_sort(arr):
    if len(arr) <= 1:
        return arr
    for i in range(len(arr)):
        heap_insert(arr, i)

    size = len(arr)
    arr[0], arr[size - 1] = arr[size - 1], arr[0]  # 注意细节
    for i in range(size - 1, 0, -1):
        heapify(arr, i, 0)
        arr[0], arr[i - 1] = arr[i - 1], arr[0]


if __name__ == "__main__":
    from common import RandomArr

    for i in range(100000):
        arr = RandomArr.arr_random_int(end=4)
        print(arr)
        arr_c = arr.copy()
        heap_sort(arr)
        assert arr == sorted(arr_c)
