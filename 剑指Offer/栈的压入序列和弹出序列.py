"""
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""

# -*- coding:utf-8 -*-
class Solution(object):
    # 用栈模拟
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) == 0 or len(pushV) != len(popV):
            return False
        stack = []

        for item in pushV:
            stack.append(item)
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            else:
                continue
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    ret = s.IsPopOrder([1,2,3,4,5],[4,5,3,2,1])
    print( ret)
