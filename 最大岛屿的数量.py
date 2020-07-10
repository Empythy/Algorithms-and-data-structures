# -*- coding: utf-8 -*-#
"""
Created on  2020/7/6  12:25 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        def dfs(i, j):
            ans = 1
            visited[i][j] = True
            for d_i, d_j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_i, new_j = i + d_i, j + d_j
                if 0 <= new_i < m and 0 <= new_j < n and \
                        visited[new_i][new_j] == False and \
                        grid[new_i][new_j] == 1:
                    visited[new_i][new_j] = True
                    ans += dfs(new_i, new_j)
            return ans

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    ans = max(ans, dfs(i, j))

        return ans


grid = [[1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]]
s = Solution()
ans = s.maxAreaOfIsland(grid)
print(ans)
