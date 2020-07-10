import itertools
from typing import List
import random


def permute(self, nums: List[int]) -> List[List[int]]:
    return list(itertools.permutations(nums))


class Solution1:
    def permute(self, nums):

        def backtrack(first=0):
            # if all integers are used up
            if first == n:
                output.append(nums[:])

            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(start, path):
            if start == size:
                res.append(path.copy())
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(start + 1, path)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []
        used = [False for _ in range(size)]
        res = []
        dfs(0, [])
        return res


class Solution:
    def permute(self, nums):
        n = len(nums)
        result = []
        used = [False] * n
        def bactrack(nums, track):
            """
             做选择 将该选择从选择列表删除
             路径.add(选择)
             backrack(路径, 选择列表)
             撤销选择
             路径.remove(选择)
             将该选择再加入选择列表
            """
            if len(track) == n:
                result.append(track.copy())
                return
            for i in range(n):
                if used[i] == True:
                    continue
                item = nums[i]
                used[i] = True
                track.append(item)
                bactrack(nums, track)
                track.remove(item)
                used[i] = False
        bactrack(nums, [])
        return result

if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)

