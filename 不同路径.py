# -*- coding: utf-8 -*-#
"""
Created on  2020/7/6  11:15 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from functools import lru_cache
from typing import List

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        @lru_cache(None)
        # 代表 0, 0 -> i, j 的方案数
        def helper(i, j):
            if i == row - 1 and j == col - 1 and obstacleGrid[i][j] != 1:
                return 1
            if i >= row or j >= col or obstacleGrid[i][j] == 1 :
                return 0
            return helper(i+1, j) + helper(i, j+1)

        return helper(0, 0)


class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        ans = [0]
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        def is_valid(i, j):
            if 0 <= i < row and 0 <= j < col:
                return True
            else:
                return False

        @lru_cache
        def dfs(i, j):
            if i == row and j == col:  # 满足条件
                ans[0] += 1
                return

            for new_i, new_j in [(i + 1, j), (i, j + 1)]:
                if is_valid(new_i, new_j) and obstacleGrid[new_i][new_j] == 0:
                    dfs(new_i, new_j)

        dfs(0, 0)
        return ans[0]



# grid = [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
grid = [[0],
        [1]]

s = Solution()
ans = s.uniquePathsWithObstacles(grid)
print(ans)