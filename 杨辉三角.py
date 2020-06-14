from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []

        def helper(i, j):
            try:
                if ret[i - 1][j - 1]:
                    return ret[i - 1][j - 1]
            except:
                if j == 1 or i == j:
                    return 1
                return helper(i - 1, j - 1) + helper(i - 1, j)

        for i in range(1, numRows + 1):
            tmp_ret = []
            for j in range(1, i + 1):
                tmp_ret.append(helper(i, j))
            ret.append(tmp_ret)
        return ret

    def getRow(self, rowIndex: int) -> List[int]:
        ret = self.generate(rowIndex)
        print(ret)
        print(ret[-1])
        return ret[-1]

if __name__ == "__main__":
    S = Solution()
    s = S.getRow(3)

