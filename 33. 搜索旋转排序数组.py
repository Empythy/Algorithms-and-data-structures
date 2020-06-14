"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:   # nums = [4, 5, 6, 7, 0, 1, 2]   2

                if nums[left] < nums[mid]:  # left -> mid 递增
                    if target >= nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[left] > nums[mid]:
                    right = mid - 1
                elif nums[left] == nums[mid]:
                    left = mid + 1

            elif nums[mid] < target:
                if nums[left] < nums[mid]:  # left -> mid 递增
                    left = mid + 1
                elif nums[left] > nums[mid]:
                    if target >= nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1

                elif nums[left] == nums[mid]:
                    left = mid + 1
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 2
s = Solution()
res = s.search(nums, target)
print(res)
assert res == len(nums) - 1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 4
res = s.search(nums, target)
assert res == 0

nums = [5, 1, 3]
target = 5
res = s.search(nums, target)
assert res == 0
nums = [5, 1, 3]
target = 3

res = s.search(nums, target)
print(res)
assert res == 2
