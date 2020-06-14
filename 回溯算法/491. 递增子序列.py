"""
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
"""
from typing import List


class Solution:
    def findSubsequences1(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(start, tmp):
            dic = {}  # 判断数字是否被使用  当前层

            if len(tmp) > 1:  # 满足条件
                res.append(tmp)

            for i in range(start, len(n)):
                if dic.get(nums[i], 0):  # 判断数字是否被使用  当前层
                    continue
                if len(tmp) == 0 or nums[i] >= tmp[-1]:
                    dic[nums[i]] = 1
                    dfs(i + 1, tmp + [nums[i]])

        dfs(0, [])
        return res

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """不能使用
        会发生 在不同的位置出现 1的问题
        """
        res = []
        n = len(nums)
        # used = [False] * n

        def dfs(start, tmp):
            seen = {}
            if len(tmp) > 1:  # 满足条件
                res.append(tmp.copy())

            for i in range(start, len(nums)):

                if seen.get(nums[i], 0): continue

                if len(tmp) == 0 or  nums[i] >= tmp[-1]:
                    # used[i] = True
                    seen[nums[i]] = 1
                    tmp.append(nums[i])
                    dfs(i + 1, tmp)
                    tmp.pop()
                    # used[i] = False

        dfs(0, [])
        return res


nums = [1, 6, 7, 1, 1]
ans1 = Solution().findSubsequences(nums)
ans2 = Solution().findSubsequences1(nums)
assert ans1 == ans2

