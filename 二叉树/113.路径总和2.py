# Definition for a binary tree node.
from typing import List
"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和
    等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        def backtack(track, root, sum):
            if not root:
                return
            if not root.left and not root.right and root.val == sum:
                # 满足条件
                # track.append(root.val)
                track += [root]
                res.append(track)
                # self.res.append(track.copy())
                # track.pop()

            # track.append(root.val)
            track += [root.val]
            backtack(track, root.left, sum-root.val)
            backtack(track, root.right, sum-root.val)
            # track.pop()

        backtack([], root, sum)
        return res








