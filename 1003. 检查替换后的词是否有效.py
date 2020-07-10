# -*- coding: utf-8 -*-#
"""
Created on  2020/7/7  9:24 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""


class Solution:
    def isValid(self, S: str) -> bool:
        if len(S) < 3:
            return False
        if len(S) == 3:
            if S == "abc":
                return True
            else:
                return False

        stack = ['']
        for i in range(len(S)):
            top = stack[-1]
            ch = S[i]
            if ch == 'a':  # 'a' 可能被截断
                stack.append('a')
            elif ch == 'b':  # 'b' 也可能被截断
                if top == 'a':
                    stack[-1] += 'b'
                else:
                    stack.append('b')
            elif ch == 'c':  # '需要判断前面是否是'ab'
                if top == 'ab':
                    stack.pop()
                else:
                    return False

        return len(stack) == 1

if __name__ == '__main__':
    S = "aabcbc"
    s = Solution()
    ans  = s.isValid(S)
    print(ans)