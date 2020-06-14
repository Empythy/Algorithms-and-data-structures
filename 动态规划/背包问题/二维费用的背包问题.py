"""
有 N 件物品和一个容量是 V 的背包，背包能承受的最大重量是 M。
每件物品只能用一次。体积是 vi，重量是 mi，价值是 wi。
求解将哪些物品装入背包，可使物品总体积不超过背包容量，
总重量不超过背包可承受的最大重量，且价值总和最大。
输出最大价值。
dp[N][V][M]
"""
data_line = ["4 5 6",
             "1 2 3",
             "2 4 4",
             "3 4 5",
             "4 5 6"]


# N, V, M = map(int, data_line[0].split())
def test():
    """
    朴素写法
    :return:
    """
    N, V, M = map(int, input().split())

    f = [[[0] * (M + 1) for _ in range(V + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        vi, mi, wi = map(int, input().split())
        for j in range(V + 1):
            for k in range(M + 1):
                f[i][j][k] = f[i - 1][j][k]
                if j >= vi and k >= mi:
                    f[i][j][k] = max(f[i][j][k],
                                     f[i - 1][j - vi][k - mi] + wi)
    print(f[N][V][M])


def test1():
    """
    二维优化
    :return:
    """
    data_line = ["4 5 6",
                 "1 2 3",
                 "2 4 4",
                 "3 4 5",
                 "4 5 6"]
    # N, V, M = map(int, input().split())
    N, V, M = map(int, data_line[0].split())
    f = [[0] * (M + 1) for _ in range(V + 1)]
    for i in range(1, N + 1):
        # vi, mi, wi = map(int, input().split())
        vi, mi, wi = map(int, data_line[i].split())
        for j in range(V, vi-1, -1):
            for k in range(M, mi - 1, -1):
                # if j >= vi and k >= mi:
                # print(f"j={j} k={k} vi={vi} mi={mi} wi={wi}")
                # print(f"f[{j}][{k}] = {f[j][k]}")
                # print(f"f[{j-vi}][{k-mi}] = {f[j-vi][k-mi]}")
                f[j][k] = max(f[j][k], f[j - vi][k - mi] + wi)
    print(f[V][M])
test1()