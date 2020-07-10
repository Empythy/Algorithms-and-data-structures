# -*- coding: utf-8 -*-#
"""
Created on  2020/7/10  9:04 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) != len(inorder): return None
        if len(preorder) == 0: return None

        val = preorder[0]
        root = TreeNode(val)
        left_pre, right_pre, left_in, right_in = self.split(preorder, inorder)
        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)

        return root

    def split(self, preorder, inorder):
        left_in = []
        right_in = []
        val = preorder[0]  # 根

        inoder_index = inorder.index(val)
        left_pre = inorder[:inoder_index]
        right_pre = inorder[inoder_index+1:]


        for item in preorder:
            if item in left_in:
                left_pre.append(item)
            elif item in right_in:
                right_pre.append(item)

        return left_pre, right_pre, left_in, right_in



if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    ans = s.buildTree(preorder, inorder)