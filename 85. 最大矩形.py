# -*- coding: utf-8 -*-#
"""
Created on  2020/7/10  11:12 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        rows = len(matrix)
        if rows == 0: return 0

        cols = len(matrix[0])
        ans = 0
        nums = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    nums[j] += 1
                elif matrix[i][j] == '0':
                    nums[j] = 0
            print("i......:", nums)
            ans = max(ans, self.findmaxRectangle(nums))

        return ans

    def findmaxRectangle(self, nums):
        if not nums or len(nums) == 0:
            return 0

        ans = 0
        left = []
        right = []
        stack = []
        n = len(nums)
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                left.append(stack[-1])
            else:
                left.append(-1)
            stack.append(i)
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                right.append(stack[-1])
            else:
                right.append(-1)
            stack.append(i)
        right = right[::-1]
        for i in range(n):
            j = left[i]  # 左边
            k = right[i]  # 右边
            if j == -1 and k == -1:
                ans = max(ans, nums[i] * n)
            elif j == -1 and k != -1:
                ans = max(ans, k * nums[i])
            elif j != -1 and k == -1:
                ans = max(ans, (n - j - 1) * nums[i])
            elif j != -1 and k != -1:
                ans = max(ans, (k - j - 1) * nums[i])

        return ans



maxtrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

s = Solution()
ans = s.maximalRectangle(maxtrix)
print(ans)


