# -*- coding: utf-8 -*-#
"""
Created on  2020/7/6  15:46 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0


        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left and right:
            return 1 + min(left, right)
        elif left:
            return 1 + left
        else:
            return 1 + right



if __name__ == '__main__':
    root = TreeNode(1)
    s = Solution()
    ans = s.minDepth(root)
    print(ans)