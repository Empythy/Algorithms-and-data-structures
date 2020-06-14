"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

2 3 1 1 4
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        index = 0
        for i in range(n):
            if i <= index:  #如果当前i比索引小，
                index = max(index, i + nums[i])
            if nums[i] + i > n - 1:
                return True

class Solution1:
    def canJump(self, nums: List[int]) -> bool:

        '''
        index = 0
        for i in range(len(nums)):
            if index >= len(nums)-1:return True
            if nums[i] == 0 and index <= i :return False
            index = i + nums[i] if i+nums[i] > index else index
        '''
        if len(nums) <= 1: return True               #特判
        index = 0  # 初始索引为0 跳的最远的位置
        for i in range(len(nums)):
            if i <= index:                          #如果当前i比索引小，
                index = max(index, i + nums[i])      #找到最大值
            if index >= len(nums) - 1:return True   #如果索引超过，返回True
        return False






