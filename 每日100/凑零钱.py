import functools
from typing import List
import time


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(amount)
        def dp(rem):
            if rem < 0: return -1
            if rem == 0: return 0
            mini = int(1e9)
            for coin in self.coins:
                res = dp(rem - coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            return mini if mini < int(1e9) else -1

        self.coins = coins
        if amount < 1: return 0
        return dp(amount)

    def coinChange1(self, coins: List[int], amount: int) -> int:

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange2(coins: List[int], amount: int):
        # 备忘录
        memo = dict()

        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: return memo[n]
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)

            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]


        return dp(amount)

    def __init__(self):
        self.ans = float('inf')


    def coinChange3(self, coins, amount):
        if amount == 0: return 0
        coins.sort(reverse=True)
        self.coinChangeCore(coins, amount, 0, 0)
        if self.ans == float("inf"): return -1
        return self.ans



    def coinChangeCore(self, coins, amount, c_index, count):
        """

        :param coins:
        :param amount:
        :param c_index:
        :param count:
        :return:
        """

        if amount == 0:
            self.ans = min(self.ans, count)
            return
        if c_index == len(coins): return

        cnt = amount // coins[c_index]
        for k in range(cnt, -1, -1):
            if k + count < self.ans:
                consume = k * coins[c_index]
                self.coinChangeCore(coins, amount - consume, c_index+1, count+k)

    def coinChange4(self, coins: List[int], amount: int) -> int:
        self.res = float('inf')
        coins.sort(reverse=True)
        size = len(coins)

        def dfs(i, num, amount):
            """
            :param i:
            :param num: 已用的个数
            :param amount: 剩余的钱
            :return:
            """
            if amount == 0:  #如果钱消耗完了
                self.res = min(self.res, num)
                return
            for j in range(i, size):
                if (self.res - num) * coins[j] < amount: #
                    break
                if coins[j] > amount: # 如果硬币比剩余的amount 大  就不选择该硬币
                    continue
                dfs(j, num + 1, amount - coins[j]) # 继续选择当前硬币

        for i in range(size):
            dfs(i, 0, amount)
        return self.res if self.res != float('inf') else -1


if __name__ == "__main__":
    coins = [1, 5, 7, 10]
    amount = 14
    s = Solution()
    time1 = time.time()
    print(s.coinChange1(coins, amount))
    print(time.time() - time1)
    time2 = time.time()
    print(s.coinChange3(coins, amount))
    print(time.time()-time2)

    time3 = time.time()
    print(s.coinChange4(coins, amount))
    print(time.time() - time3)
