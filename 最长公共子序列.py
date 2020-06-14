from functools import lru_cache

from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        memo = [[0] * n for _ in range(m)]  # 注意初始化

        if text1 == text2:
            return len(text1)

        # @lru_cache(None)
        def dp(i, j):
            # basecase
            if i < 0 or j < 0: return 0

            if memo[i][j] != 0: return memo[i][j]

            if text1[i] == text2[j]:
                memo[i][j] = dp(i - 1, j - 1) + 1
                return memo[i][j]
            else:
                memo[i][j] = max(dp(i - 1, j), dp(i, j - 1))
                return memo[i][j]

        return dp(len(text1) - 1, len(text2) - 1)


if __name__ == "__main__":
    text1 = "abscadjs;d;sf;s;fsf"
    text2 = "dsandklshfjdsljfljdsf"
    solution = Solution()
    ret = solution.longestCommonSubsequence(text1, text2)
    print(ret)
