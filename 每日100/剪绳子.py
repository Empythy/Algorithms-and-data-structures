class Solution:
    def cuttingRope(self, n: int) -> int:
        memo = {1: 1, 2: 1, 3: 2}
        def healper(n):
            if n in memo.keys():
                return memo[n]
            res = -1
            for i in range(1, n):
                    res = max(res, healper(i) *(n-i), i * (n-i))

            memo[n] = res
            return memo[n]

        return healper(n)

if __name__ == "__main__":
    s = Solution()
    ret = s.cuttingRope(6)
    print(ret)
