"""
补码： 正数不变  负数是他正数反码加1

-2  2 10000010  111111101  111111110
"""


# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        n = n & 0xFFFFFFFF

        count = 0
        for c in str(bin(n)):
            if c == '1':
                count += 1

        return count
        # count = 0
        # for i in range(32):
        #     mask = 1 << i
        #     if n & mask != 0:
        #         count += 1
        # return count

if __name__ == '__main__':
    n = 5
    s = Solution().NumberOf1Between1AndN_Solution(n)
    print(s)

