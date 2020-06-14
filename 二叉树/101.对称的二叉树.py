"""
给定一个二叉树，检查它是否是镜像对称的。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root, root)

    def helper(self, left, right):
        if not left and not right:
            return True

        if not left and right:
            return False

        if left and not right:
            return False

        if left.val == right.val:
            return self.helper(left.left, right.right) and self.helper(left.right, right.left)
        else:
            return False
