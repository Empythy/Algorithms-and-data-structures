# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        stack1= [pRoot]
        stack2 = []
        ret = []

        while stack1 or stack2:
            tmpRet = []
            if stack1:
                while stack1:
                    tmpNode = stack1.pop()
                    tmpRet.append(tmpNode.val)
                    if tmpNode.left:
                        stack2.append(tmpNode.left)
                    if tmpNode.right:
                        stack2.append(tmpNode.right)

                ret.append(tmpRet)

            if stack2:
                tmpRet = []
                while stack2:
                    tmpNode = stack2.pop()
                    tmpRet.append(tmpNode.val)
                    if tmpNode.right:
                        stack1.append(tmpNode.right)
                    if tmpNode.left:
                        stack1.append(tmpNode.left)
                ret.append(tmpRet)
        return ret