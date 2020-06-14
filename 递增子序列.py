from typing import List


# class Solution:
#     def findSubsequences(self, nums: List[int]) -> List[List[int]]:
#         ret = []
#         n = len(nums)
#         for i in range(n):
#             tmp_l = [nums[i]]
#             for j in range(i+1, n):
#                 if nums[j] >= nums[i]:
#                     if tmp_l in ret:
#                         continue
#                     tmp_l.append(nums[j])
#
#
#         return list(ret)


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start, tmp):
            dic = {}
            if len(tmp) > 1:
                res.append(tmp)
            for i in range(start, len(nums)):
                if dic.get(nums[i], 0):
                    continue
                if len(tmp) == 0 or nums[i] >= tmp[-1]:
                    dic[nums[i]] = 1
                    dfs(i + 1, tmp + [nums[i]])
        dfs(0, [])

        return res