
data_lines = ["4 5",
"1 2",
"2 4",
"3 4",
"4 5"]

"""
dp[i][j]  使用前i个物品的价值为j
"""

def general():
    n, m = [int(item) for item in data_lines[0].split()]
    dp = [[0] * (m+1) for _ in range(n+1)]
    vt = [0] * n
    wt = [0] * n
    for i in range(n):
        vt[i], wt[i] = [int(item) for item in data_lines[i].split()]


    for i in range(1, n+1):
        for j in range(m+1):
            dp[i][j] = dp[i-1][j]
            if j >= vt[i-1]:
                dp[i][j] = max(dp[i][j], dp[i][j-vt[i-1]]+wt[i-1])

    print(dp[n][m])


def general1():
    n, m = [int(item) for item in data_lines[0].split()]
    dp = [0] * (m + 1)
    vt = [0] * n
    wt = [0] * n
    for i in range(n):
        vt[i], wt[i] = [int(item) for item in data_lines[i].split()]

    for i in range(1, n + 1):
        for j in range(m + 1):
            # dp[i][j] = dp[i - 1][j]
            # dp[j] = dp[j]
            if j >= vt[i - 1]:
                dp[j] = max(dp[j], dp[j - vt[i - 1]] + wt[i - 1])
                # dp[i][j] = max(dp[i][j], dp[i][j - vt[i - 1]] + wt[i - 1])

    print(dp[m])

general1()