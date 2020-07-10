# -*- coding: utf-8 -*-#
"""
Created on  2020/6/14  1:07 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""

import bisect
import itertools
import random


class RandomArr(object):
	@classmethod
	def arr_random_int(cls, start: int = 1, end: int = 10, length: int = 6):
		"""

		"""
		# random.randint(a, b)  生成[a, b]之间的随机数
		endpoint = random.randint(0, length)
		arr = [random.randint(start, end)
		       for _ in range(endpoint)]

		return arr

	@classmethod
	def sorted_arr_random_int(cls, start=1, end=10, length=6):
		arr = cls.arr_random_int(start, end, length)
		arr.sort()
		return arr

	@classmethod
	def unique_arr_random_int(cls, start=1, end=10, length=6):
		arr = cls.arr_random_int(start, end, length)
		arr = list(set(arr))
		return arr

	@classmethod
	def sorted_unique_arr_random_int(cls, start=1, end=10, length=6):
		arr = cls.arr_random_int(start, end, length)
		arr = list(set(arr))
		arr.sort()
		return arr

	@classmethod
	def permute(cls, nums):
		return list(itertools.permutations(nums))

	@classmethod
	def compare_arr(cls, arr1, arr2, order=True):
		if order:
			return arr1 == arr2
		else:
			return len(arr1) == len(arr2) and set(arr1) == set(arr2)

	@classmethod
	def left_bound_with_sorted_arr(self, nums, target):
		"""
		给定有序数组和target 查找有序数组的最左边界, 如果不存在返回 -1
		:param nums:
		:param target:
		:return:
		"""
		left = bisect.bisect_left(nums, target)
		if left == len(nums):  # target 比所有数都大
			return -1
		if nums[left] != target:  # target 不存在
			return -1
		return left

	@classmethod
	def right_bound_with_sorted_arr(self, nums, target):
		# 给定有序数组和target
		# 查找有序数组的最右边界  如果不存在返回 -1
		left = bisect.bisect_right(nums, target)
		if left == 0:
			return -1
		if nums[left - 1] != target:
			return -1
		return left - 1
