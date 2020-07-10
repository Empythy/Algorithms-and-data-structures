# -*- coding: utf-8 -*-#
"""
Created on  2020/7/6  16:02 
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
    def trans(self, path):
        ans = 0
        for i in range(len(path)):
            ans += path[i] * 10 ** (len(path) - i - 1)
        return ans

    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = []

        def dfs(path, node):

            if not node:
                return

            if not node.left and not node.right:
                self.ans.append(
                    self.trans(path + [node.val, ])
                )
                return

            for child in [node.left, node.right]:
                dfs(path + [node.val], child)

        dfs([], root)
        print(self.ans)
        return sum(self.ans)

if __name__ == '__main__':
    root = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root.left = root2
    root.right = root3
    s = Solution()
    ans = s.sumNumbers(root)
    print(ans)