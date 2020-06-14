def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        from queue import Queue
        q = Queue()
        q.put((0, 0))
        s = set()
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and \
                    0 <= x < m and \
                    0 <= y < n and \
                    digitsum(x) + digitsum(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]:
                    q.put((nx, ny))
        return len(s)


class Solution2:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[False] * n for _ in range(m)]

        def dfs(x, y):
            if x >= m or y >= n or digitsum(x) + digitsum(y) > k or visited[x][y]:
                return 0
            visited[x][y] = True
            return 1 + dfs(x + 1, y) + dfs(x, y + 1)


if __name__ == "__main__":
    m = 2
    n = 3
    k = 1
    solution = Solution()
    res = solution.movingCount(m, n, k)
    print(res)
