# -*- coding: utf-8 -*-#
"""
Created on  2020/6/14  22:24 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from common_tree import TreeNode


class Solution:

    def mostLeftLevel(self, node, level):
        while node:
            level += 1
            node = node.left
        return level - 1

    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # 最左边的高度
        h = self.mostLeftLevel(root, 1)

        def helper(node, level):
            if level == h:
                return 1

            if self.mostLeftLevel(node.right, level + 1) == h:
                # 左边为满二叉树
                return (1 << (h - level)) + helper(node.right, level + 1)
            # 否则右边为满二叉树
            return (1 << (h - level - 1)) + helper(node.left, level + 1)

        return helper(root, 1)



if __name__ == "__main__":

    node = TreeNode(1)
    node.left = TreeNode(2)
    # node.right = TreeNode(3)
    # node.left.left = TreeNode(4)
    # node.left.right = TreeNode(5)
    # node.right.left = TreeNode(6)
    s = Solution()
    res = s.countNodes(node)
    print(res)

