from functools import lru_cache


class Solution:
    def stoneGame(self, piles):
        N = len(piles)
        # @lru_cache(None)
        # def dp(i, j):
        #     # The value of the game [piles[i], piles[i+1], ..., piles[j]].
        #     if i > j: return 0
        #     parity = (j - i - N) % 2
        #     if parity == 1:  # first player
        #         return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
        #     else:
        #         return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))
        #
        # return dp(0, N - 1) > 0
        @lru_cache(None)
        def dp(i, j):
            # for m in range(N):
            #     for n in range(i, N):
            if i == j:
                return piles[i], 0

            if i + 1 <= j and i <= j - 1:
                left = piles[i] + dp(i + 1, j)[1]
                right = piles[j] + dp(i, j - 1)[1]

                if left > right:
                    return left, dp(i + 1, j)[0]
                else:
                    return right, dp(i, j - 1)[0]
        res = dp(0, N - 1)
        return res[0] > res[1]


if __name__ == "__main__":
    l = [59, 48, 36, 70, 59, 93, 60, 98, 15, 32, 31, 13, 27, 14, 8, 17, 4, 76, 24, 47, 39, 81, 26, 6, 70, 73, 8, 36, 71,
         19, 66, 61, 86, 63, 97, 32, 15, 36, 68, 69, 32, 53, 83, 35, 100, 41, 44, 8, 28, 76, 39, 90, 37, 35, 11, 99, 48,
         49, 64, 74, 6, 54, 12, 99, 34, 47, 78, 36, 51, 26, 43, 83, 10, 68, 32, 48, 72, 54, 64, 64, 44, 62, 77, 60, 100,
         84, 15, 24, 95, 6, 6, 8, 24, 21, 84, 61, 75, 26, 63, 54]
    solution = Solution()
    res = solution.stoneGame(l)
    print(res)
