from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ret = []
        def backtrack(start, track):
            ret.append(track.copy())
            if start == n: # 递归终止
                return
            for i in range(start, n):
                """注意 得二者同时使用"""
                # 已选择的集合 [0:start]
                if i > start and nums[i] == nums[i - 1]:
                    continue
                track.append(nums[i])
                backtrack(i + 1, track)
                track.pop()

        backtrack(0, [])
        return ret

class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        def track_back(i, track):
            res.append(track.copy())
            if (i == n):
                return
            for j in range(i, n):
                if (j > i and nums[j] == nums[j - 1]):
                    continue
                track.append(nums[j])
                track_back(j + 1, track)
                track.pop()

        res = []
        track_back(0, [])
        return res
