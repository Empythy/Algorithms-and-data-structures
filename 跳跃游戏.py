class Solution:
    """
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    判断你是否能够到达最后一个位置。
    """
    def canJump(self, nums):
        n = len(nums)
        furthest = 0
        for i in range(n):
            if furthest < i: # 判断之前跳跃的最远的位置是否能跳到当前位置
                return False
            furthest = max(furthest, nums[i] + i)
        return furthest >= n - 1

    def canJump_dp(self, nums):
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            if nums[i] + i >= n - 1:
                # 如果当前位置能直接跳跃到最后位置
                dp[i] = True
            else:
                # 判断在i 的跳跃范围内 是否能跳跃到最后
                dp[i] = any(dp[i + 1: i + nums[i] + 1])
        return dp[0]