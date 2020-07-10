# -*- coding: utf-8 -*-#
"""
Created on  2020/6/14  10:05 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from common import TreeNode

"""
搜索二叉树一般没有重复节点，如果有也可以压缩在同一个节点上
左子树的值 < 根节点的值 < 小于 右子树的值

非递归中序遍历
"""


def is_bst(root) -> bool:
    if not root:
        return True

    pre_val = float('-inf')
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.val < pre_val:
                return False
            pre_val = node.val
            node = node.right
    return True


def is_bst_recursive(root):
    def helper(root, min_val, max_val):
        if root is None:
            return True

        if min_val < root.val < max_val:
            return helper(root.left, min_val, root.val) and \
                   helper(root.right, root.val, max_val)
        else:
            return False

    return helper(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    head = TreeNode(4)
    head.left = TreeNode(2)
    head.right = TreeNode(6)
    head.left.left = TreeNode(1)
    head.left.right = TreeNode(3)
    head.right.left = TreeNode(5)
    print(is_bst(head))
