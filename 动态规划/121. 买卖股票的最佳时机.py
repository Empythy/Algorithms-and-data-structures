"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0],  # # 昨天休息
                           dp[i-1][1] + prices[i]  # 今天卖掉
                        )

            dp[i][1] = max(dp[i-1][1],  #   前一天持有 今天休息
                           -prices[i]   # 昨天没有 今天买入
                           # 注意 dp[i-1][0] - prices[i]
                        )

        print(dp)
        return dp[n-1][0]
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    solution = Solution()
    ret = solution.maxProfit(prices)
    print(ret)