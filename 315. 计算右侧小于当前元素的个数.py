from typing import List
import bisect


class Solution:
    def lower_bound(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1

        return left

    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n==0:
            return []
        if n==1:
            return [0]
        sorted_nums = [nums[n-1]]
        ans = [0]
        for index in range(n-2, -1, -1):
            insert_index = bisect.bisect_left(sorted_nums, nums[index])
            print(insert_index)
            # insert_index = self.lower_bound(sorted_nums, nums[index])

            ans.append(insert_index)
            bisect.insort_left(sorted_nums, nums[index])
            # sorted_nums.insert(insert_index, nums[index])
        return ans[::-1]



s = Solution()
nums = [5,2,6,1]
# [1], 0   0
# [1], 1   0
# [1], 2   1


# res = s.lower_bound([1], 2)
# print(res)
res = s.countSmaller(nums)
print(res)