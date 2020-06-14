# -*- coding:utf-8 -*-
"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.pLastNodeInList = None
        self.head = None
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None

        if pRootOfTree.left is None and pRootOfTree.right is None:
            return pRootOfTree


        def findRight(node):
            while node.right:
                node = node.right
            return node
        leftNode = self.Convert(pRootOfTree.left)
        rightNode = self.Convert(pRootOfTree.right)
        retNode = leftNode
        if leftNode:
            leftNode = findRight(leftNode)
        else:
            retNode = pRootOfTree

        if leftNode != None:
            leftNode.right = pRootOfTree
        if rightNode:
            pRootOfTree.right = rightNode
        pRootOfTree.left = leftNode
        return retNode

    def ConvertV1Core(self, pRootOfTree):
            if pRootOfTree is None:
                return
            pCurrent = pRootOfTree
            if pCurrent.left != None:
                self.ConvertV1Core(pCurrent.left)

            pCurrent.left = self.pLastNodeInList
            if self.pLastNodeInList:
                self.pLastNodeInList.right = pCurrent
            self.pLastNodeInList = pCurrent
            if pCurrent.right != None:
                self.ConvertV1Core(pCurrent.right)


    def ConvertV1(self, pRootOfTree):
        self.ConvertV1Core(pRootOfTree)
        pLastNodeInList = self.pLastNodeInList
        while pLastNodeInList and pLastNodeInList.left:
            pLastNodeInList = pLastNodeInList.left
        return pLastNodeInList

    def ConvertV2(self, pRootOfTree):


        def dfs(cur):
            if not cur: return
            dfs(cur.left)  # 递归左子树
            if self.pre:  # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else:  # 记录头节点
                self.head = cur
            self.pre = cur  # 保存 cur
            dfs(cur.right)  # 递归右子树

        if not pRootOfTree: return
        self.pre = None
        dfs(pRootOfTree)
        return self.head




if __name__ == '__main__':
    pass


