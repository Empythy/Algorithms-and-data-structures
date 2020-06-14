"""
f[i] 总体积i的情况下  最大价值是多少
for (int i=0; i<=m; i++)
    for (int j=m; j>=v[i]; j--)
        f[j] = max(f[j], f[j-v[i]]+w[i])
        f[j] = max(f[j], f[j-v[i]]+w[i], f[j-k * v[i]]+ k * w[i])

"""
N = 110
data_line = ["4 5"
    , "1 2 3"
    , "2 4 1"
    , "3 4 3"
    , "4 5 2"]

n, m = [int(item) for item in data_line[0].split()]
# st, vt, wt = [0] * N, [0] * N, [0] * N
# for i in range(n):
#     st[i], vt[i], wt[i] = [int(item) for item in data_line[i + 1].split()]
# print(vt)
# print(wt)
dp = [0] * N
for i in range(n):
    v, w, s = [int(item) for item in data_line[i + 1].split()]
    for j in range(m, -1, -1):
        max_k = min(s, j // v)
        for k in range(1, max_k + 1):
            dp[j] = max(dp[j], dp[j - k * v] + k * w)
print(dp[m])
