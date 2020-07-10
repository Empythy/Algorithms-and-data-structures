# -*- coding: utf-8 -*-#
"""
Created on  2020/7/9  20:24 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def split_arr(nums):
    """
    [0:pivot] 是左子树
    """
    root_val = nums[-1]

    pivot = -1

    for i in range(len(nums) - 1):
        if nums[i] < root_val:
            pivot += 1
        else:
            return pivot


def deseialize(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return TreeNode(arr[0])
    val = arr[-1]
    root = TreeNode(val)
    left = left_bound(arr[:-1], val)
    left_arr = []
    right_arr = []
    if left == -1:
        right_arr = arr[:-1]
    elif left == len(arr[:-1]):
        left_arr = arr[:-1]
    else:
        left_arr = arr[:left]
        right_arr = arr[left:-1]

    root.left = deseialize(left_arr)
    root.right = deseialize(right_arr)
    return root


def left_bound(arr, target):
    # 返回数组有多少个数比target 小
    if len(arr) == 0: return -1
    if arr[0] > target: return -1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    return left


nums = [1, 2, 3]
ans = left_bound(nums, 7)
print(ans)
