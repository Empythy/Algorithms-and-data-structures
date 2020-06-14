# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre = None
        # 类似后序遍历
        def helper(root):
            if not root:
                return self.pre
            # 记录遍历时候,该节点的前一个节点
            helper(root.right)
            helper(root.left)
            # 拼接
            root.right = self.pre
            root.left = None
            self.pre = root

        helper(root)


class Solution1:
    """先序遍历"""

    def flatten(self, root: TreeNode) -> None:
        if root != None:
            # 处理root
            l, r = root.left, root.right
            root.left = None
            root.right = l
            # 处理root.left
            self.flatten(l)
            # 将root.right接到结果单链表后面
            if l != None:
                while l.right != None:
                    l = l.right
                l.right = r
            else:
                root.right = r
            # 处理root.right
            self.flatten(r)


class Solution2(object):

    def flatten(self, root):
        """前序遍历 + 队列 """
        if not root:
            return
        queue = deque([])

        # 前序遍历整棵二叉树，并将遍历的结果放到数组中
        def dfs(root):
            if not root:
                return
            queue.append(root)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        head = queue.popleft()
        head.left = None
        # 遍历链表，将链表中的TreeNode节点前后串联起来
        while queue:
            tmp = queue.popleft()
            tmp.left = None
            head.right = tmp
            head = tmp

    def flatten1(self, root):
        # 前序遍历 + stack
        if not root:
            return
        stack = [root]
        pre = TreeNode(-1)
        while stack:
            # 用栈作为辅助数据结构，从栈中弹出元素后
            # 先将右节点放到栈中，再将左节点放入栈中，模拟前序遍历
            tmp = stack.pop()
            pre.left, pre.right = None, tmp
            # 先放入右节点，再放入左边点，顺序不能反了
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
            pre = tmp

    def flatten2(self, root):
        # 后序遍历
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            # 将右子树挂到 左子树的最右边
            # 再将整个左子树挂到根节点的右边
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None
        dfs(root)


    def flatten3(self, root):
        self.pre = None

        def dfs(root):
            if not root:
                return None
            # 右节点-左节点-根节点 这种顺序正好跟前序遍历相反
            # 用pre节点作为媒介，将遍历到的节点前后串联起来
            dfs(root.right)
            dfs(root.left)
            root.left = None
            root.right = self.pre
            self.pre = root

        dfs(root)


