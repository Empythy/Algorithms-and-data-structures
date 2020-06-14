import itertools
from typing import List
"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        """库函数"""
        res = []
        for i in range(len(nums) + 1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:

        """回溯
        https://leetcode-cn.com/problems/subsets/solution/hui-su-si-xiang-tuan-mie-pai-lie-zu-he-zi-ji-wen-t/
        """
        n = len(nums)
        ret = []
        used = [False] * n

        def backtrack(start, track):
            ret.append(track.copy()) # 直接添加
            if start == n:
                return

            for i in range(start, len(nums)):
                if used[i]:
                    continue
                used[i] = True
                track.append(nums[i])
                backtrack(i+1, track)
                track.pop()
                used[i] = False
        backtrack(0, [])
        return ret

    

