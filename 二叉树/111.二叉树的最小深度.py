# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        return 1 + min(self.minDepth(root.left),
                    self.minDepth(root.right))

class Solution1:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        dq = deque([(1, root)])
        while dq:
            depth, node = dq.popleft()
            children = [root.left, root.right]
            if not any(children): # 如果到达了一个叶节点
                return depth
            for c in children:
                if c:
                    dq.append((depth+1, c))

            # if node.left and node.right:
            #     # 如果一个节点都含有左右子节点
            #     dq.append((depth+1, node.left))
            #     dq.append((depth+1, node.right))
            # else:
            #     # 直接返回
            #     return depth

