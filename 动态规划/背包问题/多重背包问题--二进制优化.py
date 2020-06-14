import collections
if __name__ == '__main__':
    goods = collections.namedtuple('good', ['v', 'w'])
    N, V = map(int, input().split())
    Goods = []
    dp = [0] * (V + 1)
    for i in range(N):
        v, w, s = map(int, input().split())
        k = 1
        while k <= s:
            s -= k
            Goods.append(goods._make([v*k, w*k]))
            k *= 2
        if s > 0:
            Goods.append(goods._make([v*s, w*s]))

    for good in Goods:
        for j in range(V, good.v - 1, -1):
            dp[j] = max(dp[j], dp[j - good.v] + good.w)
    print(dp[V])
