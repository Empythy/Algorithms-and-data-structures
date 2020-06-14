data_line = ["4 5",
             "1 2",
             "2 4",
             "3 4",
             "4 6"]

# f[i] # 用来存储容积为i的最佳方案
# cnt[i] # 容积为i时 总价值为最佳的方案数

N, V = map(int, input().split())
f = [0] * (V + 1)
cnt = [1] * (V + 1)
mod = 1e9 + 7
for i in range(N):
    vi, wi = map(int, input().split())
    # vi, wi = map(int, data_line[i + 1].split())
    for j in range(V, vi-1, -1):
        value = f[j-vi] + wi
        if value > f[j]:
            f[j] = value
            cnt[j] = cnt[j-vi]
        elif (value == f[j]):
            cnt[j] = (cnt[j] + cnt[j - vi]) % mod


