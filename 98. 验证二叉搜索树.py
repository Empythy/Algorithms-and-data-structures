# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            # 判断 node.val 是否大于左子树  是否小于右子树
            if not node:
                return True
            val = node.val
            if val <= lower or val > upper:
                return False

            if not helper(node.right, val, upper):
                return False

            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

    def method(self, root):
        if not root:
            return True
        pre_val = float('-inf')

        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.val <= pre_val:
                    return False
                pre_val = node.val
                node = node.right