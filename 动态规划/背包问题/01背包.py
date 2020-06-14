
def test(n, m, vt, wt, N):
    # dp = [[0] * N for _ in range(N)]
    dp = [0] * N
    for i in range(1, n+1):
        # for j in range(m+1):
        for j in range(m, vt[i]-1, -1):
            # dp[i][j] = dp[i-1][j] # 不选i东西
            if vt[i] <= j:
                # dp[i][j] = max(dp[i][j], dp[i-1][j-vt[i]]+wt[i]) # 比较选i
                dp[j] = max(dp[j], dp[j-vt[i]]+wt[i])
    return dp[m]
if __name__ == "__main__":
    N, V = 0, 0
    vt, wt = [], []