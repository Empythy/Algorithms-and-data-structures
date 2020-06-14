"""
 public int longestPalindromeSubseq2nd(String s) {
        int n = s.length();
        Integer[][] memo = new Integer[n][n];
        return helper(s, 0, n - 1, memo);
    }

    private int helper(String s, int i, int j, Integer[][] memo) {
        if (memo[i][j] != null) return memo[i][j];
        if (i > j) return 0;
        if (i == j) return 1;
        if (s.charAt(i) == s.charAt(j)) {
            memo[i][j] = helper(s, i + 1, j - 1, memo) + 2;
        } else {
            memo[i][j] = Math.max(helper(s, i + 1, j, memo), helper(s, i, j - 1, memo));
        }
        return memo[i][j];
    }

作者：a-fei-8
链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence/solution/a-fei-xue-suan-fa-zhi-si-ke-yi-dao-ti-516-zui-chan/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = [[0] * n for _ in range(n)]
        def helper(s, i, j):
            if memo[i][j] != 0: return memo[i][j]
            if i > j: return 0
            if i == j: return 1
            # while i >= 0 and j < len(s) and i<j:
            if s[i] == s[j]:
                res = helper(s, i + 1, j - 1)+2
            else:
                res = max(
                    helper(s, i + 1, j),
                    helper(s, i, j - 1)
                    )
            memo[i][j] = res
            print(f"{i}-{j}:{res}")
            return res

        "mome[i][j] 返回s[i]-s[j]最长的回文子序列长度"
        return helper(s, 0, len(s) - 1)

# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         # 使用dp思想
#         n = len(s)
#         dp = [[0] * n for i in range(n)]
#         # 注意basecase
#         for i in range(n):
#             dp[i][i] = 1
#
#         # 倒着遍历
#         for i in range(n, -1, -1):
#             for j in range(i + 1, n):
#                 if s[i] == s[j]:
#                     dp[i][j] = dp[i + 1][j - 1] + 2
#                 else:
#                     dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
#         return dp[0][n - 1]


if __name__ == "__main__":
    str1 = "bbbab"
    solution = Solution()
    res = solution.longestPalindromeSubseq(str1)
    print(res)
