from functools import lru_cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 该代码求解的是排列数
        @lru_cache(None)
        def dp(n):
            if n == 0:
                return 1
            res = 0
            for coin in coins:
                if n - coin >= 0:
                    res += dp(n - coin)
            return res
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for n in range(1, amount + 1):  #  先循环金额  再循环硬币   该代码求解的是排列数
            for coin in coins:  # 
           
                if n - coin < 0:
                    continue
                dp[n] += dp[n - coin]
        return dp[amount]
        """
    def change2(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:  # 先循环 硬币 再循环金额  求解组合数
            for n in range(1, amount + 1):
                if n - coin < 0:
                    continue
                dp[n] += dp[n - coin]
        return dp[amount]

    def change3(self, amount: int, coins: List[int]) -> int:
        self.res = 0
        n = len(coins)
        coins.sort()
        @lru_cache(None)
        def backtrack(residual, start):
            if residual == 0:
                self.res += 1
            for i in range(start, n):
                if residual-coins[i] < 0:
                    return
                backtrack(residual-coins[i], i)
        backtrack(amount, 0)
        return self.res



if __name__ == "__main__":
    solution = Solution()
    amount = 5
    coins = [1, 2, 5]
    res = solution.change(amount, coins)
    res1 = solution.change2(amount, coins)

    print(res)
    print(res1)
    res3 = solution.change3(amount, coins)
    print(f"回溯法{res3}", )
    # assert res == res1
