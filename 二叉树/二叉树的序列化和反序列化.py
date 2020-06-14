# -*- coding: utf-8 -*-#
"""
Created on  2020/6/14  0:15 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from queue import Queue


class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree(object):

    def serial_by_pre(self, root):
        if root is None:
            return "#!"

        res = str(root.val) + "!"
        res += self.serial_by_pre(root.left)
        res += self.serial_by_pre(root.right)
        return res

    def recon_pre_order(self, que: Queue):
        val = que.get()
        if val == "#":
            return None

        node = TreeNode(int(val))
        node.left = self.recon_pre_order(que)
        node.right = self.recon_pre_order(que)
        return node


    def recon_by_pre_str(self, pre_str):
        values = pre_str.split("!")

        queue = Queue()
        for i in range(len(values)-1):
            queue.put(values[i])

        return self.recon_pre_order(queue)


if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.right.right = TreeNode(5)

    tree = Tree()
    print("=" * 30)

    pre = tree.serial_by_pre(head)
    print(pre)

    new_tree = tree.recon_by_pre_str(pre)
    print(new_tree.val)
    print(tree.serial_by_pre(new_tree))