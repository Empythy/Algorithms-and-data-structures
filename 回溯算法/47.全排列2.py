from typing import List


class Solution:
    """
    给定一个可包含重复数字的序列，返回所有不重复的全排列。
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        used = [False] * n
        result = []
        def backtrack(track):

            """满足条件"""
            if len(track) == n:
                result.append(track.copy())
                return
            for i in range(n):
                if used[i] == True:
                    continue
                ## 去重 注意 use[i-1]  要在使用上一个的情况下才能使用当前的
                if i > 0 and nums[i] == nums[i - 1] and not used[i-1]:
                    continue
                used[i] = True
                track.append(nums[i])
                backtrack(track)
                track.remove(nums[i])
                used[i] = False
        backtrack([])
        return result

if __name__ == "__main__":
    solution = Solution()
    l = [1, 2, 1]
    ret = solution.permuteUnique(l)
    print(ret)
