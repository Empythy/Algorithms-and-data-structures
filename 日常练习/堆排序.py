# -*- coding: utf-8 -*-#
"""
Created on  2020/7/1  20:23   完成时间 45 分钟
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from common import RandomArr
import heapq


def swap(nums, i, j):
	nums[i], nums[j] = nums[j], nums[i]


def heap_insert(nums, index):
	# 每次往最后插入一个数  然后大的上浮
	parent = (index - 1) // 2

	while nums[index] > nums[parent] and index > 0:
		swap(nums, index, parent)  # 满足 条件则与父节点进行交换
		index = parent
		parent = (index - 1) // 2 #


def heapify(nums, n, index):
	# n 调整的最大index的值
	# 每次从首个数字开始  该数字小就下沉
	l = 2 * index + 1
	r = 2 * index + 2
	largest = index
	# 如果左右孩子没有超过范围
	if l < n and nums[l] > nums[index]:
		largest = l
	if r < n and nums[r] > nums[index] and nums[r] > nums[l]:
		largest = r

	while largest != index: # 如果最大值不是当前节点
		swap(nums, index, largest)  # 交换二者的位置
		index = largest  # 更新index 继续比较是否需要下沉
		heapify(nums, n, index)


def heap_sort(nums) -> None:
	if len(nums) <= 1:
		return
	for i in range(len(nums)):
		heap_insert(nums, i)
	print("最大堆是", nums)

	for size in range(len(nums) - 1, 0, -1):
		swap(nums, 0, size)  # 每次将堆顶元素和最后一个元素交换
		heapify(nums, size, 0)

def test_heap_sort():
	for i in range(10000):
		arr = RandomArr.arr_random_int(1, 10, 6)
		new_arr = arr.copy()
		new_arr.sort()
		heap_sort(arr)
		print("heap sorted arr is ", arr)
		print("sorted arr is", new_arr)
		assert arr == new_arr
		print("============================")


class MinHeap(object):
	# 创建最小堆
	def __init__(self, nums):
		self.nums = nums
		self.heapify()

	def swap(self, i, j):
		self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

	def _up(self, index):
		parent = (index - 1) // 2
		# 子节点 < 父节点的值
		# 注意父节点的值
		while index > 0 and parent >= 0 and \
				self.nums[index] < self.nums[parent]:
			self.swap(index, parent)
			index = parent  # 继续往上冒泡
			self._up(index)

	def _down(self, size, index):
		l = 2 * index + 1
		r = 2 * index + 2
		smallest = index
		if l < size and self.nums[index] > self.nums[l]:
			smallest = l
		if r < size and self.nums[index] > self.nums[r] \
				and self.nums[r] < self.nums[l]:
			smallest = r

		while smallest != index:
			self.swap(index, smallest)
			index = smallest
			self._down(size, index)

	def heapify(self):

		for index in range(len(self.nums)):
			self._up(index)

	def pop(self):
		self.swap(0, len(self.nums) - 1)
		num = self.nums.pop()
		self._down(len(self.nums), 0)
		return num

	def append(self, item):
		self.nums.append(item)
		self._up(len(self.nums)-1)

def _():
	for _ in range(10000):
		arr = RandomArr.arr_random_int(1, 6, 6)
		print("orin arr", arr)
		new_arr = arr.copy()
		heapq.heapify(arr)
		min_heap = MinHeap(new_arr)
		print("self define min heap", min_heap.nums)
		print("heapq", arr)
		for i in range(len(arr)):
			assert heapq.heappop(arr) == min_heap.pop()
		print("==========================")


if __name__ == "__main__":
	# arr = [5, 1, 9, 2, 7, 9]
	# print("orin arr", arr)
	# new_arr = arr.copy()
	# heapq.heapify(arr)
	# min_heap = MinHeap(new_arr)
	# print("self define min heap", min_heap.nums)
	# print("heapq", arr)
	# for i in range(len(arr)):
	# 	assert heapq.heappop(arr) == min_heap.pop()
	# print("==========================")
	arr = [3,2,4,1,6,7]

	heapq.heapify(arr)
