# -*- coding: utf-8 -*-#
"""
Created on  2020/7/10  10:05 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from typing import List


class Solution:

    def largestRectangleArea1(self, heights: List[int]) -> int:
        """ 暴力解法"""
        # 枚举高度  直到遇见左右第一个小于高度的位置
        ans = 0
        n = len(heights)
        for mid in range(0, n):
            height = heights[mid]
            left = mid
            rihgt = mid
            # 如果可以往左移动  而且 左边的高度 >= 当前高度
            while left - 1 >= 0 and heights[left - 1] >= height:
                left -= 1
            # 如果可以往右移动  而且 右边的高度 >= 当前高度
            while rihgt + 1 < n and heights[rihgt + 1] >= height:
                rihgt += 1
            ans = max((rihgt - left + 1) * height, ans)
        return ans

    def largestRectangleArea2(self, heights: List[int]) -> int:
        """ 使用单调栈解决"""
        # 枚举高度  直到遇见左右第一个小于高度的位置
        left = []
        right = []
        stack = []
        # 找到左边第一个比它小的数
        n = len(heights)
        for i in range(n - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if len(stack) == 0:
                right.append(-1)
            else:
                right.append(stack[-1])
            stack.append(i)

        stack = []
        for i in range(n):
            # 如果当前高度小于或等于栈顶
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if len(stack) == 0:
                left.append(-1)
            else:
                left.append(stack[-1])
            stack.append(i)
        ans = 0
        right = right[::-1]
        for i in range(n):
            height = heights[i]
            l = left[i]
            r = right[i]
            if l != -1 and r != -1:
                ans = max(ans, (r - l - 1) * height)
            elif l == -1 and r != -1:
                # 左边没有小于 该高度的数字
                ans = max(ans, (r - l - 1) * height)
            elif l == -1 and r == -1:
                ans = max(ans, height * n)
            elif l != -1 and r == -1:
                # 右边没有小于 该高度的数字
                ans = max(ans, (n - l - 1) * height)

        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights or len(heights) == 0:
            return 0
        stack = []
        ans = 0
        n = len(heights)
        for i in range(n):
            now_rec = -1
            if i < n:
                now_rec = heights[i]
            while stack and now_rec <= heights[stack[-1]]:
                this_height = heights[stack.pop()]
                this_width = i
                if stack:
                    this_width = i - stack[-1] -1
                ans = max(ans, this_height * this_width)
            stack.append(i)
        return ans





heights = [1, 1]
s = Solution()
ans = s.largestRectangleArea(heights)
print(ans)
