class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        deque = []
        cnt = 0
        row = len(grid)
        col = len(grid[0])
        visited = []  ## 不能直接使用乘法
        for i in range(row):
            visited.append([0]*col)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    deque.append((i, j, 0))
                    visited[i][j] = 1
                elif grid[i][j] == 1:
                    cnt = cnt + 1
                else:
                    continue
        max_minutes = 0
        while deque:
            x, y, mins = deque.pop(0)
            max_minutes = mins
            for tx, ty in zip(dx, dy):
                new_x = x + tx
                new_y = y + ty
                if 0 <= new_x < row and 0 <= new_y < col:
                    if grid[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                        visited[new_x][new_y] = 1
                        deque.append((new_x, new_y, mins + 1))
                        cnt -= 1

        if cnt > 0:
            return -1
        else:
            return max_minutes


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    s = Solution()
    ret = s.orangesRotting(grid)
    print(ret)
