"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
这条路径上所有节点值相加等于目标和
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        sum -= root.val
        if root.left is None and root.right is None:
            return sum == 0
        left = self.hasPathSum(root.left, sum)
        right = self.hasPathSum(root.right, sum)
        return left or right

    def test(self, root, sum):
        """刚才莫名报错"""
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        left = self.hasPathSum(root.left, sum - root.val)
        right = self.hasPathSum(root.right, sum - root.val)
        return left or right
