from typing import List


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#
#         n = len(nums)
#         tmp = 0
#         res = 0
#         for i in range(n):
#             tmp += nums[i]
#             if tmp < 0:
#                 res = max(res, tmp - nums[i])
#                 tmp = 0
#             res = max(res, tmp)
#         res = max(res, tmp)
#         return res
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tmp = nums[0] # 当前和
        max_ = tmp # 当前最大值
        n = len(nums)
        for i in range(1, n):
            # 当 当前序列加上此时的元素的值小的值，
            # 说明最大序列和可能出现在后续序列中，记录此时的最大值
            if tmp + nums[i] > nums[i]:
                max_ = max(max_, tmp + nums[i])
                tmp = tmp + nums[i]
            else:
            #当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
            # 并记录此时的最大值
                max_ = max(max_,
                           tmp,  # 之前的序列和
                           nums[i])
                tmp = nums[i]
        return max_


s = Solution()
arr = [-2, -1]
res = s.maxSubArray(arr)
print(res)
