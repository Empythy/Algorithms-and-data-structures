import collections
from typing import List

"""
给定一个包含了一些 0 和 1 的非空二维数组 grid 。
一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。
你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0)
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def dfs(self, grid, cur_i, cur_j):
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
            return 0
        grid[cur_i][cur_j] = 0
        ans = 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i, next_j = cur_i + di, cur_j + dj
            ans += self.dfs(grid, next_i, next_j)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans = max(self.dfs(grid, i, j), ans)
        return ans

"""
深度优先搜索
"""

class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                cur = 0
                stack = [(i, j)]
                while stack:
                    cur_i, cur_j = stack.pop()
                    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) \
                            or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
                        continue
                    cur += 1
                    grid[cur_i][cur_j] = 0
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        next_i, next_j = cur_i + di, cur_j + dj
                        stack.append((next_i, next_j))
                ans = max(ans, cur)
        return ans

"""广度优先搜索"""
class Solution3:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                cur = 0
                q = collections.deque([(i, j)])
                while q:
                    cur_i, cur_j = q.popleft()
                    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or \
                            cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
                        continue
                    cur += 1
                    grid[cur_i][cur_j] = 0
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        next_i, next_j = cur_i + di, cur_j + dj
                        q.append((next_i, next_j))
                ans = max(ans, cur)
        return ans


