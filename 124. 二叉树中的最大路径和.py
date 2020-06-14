class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        def tranverse(root):
            if not root:
                return 0
            left = max(tranverse(root), 0)
            right = max(tranverse(root), 0)

            maxPathSum = root.val + left + right
            self.ans =  max(self.ans, maxPathSum)
            return root.val + max(left, right)
        tranverse(root)
        return self.ans


class Solution1:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)

        maxPathSum = root.val + max(0, left) + max(0, right)

        self.res = max(self.res, maxPathSum)
        return root.val + max(0, max(left, right))