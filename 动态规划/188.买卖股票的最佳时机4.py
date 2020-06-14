
"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
"""
from typing import List


class Solution:
    def maxProfit_k_inf(self, prices):
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = float("-inf")
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        n = len(prices)
        if k > n:
            # 如果超过了数组长度  就是相当于 不限制交易次数
            return self.maxProfit_k_inf(prices)

        max_k = min(k, n // 2)
        dp = [[[0, 0] for _ in range(max_k + 1)] for _ in range(n)]
        for i in range(n):
            for k in range(max_k, 0, -1):
                if i >= 1:
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
                else:
                    dp[0][k][0] = 0  # 第一天休息
                    dp[0][k][1] = -prices[0]  # 第一天购买
        return dp[n - 1][max_k][0]