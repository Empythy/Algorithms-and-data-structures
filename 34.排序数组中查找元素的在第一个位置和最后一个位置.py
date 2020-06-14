"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。
找出给定目标值在数组中的开始位置和结束位置。
"""
from typing import List
import bisect


def bisearch_left_bound(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    if left == len(arr): # target 比所有数都大
            return -1
    if arr[left] != target: # target 不存在
        return -1
    return left

def bisearch_right_bound(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) //2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1

    if left == 0:
        return -1

    if nums[left - 1] != target:
        return -1

    return left - 1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left = self.left_bound(nums, target)
        if left == -1:
            return [-1, -1]
        right = self.right_bound(nums, target)
        return [left, right]

    def left_bound(self, nums, target):
        left = bisect.bisect_left(nums, target)
        if left == len(nums): # target 比所有数都大
            return -1
        if nums[left] != target: # target 不存在
            return -1
        return left

    def right_bound(self, nums, target):
        left = bisect.bisect_right(nums, target)
        if left == 0:
            return -1
        if nums[left-1] != target:
            return -1

        return left - 1




if __name__ == "__main__":

    from random_data import RandomData
    s = Solution()
    for i in range(100000):
        try:
            nums = RandomData.sorted_arr_random_int()
            target = 3
            res = s.searchRange(nums, target)
            assert res[0] == bisearch_left_bound(nums, 3) and \
                res[1] ==bisearch_right_bound(nums, target)
            print("ok:\t", nums)
        except:
            print("bad cases:\t", nums)




