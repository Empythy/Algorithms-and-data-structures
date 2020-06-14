# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        def findRight(node):
            while node.right:
                node = node.right
            return node

        if not root or (not root.left and not root.right):
            return root
        left_node = self.treeToDoublyList(root.left)

        right_node = self.treeToDoublyList(root.right)

        ret_node = left_node

        if left_node:
            left_node = findRight(left_node)
        else:
            ret_node = root
        if right_node:
            root.right = right_node

        ret_node.left = left_node
        return ret_node

    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None

        if pRootOfTree.left is None and pRootOfTree.right is None:
            return pRootOfTree

        def findRight(node):
            while node.right:
                node = node.right
            return node

        leftNode = self.Convert(pRootOfTree.left)
        rightNode = self.Convert(pRootOfTree.right)

        retNode = leftNode

        if leftNode:
            leftNode = findRight(leftNode)
        else:
            retNode = pRootOfTree

        if leftNode != None:
            leftNode.right = pRootOfTree
        if rightNode:
            pRootOfTree.right = rightNode
        pRootOfTree.left = leftNode
        return retNode


class Solution2:
    def __init__(self):
        self.head = None
        self.tail = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':

        def dfs(cur):
            # 中序遍历
            if not cur: return
            dfs(cur.left)  # 递归左子树
            if self.pre:  # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else:  # 记录头节点
                self.head = cur
            self.pre = cur  # 保存 cur
            dfs(cur.right)  # 递归右子树

        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


