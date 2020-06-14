def jump_greedy(nums):
    n = len(nums)
    step = 0
    farthest = 0
    end = 0
    for i in range(n):
        farthest = max(farthest, i + nums[i])
        if farthest <= i:
            return -1
        if i == end:
            step += 1
            end = farthest
    return step
def jump_dp(nums):
    n = len(nums)
    dp = [n+1] * n
    dp[n-1] = 0
    for i in range(n-2, -1, -1):
        if i + nums[i] >= n-1:
            dp[i] = 1
        else: # 注意[i, num[i]+i+1]
            dp[i] = min(dp[i+1:i+nums[i]+1]) + 1
    return dp[0] if dp[0] < n+1 else -1

def jump_greedy1(nums):
    n = len(nums)
    if n <= 1:
        return 0
    step = 0
    farthest = 0
    end = 0
    for i in range(n):
        farthest = max(farthest, i + nums[i])  # 尝试跳
        if farthest >= n-1:
            return step + 1  #跳
        if farthest <= i:
            return -1
        if i == end:
            step += 1 # 跳
            end = farthest

nums = [2, 1, 1, 0, 1]
# ans = jump_greedy1(nums)
ans = jump_dp(nums)
print(ans)