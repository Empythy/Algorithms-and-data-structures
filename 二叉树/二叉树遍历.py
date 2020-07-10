# -*- coding: utf-8 -*-#
"""
Created on  2020/6/13  9:28 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def recursive_pre_order(root: TreeNode):
    if root is None:
        return

    print(root.val, end=" ")
    recursive_pre_order(root.left)
    recursive_pre_order(root.right)


def recursive_in_order(root):
    if root is None:
        return
    recursive_in_order(root.left)
    print(root.val, end=" ")
    recursive_in_order(root.right)


def recursive_post_order(root):
    if root is None:
        return None
    recursive_post_order(root.left)
    recursive_post_order(root.right)
    print(root.val, end=" ")



def non_recur_pre_order(root):
    if root is None:
        return None

    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=" ")
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    print()

def non_cur_in_order(root):
    print("in-order")
    if root is None:
        return None

    stack = []
    node = root
    while (stack or node):
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.val, end=" ")
            node = node.right

    print()

def non_cur_post_order(root):
    print("pos-order: ")
    if root is None:
        return

    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        print(stack2.pop().val, end=" ")

    print()

if __name__ == "__main__":
    head = TreeNode(5)
    head.left = TreeNode(3)
    head.right = TreeNode(8)
    head.left.left = TreeNode(2)
    head.left.right = TreeNode(4)
    head.left.left.left = TreeNode(1)
    head.right.left = TreeNode(7)
    head.right.left.left = TreeNode(6)
    head.right.right = TreeNode(10)
    head.right.right.left = TreeNode(9)
    head.right.right.right = TreeNode(11)

    print("==============recursive==============")
    print("pre-order: ")
    recursive_pre_order(head)
    print()
    print("in-order: ")
    recursive_in_order(head)
    print()
    print("pos-order: ")
    recursive_post_order(head)
    print()

    print("============unrecursive=============")
    non_recur_pre_order(head)
    non_cur_in_order(head)
    non_cur_post_order(head)
