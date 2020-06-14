from functools import lru_cache

"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

"""


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word1), len(word2)

        @lru_cache
        def dp(i, j):
            if i < 0:
                return j+1
            if j < 0:
                return i+1
            if word1[i] == word2[j]:
                ## 相同
                return dp(i - 1, j - 1)
            else:
                return min(
                    dp(i - 1, j),  # 删除
                    dp(i, j - 1),  # 插入
                    dp(i - 1, j - 1)  # 替换
                ) + 1

        return dp(m - 1, n - 1)

    def minDistance1(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # dp[m][n] 代表 m,n 最小编辑距离
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j


        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1],  # 替换
                                   dp[i][j], dp[i - 1][j],  # 删除
                                   dp[i][j - 1])  # 替换

        return dp[m][n]
