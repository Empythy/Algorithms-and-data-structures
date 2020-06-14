"""
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []

        def dfs(node, tmp, res):
            if not node:
                return
            if not node.left and not node.right:  # 判断当前结点是否为叶子结点，是的话返回值，加入到res列表中
                res.append(int(tmp + str(node.val)))
                return
            tmp += str(node.val)
            dfs(node.left, tmp, res)
            dfs(node.right, tmp, res)

        dfs(root, '', res)
        return sum(res)


class Solution1:
    def sumNumbers(self, root: TreeNode) -> int:
        # 用来记录各个路径的结果
        all_num = []


        def helper(node, tmp_sum):
            if not node:
                return
            # 此时为叶子节点
            if not node.left and not node.right:
                all_num.append(tmp_sum * 10 + node.val)
                return

            # 根据题目意思选择先序遍历
            helper(node.left, tmp_sum * 10 + node.val)
            helper(node.right, tmp_sum * 10 + node.val)

        helper(root, 0)

        return sum(all_num)



