# -*- coding: utf-8 -*-#
"""
Created on  2020/6/14  8:58 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from common_tree import TreeNode



class ReturnData(object):

    def __init__(self, is_b, h):
        self.is_b = is_b
        self.h = h


def is_balance(root)->ReturnData:

    if root is None:
        return ReturnData(True, 0)

    left = is_balance(root.left)

    if not left.is_b:
        return ReturnData(False, -1)

    right = is_balance(root.right)

    if not right.is_b:
        return ReturnData(False, -1)

    if abs(left.h - right.h)>1:
        return ReturnData(False, -1)

    return ReturnData(True, max(left.h, right.h) + 1)

def isBalance(root):
    res = is_balance(root)
    print(res)
    return is_balance(root).is_b

if __name__ == "__main__":

    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    isBalance(head)