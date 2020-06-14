def jump_dp(nums):
    n = len(nums)
    dp = [False] * n

    dp[n-1] = True
    for i in range(n-2, -1, -1):
        if nums[i] + i >= n - 1:
            dp[i] = True
        else:
            dp[i] = any(dp[i+1:i+nums[i]+1])
    return dp[0]

def test_jupm_dp():
    nums = [2, 3, 1, 1, 4]
    ans = jump_dp(nums)
    assert ans == True
    nums = [3, 2, 1, 0, 4]
    ans = jump_dp(nums)
    print(ans)


def jump_greedy(nums):
    n = len(nums)
    farthest = 0
    for i in range(n):
        farthest = max(farthest, nums[i] + i)
        if farthest <= i:
            # 注意等于符号
            return False
    return farthest >= n-1


class Solution:
    def canJump(self, nums):
        n = len(nums)

        dp = [False] * n
        dp[n-1] = True

        for i in range(n-2, -1, -1):
            if nums[i] + i >= n - 1:
                dp[i] = True
            else:
                dp[i] = any(dp[i+1:i+nums[i]+1])
        return dp[0]
