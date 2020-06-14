class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def Mirror(self, root):
        if root is None:
            return None
        ## 处理根节点
        ## 处理左子树
        ## 处理右子树
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)

        return root




