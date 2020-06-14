
"""
10
0 1 0 1 0 0 0 1 0 1
0 0 0 1 1 1 0 1 0 1

5
"""

line1 = "10"
line2 = "0 1 0 1 0 0 0 1 0 1"
line3 = "0 0 0 1 1 1 0 1 0 1"
n = int(line1)
gym = list(map(int, line2.split()))
work = list(map(int, line3.split()))
dp = [[0] * 3 for _ in range(n+1)]

# 0-->休息 1-->工作 2-->健身
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0

for i in range(1, n+1):
    if gym[i-1] == 1:
        # 健身
        dp[i][1] = min(dp[i-1][0], dp[i-1][2])
    if work[i-1] == 1:
        dp[i][2] = min(dp[i-1][0], dp[i-1][1])

    dp[i][0] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + 1

ans = min(dp[n][0], dp[n][1], dp[n][2])
print(ans)
