'''

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''


# -*- coding:utf-8 -*-

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def Convert(self, pRootOfTree):
        # or (pRootOfTree.left is None and pRootOfTree.right is None)
        if pRootOfTree is None:
            return pRootOfTree

        def find_right(node):
            while node.right:
                node = node.right

            return node

        leftNode = self.Convert(pRootOfTree.left)
        rightNode = self.Convert(pRootOfTree.right)

        retNode = leftNode

        if leftNode:
            leftNode = find_right(leftNode)
        else:
            retNode = pRootOfTree

        pRootOfTree.left = leftNode
        pRootOfTree.right = rightNode

        if leftNode != None:
            leftNode.right = pRootOfTree
        if rightNode != None:
            rightNode.left = pRootOfTree

        return retNode


if __name__ == '__main__':
    pNode1 = TreeNode(8)
    pNode2 = TreeNode(6)
    pNode3 = TreeNode(10)
    pNode4 = TreeNode(5)
    pNode5 = TreeNode(7)
    pNode6 = TreeNode(9)
    pNode7 = TreeNode(11)
    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode2.right = pNode5
    pNode3.left = pNode6
    pNode3.right = pNode7
    S = Solution()
    newList = S.Convert(pNode1)

    while newList:
        print(newList.val)
        newList = newList.right
