from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, track):
            res.append(track.copy())
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(i+1, track)
                track.pop()
        backtrack(0, [])
        return res

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#
#         def backtrack(path):
#             ans.append(path.copy())
#
#             for item in nums:
#                 if not item in path:
#                     path.append(item)
#                     backtrack(path)
#                     path.pop()
#
#         backtrack([])
#         return ans


s = Solution()
nums = [1, 2, 3]
ans = s.subsets(nums)
print(ans)