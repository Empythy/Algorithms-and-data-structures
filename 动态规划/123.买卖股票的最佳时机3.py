# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 限制交易次数
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        max_k = 2
        dp = [[[0, 0] for _ in range(max_k+1)] for _ in range(n)]

        for i in range(n):
            # k=max_k   k>=1
            for k in range(max_k, 0, -1):
                if i >= 1:
                    dp[i][k][0] = max(dp[i - 1][k][0],
                                      dp[i - 1][k][1] + prices[i])

                    dp[i][k][1] = max(dp[i - 1][k][1],
                                      dp[i - 1][k - 1][0] - prices[i])
                else:
                    dp[0][k][0] = 0
                    dp[0][k][1] = -prices[0]

        return dp[n - 1][max_k][0]
