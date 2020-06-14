from typing import List
from collections import deque

class Solution1:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        l = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    l.append((i, j))

        queue = deque(l)
        while queue:
            tmp = []
            # 用来存放新的橘子
            for _ in range(len(queue)):
                cur_x, cur_y = queue.popleft()
                for d_x, d_y in zip(dx, dy):
                    new_x = d_x + cur_x
                    new_y = d_y + cur_y
                    print("111", new_x, new_y)
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                        print(new_x, new_y)
                        grid[new_x][new_y] = 2
                        tmp.append((new_x, new_y))
            cnt += 1
            queue = deque(tmp)

        if any(1 in row for row in grid):
            return -1
        return cnt - 1 if cnt > 0 else 0


from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        R, C = len(grid), len(grid[0])
        # queue - all starting cells with rotting oranges
        queue = deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        if any(1 in row for row in grid):
            return -1
        return d


if __name__ == "__main__":
    # grid = [[2,1,1],[1,1,0],[0,1,1]]
    solution = Solution1()
    grid = [[1], [2]]
    res = solution.orangesRotting(grid)
    print(res)
