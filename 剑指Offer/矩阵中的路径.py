class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix and rows <= 0 and cols <= 0 and path == None:
            return False
        boolmatrix = [0] * (rows * cols)
        # boolmatrix = [ [0 for _ in range(cols)] for _ in range(rows)]
        # 也可以，后面都使用 矩阵boolmatrix[i][j]的形式
        pathLength = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathLength, boolmatrix):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, boolmatrix):
        if len(path) == pathLength:
            return True

        hasNextPath = False
        if (row >= 0 and row < rows and col >= 0 and col < cols and
                matrix[row * cols + col] == path[pathLength] and not boolmatrix[row * cols + col]):
            pathLength += 1
            boolmatrix[row * cols + col] = True
            # 进行该值的上下左右的递归(周围是否存在下一个路径点)
            hasNextPath = (self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathLength, boolmatrix)
                           or self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathLength, boolmatrix)
                           or self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathLength, boolmatrix)
                           or self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathLength, boolmatrix))
            #































             
        return hasNextPath
