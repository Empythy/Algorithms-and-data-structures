"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""


# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def __init__(self):
        self.ret = []

    def printMatrix(self, matrix):
        # write code here
        row = len(matrix)
        col = len(matrix[0])
        if row == 0 and col == 0:
            return self.ret
        if row == 1 and col == 1:
            self.ret.append(matrix[0][0])
            return self.ret
        if row == 1 and col != 1:
            self.ret.extend(matrix[0])
            return ret
        if row != 1 and col == 1:
            self.ret.extend([item[0] for item in matrix])
        if row == 2:
            self.ret.extend(matrix[0])
            self.ret.extend(reversed(matrix[1]))
            return self.ret
        if col == 2:
            self.ret.extend(matrix[0])
            self.ret.extend([item[-1] for item in matrix[1:]])
            self.ret.extend(reversed([item[0] for item in matrix][1:]))
            return self.ret

        """
        [[1, 2],
         [3, 4]
        """
        if row > 2 and col > 2:
            self.ret.extend(matrix[0])  #
            self.ret.extend([item[-1] for item in matrix[1:]])
            self.ret.extend(reversed(matrix[row - 1][:-1]))
            self.ret.extend(reversed([item[0] for item in matrix][1:-1]))
            new_matrix = [item[1:-1] for item in matrix[1:-1]]
            return self.printMatrix(new_matrix)


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    s = Solution()
    # ret = s.printMatrix([[1]])
    # ret = s.printMatrix([[1,2],[3,4]])
    # ret = s.printMatrix([[1, 2, 3, 4],
    #                      [5, 6, 7, 8],
    #                      [9, 10, 11, 12],
    #                      [13, 14, 15, 16]])
    # ret = s.printMatrix([[1],[2],[3],[4],[5]])
    # ret = s.printMatrix([[1,2],
    #                      [3,4],
    #                      [5,6],
    #                      [7,8],
    #                      [9,10]])

    ret = s.printMatrix([[1,2,3,4,5]])
    print(ret)
