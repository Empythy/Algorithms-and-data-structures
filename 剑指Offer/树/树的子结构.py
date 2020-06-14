# -*- coding:utf-8 -*-
"""
输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 is None or pRoot2 is None:
            return False

        if pRoot1.val == pRoot2.val:
            ret = self.hasEqual(pRoot1, pRoot2)
            if ret:
                return True
        return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def hasEqual(self, pRoot1, pRoot2):

        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False

        if pRoot1.val == pRoot2.val:
            if pRoot2.left is None:
                leftEqual = True
            else:
                leftEqual = self.hasEqual(pRoot1.left, pRoot2.left)

            if pRoot2.right is None:
                rightEqual = True
            else:
                rightEqual = self.hasEqual(pRoot1.right, pRoot2.right)
            return leftEqual and rightEqual
        return False
