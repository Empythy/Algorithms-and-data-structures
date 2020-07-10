# -*- coding: utf-8 -*-#
"""
Created on  2020/7/6  14:33 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            path_sum = root.val + max(0, left) + max(0, right)
            self.res = max(self.res, path_sum)

            return root.val + max(0, max(left, right))

        dfs(root)
        return self.res


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return 0

        left = self.traverse(root.left)  # 最大以左子树根开头路径和
        right = self.traverse(root.right)  # 最大以右子树根开头路径和
        maxPathSum = root.val + max(0, left) + max(0, right) # 包含三种情况
        self.res = max(self.res, maxPathSum)
        return root.val + max(0, max(left, right))


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == sum

        left = self.hasPathSum(root.left, sum - root.val)
        right = self.hasPathSum(root.right, sum - root.val)
        return left or right


if __name__ == "__main__":
    root = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root.left = root2
    root.right = root3
    s = Solution()
    ans = s.maxPathSum(root)
    print(ans)
