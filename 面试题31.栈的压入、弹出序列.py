"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，
但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        data_stack = []
        n_push = len(pushed)
        n_pop = len(popped)
        if n_pop != n_push:
            return False
        for i in range(n_push):
            data_stack.append(pushed[i])
            while len(data_stack) > 0 and len(popped) > 0 and data_stack[-1] == popped[0]:
                data_stack.pop()
                popped.pop(0)

        return len(data_stack) == 0
