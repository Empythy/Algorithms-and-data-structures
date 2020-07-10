def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [
            [False] * n for _ in range(m)
        ]
        def dfs(x, y):
            if x >= m or y >= n or digitsum(x) + digitsum(y) > k or visited[x][y]:
                return 0
            visited[x][y] = True
            return 1 + dfs(x + 1, y) + dfs(x, y + 1)

        return dfs(0, 0)