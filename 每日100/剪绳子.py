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
# class Solution1:
#     def cuttingRope(self, n: int) -> int:
#         f = [0 for _ in range(n + 1)]
#         # 使用辅助函数
#         def memoize(n):
#
#             if n == 2: return 1
#             if f[n] != 0: # 如果f[n]已经计算过，直接返回避免重复计算
#                 return f[n]
#             res = -1
#             for i in range(1, n):
#                 res = max(res,
#                           max(i * (n - i),
#                               i * memoize(n - i)))
#             f[n] = res
#             return res
#
#         return memoize(n)

if __name__ == "__main__":
    s = Solution()
    ret = s.cuttingRope(6)
    print(ret)
