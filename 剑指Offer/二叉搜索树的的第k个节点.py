# -*- coding:utf-8 -*-
"""
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如,(5，3，7，2，4，6，8) 中，按
结点数值大小顺序第三小结点的值为4。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 返回对应节点TreeNode
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        retList = []
        if pRoot is None:
            return None

        def inOrder(pRoot):
            if pRoot is None:
                return None
            inOrder(pRoot.left)
            retList.append(pRoot)
            inOrder(pRoot.right)

        inOrder(pRoot)
        if len(retList) < k or k < 1:
            return None
        return retList[k - 1]

if __name__ == '__main__':
    node8 = TreeNode(8)
    node6 = TreeNode(6)
    node5 = TreeNode(5)
    node7 = TreeNode(7)
    node10 = TreeNode(10)
    node9 = TreeNode(9)
    node11 = TreeNode(11)
    node8.left = node6
    node8.right = node10
    node6.left = node5
    node6.right = node7
    node10.left = node9
    node10.right = node11

    # inOrder(node8)
    # print(retList)
    s = Solution()
    ret = s.KthNode(node8, 1)
    print(ret.val)
