from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return N
        dp = [1] * N  # lengths[i] = longest ending in nums[i]
        counts = [1] * N  # count[i] = number of longest ending in nums[i]
        for j, num in enumerate(nums):
            for i in range(j):
                if nums[j] > nums[i]:
                    if dp[i] >= dp[j]:
                        dp[j] = 1 + dp[i]
                        counts[j] = counts[i]
                    elif dp[i] + 1 == dp[j]:
                        counts[j] += counts[i]
        longest = max(dp)
        return sum(c for i, c in enumerate(counts) if dp[i] == longest)

