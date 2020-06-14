# -*- coding:utf-8 -*-
"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        pTmp = root
        stack = [root]
        ret = []
        while pTmp and stack:
            pTmp = stack.pop(0)
            ret.append(pTmp.val)
            if pTmp.left:
                stack.append(pTmp.left)
            if pTmp.right:
                stack.append(pTmp.right)

        return ret

