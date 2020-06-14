from functools import lru_cache
from typing import List

"""
不限个数 求最小的张数
"""

class Solution:
    def coinChange(coins: List[int], amount: int):
        # 定义： 要凑出⾦额 n， ⾄少要 dp(n) 个硬币
        @lru_cache(None)
        def dp(n):
            if n == 0: return 0
            if n < 0: return -1
            res = float('inf')
            # 做选择， 选择需要硬币最少的那个结果
            for coin in coins:
                # subproblem = dp(n - coin)
                # if subproblem == -1:
                #     continue
                if n >= coin:
                    res = min(res, 1 + dp(n - coin))
            return res

        # 我们要求的问题是 dp(amount)
        return dp(amount)
