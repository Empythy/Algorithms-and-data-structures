from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n <=1:
            return 0
        dp = [[0,0] for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(
                dp[i-1][0],
                dp[i-1][1]+prices[i]
            )
            dp[i][1] = max(
                dp[i-1][1],
                dp[i-1][0]-prices[i]
            )
        return dp[n-1][0]

    def maxProfit1(self, prices: List[int]) -> int:

        n = len(prices)
        if n <= 1:
            return 0
        dp_i_0 = 0
        dp_i_1 = -prices[0]

        for i in range(1, n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0



if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    res = s.maxProfit(prices)
    print(res)