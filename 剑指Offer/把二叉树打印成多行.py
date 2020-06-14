"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        ret = []
        deque1 = [pRoot]
        deque2 =[]
        while deque1 or deque2:
            if deque1:
                tmpRet = []
                while deque1:
                    tmpNode = deque1.pop(0)
                    tmpRet.append(tmpNode.val)
                    if tmpNode.left:
                        deque2.append(tmpNode.left)
                    if tmpNode.right:
                        deque2.append(tmpNode.right)
                ret.append(tmpRet)
            if deque2:
                tmpRet = []
                while deque2:
                    tmpNode = deque2.pop(0)
                    tmpRet.append(tmpNode.val)
                    if tmpNode.left:
                        deque1.append(tmpNode.left)
                    if tmpNode.right:
                        deque1.append(tmpNode.right)
                ret.append(tmpRet)

        return ret
