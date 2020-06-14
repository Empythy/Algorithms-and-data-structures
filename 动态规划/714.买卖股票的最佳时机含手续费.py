from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp_i_0 = 0
        dp_i_1 = -prices[0]
        for i in range(1, n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i]-fee)
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0