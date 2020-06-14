"""
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
两个相邻元素间的距离为 1

例子：
0 0 0
0 1 0
0 0 0

输出
0 0 0
0 1 0
0 0 0
"""
import collections
from typing import List

from collections import deque

#
# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         m = len(matrix)
#         n = len(matrix[0])
#         dist = [[0] * n for _ in range(m)]
#         zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
#         dq = deque(zeroes_pos)
#         seen = set(zeroes_pos)
#         while dq:
#             row, col = dq.popleft()
#             for new_row, new_col in [(row + 1, col), (row, col + 1),
#                                      (row - 1, col), (row, col - 1)]:
#                 if 0 <= new_row < m and 0 <= new_col < n and \
#                         not (new_row, new_col) in seen:
#
#                     dist[new_row][new_col] += 1
#                     seen.add((new_row, new_col))
#         return dist


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)

        # 广度优先搜索
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j),
                           (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))

        return dist
