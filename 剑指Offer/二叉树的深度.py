# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        return self.depth(pRoot)

    def depth(self, root):
        if root is None:
            return 0
        # deep = 1
        from collections import deque
        dq = deque()
        layer = 1
        dq.append((root, 1))
        while dq:
            node, layer = dq.popleft()
            deep = layer
            if node.left:
                dq.append((node.left, layer + 1))
            if node.right:
                dq.append((node.right, layer + 1))
        return deep