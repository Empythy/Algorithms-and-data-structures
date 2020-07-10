# -*- coding: utf-8 -*-#
"""
Created on  2020/6/28  14:02
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com
@Description:
@version: V1
"""
from typing import List


def heap_insert(arr: List, index: int) -> None:
	"""
	构建最大堆  每次插入一个点 然后递归的比较 其与父节点的值 如果大 则上浮
	:param arr:
	:param index:
	:return:
	"""
	# 当前节点大于父节点的值  一直往上冒泡
	# 注意 index 必须大于0  (0-1) //2 = -1
	while arr[index] > arr[(index - 1) // 2] and index > 0:
		parent = (index - 1) // 2
		swap(arr, index, parent)
		index = (index - 1) // 2


def heapify(arr: List, index: int, size: int) -> None:
	"""

	:param arr:
	:param index: 要调整的位置 进行下沉 判断左右节点 谁大进行交换 继续下沉
	:param size: 堆的长度
	:return:
	"""
	left = index * 2 + 1
	while left < size:
		largest = left
		# 如果右孩子存在
		if left + 1 < size and arr[left+1] > arr[left]:
			largest = left + 1
		if arr[largest] > arr[index]:
			largest = largest
		else:
			largest = index

		if largest == index:
			break

		arr[largest], arr[index] = arr[index], arr[largest]
		index = largest # 更新 index位置
		left = index * 2 + 1


def heap_sort(arr: List) -> None:
	if len(arr) < 2:
		return
	# 循环增加每个元素 构建最大堆
	for i in range(len(arr)):
		heap_insert(arr, i)

	size = len(arr)
	swap(arr, 0, size-1)
	size -= 1

	while size > 0:
		heapify(arr, 0, size)
		swap(arr, 0, size-1)
		size -= 1

def swap(arr, i, j):
	t = arr[i]
	arr[i] = arr[j]
	arr[j] = t


if __name__ == '__main__':
	from common import RandomArr

	for i in range(100000):
		arr = RandomArr.arr_random_int()
		print("orin arr is: \t", arr)
		orin_arr = arr.copy()
		orin_arr.sort()  # 就地修改
		print("sorted arr is: \t", orin_arr)
		heap_sort(arr)  # 就地修改
		print("heap sorted arr is:\t", arr)
		assert orin_arr == arr
		print("===============")