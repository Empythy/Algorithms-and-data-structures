class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        import math
        ans = []
        N = int(math.sqrt(2 * tsum))
        for n in range(N, 1, -1):
            # n为奇数时，序列中间的数正好是序列的平均值，
            # 所以条件为：(n & 1) == 1 && sum % n == 0
            # n为偶数时，序列中间两个数的平均值是序列的平均值，而这个平均值的小数部分为0.5，
            # 所以条件为：(sum % n) * 2 == n.
            if ((n & 1) == 1 and tsum % n == 0 or (tsum % n) * 2 == n):
                num_list = []
                k = (tsum // n) - (n - 1) // 2
                for j in range(n):
                    num_list.append(k)
                    k += 1
                ans.append(num_list[:])
        return ans

if __name__ == '__main__':
    s = Solution()
    ret = s.FindContinuousSequence(9)
    print(ret)