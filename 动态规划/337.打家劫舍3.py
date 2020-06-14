# Definition for a binary tree node.
from functools import lru_cache


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    @lru_cache(None)
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # 抢劫
        left = 0 if root.left is None else self.rob(root.left.left) + self.rob(root.left.right)
        right = 0 if root.right is None else self.rob(root.right.left) + self.rob(root.right.right)
        do_it = root.val + left + right
        not_do = self.rob(root.left) + self.rob(root.right)
        res = max(do_it, not_do)
        return res

