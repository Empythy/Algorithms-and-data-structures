# -*- coding: utf-8 -*-#
"""
Created on  2020/7/7  9:38
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com
@Description:
@version: V1
"""

class Solution():

    def elimilate(self, S, k):
        if len(S) <= 1:
            return S
        stack = ['']
        for i in range(len(S)):
            top = stack[-1]
            ch = S[i]
            # 每次遇见新元素之前  先判断能否和前面的字符串构成整体
            if ch == top or len(top) > 1 and top[-1] == ch:
                stack[-1] += ch
            else:
                # 接着判断 栈顶元素是否满足弹出要求
                if len(stack[-1]) >= k:
                    stack.pop()
                # 然后 再进行添加
                # 1. 是否和新的栈顶元素构成整体
                # 否则 将其作为一个新的元素添加到栈中
                if ch == stack[-1] or len(stack[-1]) > 1 and stack[-1][-1] == ch:
                    stack[-1] += ch
                else:
                    stack.append(ch)

        return ''.join(stack[1:])


    def removeDuplicates(self, s: str, k: int) -> str:
        """移除k个相同的字符串"""
        if len(s) < k:
            return s

        stack = ['']
        for i in range(len(s)):
            top = stack[-1]
            ch = s[i]
            if top == s[i] or (len(top) > 1 and top[-1] == s[i]):
                stack[-1] = stack[-1] + ch
            else:
                stack.append(ch)
            # 每次添加完之后再删除
            if len(stack[-1]) == k:
                stack.pop()

        return "".join(stack[1:])


if __name__ == '__main__':
    S = "abbaca"
    s = Solution()
    ans = s.elimilate(S, 2)
    print(ans)
