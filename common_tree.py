# -*- coding: utf-8 -*-#
"""
Created on  2020/6/14  10:33 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from queue import Queue


class TreeNode():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:

    @classmethod
    def recursive_pre_order(cls, root: TreeNode):
        if root is None:
            return

        print(root.val, end=" ")

        cls.recursive_pre_order(root.left)
        cls.recursive_pre_order(root.right)

    @classmethod
    def recursive_in_order(cls, root):
        if root is None:
            return
        cls.recursive_in_order(root.left)
        print(root.val, end=" ")
        cls.recursive_in_order(root.right)

    @classmethod
    def recursive_post_order(cls, root):
        if root is None:
            return None
        cls.recursive_post_order(root.left)
        cls.recursive_post_order(root.right)
        print(root.val, end=" ")

    @classmethod
    def non_recur_pre_order(cls, root):
        if root is None:
            return

        stack = [root]
        while stack:
            node = stack.pop()
            print(node.val, end=" ")
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        print()

    @classmethod
    def non_cur_in_order(cls, root):
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

    @classmethod
    def non_cur_post_order(cls, root):
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

    @classmethod
    def compare_tree(cls, root1: TreeNode, root2: TreeNode):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            return cls.compare_tree(root1.left, root2.left) and \
                   cls.compare_tree(root1.right, root2.right)

    @classmethod
    def serial_by_pre_order(cls, root: TreeNode):
        if root is None:
            return "#!"
        res = str(root.val) + "!"
        res += cls.serial_by_pre_order(root.left)
        res += cls.serial_by_pre_order(root.right)

        return res

    @classmethod
    def recon_by_pre_str(cls, pre_str):

        data = pre_str.split("!")[:-1]  # 注意最后一个''

        que = Queue()
        for i in range(len(data)):
            que.put(data[i])

        def helper(que):
            val = que.get()
            if val == "#":
                return None

            node = TreeNode(int(val))
            node.left = helper(que)
            node.right = helper(que)
            return node

        return helper(que)

    @classmethod
    def serial_by_in_order(cls, root: TreeNode):
        if root is None:
            return "#!"
        res = ''
        res += cls.serial_by_pre_order(root.left)
        res += str(root.val) + "!"
        res += cls.serial_by_pre_order(root.right)
        return res

    @classmethod
    def recon_by_in_str(cls, in_str):
        """未完成"""
        pass

    @classmethod
    def recon_by_level(cls, level_str):
        def generateNodeByString(val):
            if val == "#":
                return None
            return TreeNode(int(val))

        values = level_str.split("_")[:-1]
        index = 0

        head = generateNodeByString(values[0])
        que = Queue()
        if head:
            que.put(head)

        node = None
        while not que.empty():  # 如果队列非空
            node = que.get()
            index += 1
            node.left = generateNodeByString(values[index])
            index += 1
            node.right = generateNodeByString(values[index])
            if node.left:
                que.put(node.left)
            if node.right:
                que.put(node.right)

        return head

    @classmethod
    def tranvesal_by_level(cls, root):
        if not root:
            print("_", end=' ')
        que = Queue()
        que.put(root)
        while not que.empty():
            node = que.get()
            print(node.val, end=" ")

            if node.left:
                que.put(node.left)
            if node.right:
                que.put(node.right)

    @classmethod
    def serialize_by_level(cls, root: TreeNode):
        if root is None:
            return "#_"

        que = Queue()
        que.put(root)
        res = str(root.val) + "_"

        while not que.empty():
            node = que.get()
            if node.left:
                res += str(node.left.val) + "_"
                que.put(node.left)
            else:
                res += "#_"

            if node.right:
                res += str(node.right.val) + "_"
                que.put(node.right)
            else:
                res += '#_'
        return res


def test_serial_and_deserial_by_pre_order():
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.right.right = TreeNode(5)
    pre_str = Tree.serial_by_pre_order(head)
    print("pre_str:\t", pre_str)
    new_tree = Tree.recon_by_pre_str(pre_str)
    pre_str_1 = Tree.serial_by_pre_order(new_tree)
    print("pre_str_1:\t", pre_str_1)
    assert pre_str == pre_str_1


if __name__ == "__main__":
    # test_serial_and_deserial_by_pre_order()

    level_str = "1_2_3_4_#_#_5_#_#_#_#_"
    node = Tree.recon_by_level(level_str)
    print(node)
    Tree.tranvesal_by_level(node)
    res = Tree.serialize_by_level(node)
    print(res)
    assert level_str == res
