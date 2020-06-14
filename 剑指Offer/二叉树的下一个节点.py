
"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""
# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
            return None
        # 1.寻找右子树 如果存在就找到右子树的最左边
        # 2. 否则 寻找他的父节点 一直找到它是父节点的左子树 打印父节点


        if pNode.right:
            tmpNode = pNode.right
            while tmpNode.left:
                tmpNode = tmpNode.left
            return tmpNode

        else:
            tmpNode = pNode

            while tmpNode.next:
                if tmpNode.next.left == tmpNode:
                    return tmpNode.next
                tmpNode =tmpNode.next

            return None
