# Definition for a binary tree node.
from queue import Queue
from typing import List
from common import create_tree

"""
queue 模块中有 
Queue   先入先出
LifoQueue  后入先出
PriorityQueue # 数据可设置优先级


"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from queue import Queue


class Solution:

    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        # deque = collections.deque([root])
        q = Queue()
        q.put(root)
        ret = []
        # ret.append(root.val)
        while q.qsize() > 0:
            size = q.qsize()
            for i in range(size):
                node = q.get()
                if i == size - 1:
                    ret.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
        return ret


l = [1, 2, 3, None, 5, None, 4]

root = create_tree(l, TreeNode)

s = Solution()
res = s.rightSideView(root)
print(res)
