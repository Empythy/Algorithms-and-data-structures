# -*- coding: utf-8 -*-#
"""
Created on  2020/7/8  15:03 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from typing import List

"""
给定一个整数数组 A，找到 min(B) 的总和，其中 B 的范围为 A 的每个（连续）子数组
"""

class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        len_A = len(A)
        if len_A == 0:
            return 0
        if len_A == 1:
            return A[0]
        ans = 0
        left = [0] * len_A
        right = [0] * len_A

        stack = []
        for i in range(len_A):
            # 注意边界
            # 1 1 1 1
            while stack and A[stack[-1]] > A[i]: # 堆顶元素大于当前元素
                stack.pop()

            if not stack: # 如果栈为空  没有元素小于它
                left[i] = -1  # 注意边界
            else:
                left[i] = stack[-1]
            stack.append(i)
        # 1 1 1 1
        #
        stack = []
        for i in range(len_A - 1, -1, -1):
            while stack and A[stack[-1]] >= A[i]: # 栈顶数据大于该元素 就将该元素抛出
                stack.pop()
            if not stack:
                right[i] = len_A # 如果右边不存在比该元素小的数 就赋值为 n
            else:
                right[i] = stack[-1]
            stack.append(i)

        for i in range(len_A):
            ans += (i - left[i]) * (right[i] - i) * A[i]
            ans %= 1000000007
        return ans

if __name__ == '__main__':
    A = [3, 1, 2, 4]
    s = Solution()
    ans = s.sumSubarrayMins(A)
    print(ans)
