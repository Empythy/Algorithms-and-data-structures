from typing import List
from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        steps = -1
        queue = deque(
            [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1])
        if len(queue) == 0 or len(queue) == n ** 2:
            return steps
        while len(queue) > 0:
            tmp = []
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for xi, yj in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if xi >= 0 and xi < n and yj >= 0 and yj < n and grid[xi][yj] == 0:
                        tmp.append((xi, yj))
                        grid[xi][yj] = -1 # 进行标记
            queue = deque(tmp)
            steps += 1

        return steps
