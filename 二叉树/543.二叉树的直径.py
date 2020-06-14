"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。
这条路径可能穿过也可能不穿过根结点。
"""
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree1(self, root: TreeNode) -> int:
        self.diam = 0
        def tranverse(root):
            if not root:
                return 0
            left = tranverse(root.left)
            right = tranverse(root.right)
            self.diam = max(self.diam, left+right)
            return 1 + max(left, right)

        tranverse(root)
        return self.diam


    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def traverse( root):
            if not root:
                return (0, 0) # 返回深度和左子树的直径
            left_depth, left_diam = traverse(root.left)
            right_depth, right_diam = traverse(root.right)
            depth = 1 + max(left_depth, right_depth)
            diam = max(left_diam, right_diam, left_depth + right_depth)

            return depth, diam
        depth, diam = traverse(root)
        return diam


