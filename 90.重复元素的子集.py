from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(start, path):
            ans.append(path.copy())
            if start == len(nums):
                return
            for index in range(start, len(nums)):
                # if path and nums[index] == nums[index-1]:
                if index > start and nums[index] == nums[index-1]:
                    continue
                path.append(nums[index])
                backtrack(index+1, path)
                path.pop()

        backtrack(0, [])
        return ans

nums = [1,2,2]
s = Solution()
ans = s.subsetsWithDup(nums)
print(ans)