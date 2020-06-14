"""
第⼀个状态是剩余的按键次数， ⽤ n 表⽰；
第⼆个状态是当前屏幕上字符 A 的数量， ⽤ a_num 表⽰；
 第三个状态是剪切板中字符 A 的数量， ⽤ copy 表⽰
"""
from functools import lru_cache


class Solution():
    @lru_cache(None)
    def Numof_A(self, N):
        """
        dp(n - 1, a_num + 1, copy),  # A
        解释： 按下A键， 屏幕上加⼀个字符同时消耗1个操作数
        dp(n - 1, a_num + copy, copy),  # C-V
        解释： 按下C - V 粘贴， 剪切板中的字符加⼊屏幕同时消耗1个操作数
        dp(n - 2, a_num, a_num)  # C-A C-C
        解释： 全选和复制必然是联合使⽤的，剪切板中A的数量变为屏幕上
        A的数量同时消耗2个操作数
        """

        def dp(n, a_num, copy):
            """
            :param n: 剩余次数
            :param a_num:  屏幕上a的个数
            :param copy: 缓冲区中A的个数
            :return:
            """
            if n <= 0: return a_num
            return max(
                dp(n - 1, a_num + 1, copy),
                dp(n - 1, a_num + copy, copy),
                dp(n - 2, a_num, a_num)
            )

        return dp(N, 0, 0)
