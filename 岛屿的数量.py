from functools import lru_cache
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        @lru_cache
        def dfs(i, j):

            visited[i][j] = True

            for d_i, d_j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_i, new_j = i + d_i, j + d_j
                if 0 <= new_i < m and 0 <= new_j < n and \
                        not visited[new_i][new_j] and \
                        grid[new_i][new_j] == '1':
                    dfs(new_i, new_j)

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    cnt += 1
                    dfs(i, j)
        return cnt