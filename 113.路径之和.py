# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []

        def dfs(node, path, sum_):
            if not node:
                return
            sum_ += node.val
            path.append(node.val)
            if not node.left and not node.right and sum_ == sum:
                res.append(path.copy())

            for child in [node.left, node.right]:
                dfs(child, path, sum_)
            sum_ -= node.val
            path.pop()
        dfs(root, [], 0)
        return res



    def pathSum2(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []

        def dfs(track, root, sum):
            if not root:
                return
            if not root.left and not root.right and root.val == sum:
                # 满足条件
                # track.append(root.val)
                self.res.append(track + [root.val])
                # self.res.append(track.copy())
                # track.pop()
                return

            dfs(track + [root.val], root.left, sum - root.val)
            dfs(track + [root.val], root.right, sum - root.val)

        dfs([], root, sum)
        return self.res

def create_data():
    # data = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    t5 = TreeNode(5)

    t4 = TreeNode(4)
    t8 = TreeNode(8)
    t5.left = t4
    t5.right = t8

    t11 = TreeNode(11)
    t4.left = t11

    t7 = TreeNode(7)
    t2 = TreeNode(2)
    t11.left = t7
    t11.right = t2

    t13 = TreeNode(13)
    t4_1 = TreeNode(4)

    t8.left = t13
    t8.right = t4_1

    t5_1 = TreeNode(5)
    t1 =TreeNode(1)
    t4_1.left = t5_1
    t4_1.right = t1
    return t5


def pre_order(root):
    if not root:
        print("None")
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)
root = create_data()

# pre_order(root)
s = Solution()
res = s.pathSum(root, 22)
print(res)
res1 = s.pathSum2(root, 22)
print(res1)




