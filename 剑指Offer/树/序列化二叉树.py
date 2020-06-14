# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        ret = []
        def preOrder(root):
            if root is None:
                ret.append("#")
                return
            ret.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)
        return " ".join(ret)

    def Deserialize(self, s):
        # write code here
        retList = s.split()
        def dePreOder():
            if len(retList) == 0:
                return None
            rootVal = retList[0]
            del retList[0]
            if rootVal == "#":
                return None
            node = TreeNode(int(rootVal))

            leftNode = dePreOder()
            rightNode = dePreOder()

            node.left = leftNode
            node.right = rightNode
            return node
        pRoot = dePreOder()
        return pRoot
