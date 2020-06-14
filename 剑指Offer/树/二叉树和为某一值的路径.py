# -*- coding:utf-8 -*-
"""
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


## 解法1
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径

    def FindPath(self, root, expectNum):
        if not root:
            return []
        if root.left == None and root.right == None:
            if expectNum == root.val:
                return [[root.val]]
            else:
                return []
        ## 只有一个节点

        stack = []
        leftStack = self.pathSum(root.left, expectNum - root.val)
        for i in leftStack:
            i.insert(0, root.val)
            stack.append(i)
        rightStack = self.pathSum(root.right, expectNum - root.val)

        for i in rightStack:
            i.insert(0, root.val)
            stack.append(i)
        return stack

    # 优化写法
    def pathSum(self, root, expectNum):
        if not root:
            return []
        if root.left == None and root.right == None:
            if expectNum == root.val:
                return [[root.val]]
            else:
                return []
        a = self.pathSum(root.left, expectNum - root.val) + \
            self.pathSum(root.right, expectNum - root.val)

        return [[root.val] + i for i in a]


## 解法2
import copy


class Solution1(object):
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        ret = []

        support = [root]
        supportArrayList = [[root.val]]
        while support:
            tmpNode = support[0]
            tmpArrayList = supportArrayList[0]
            if tmpNode.left is None and tmpNode.right is None:
                if sum(tmpArrayList) == expectNumber:
                    ret.insert(0, tmpArrayList)
            if tmpNode.left:
                support.append(tmpNode.left)
                newTmpArrayList = copy.copy(tmpArrayList)
                newTmpArrayList.append(tmpNode.left.val)
                supportArrayList.append(newTmpArrayList)
            if tmpNode.right:
                support.append(tmpNode.right)
                newTmpArrayList = copy.copy(tmpArrayList)
                newTmpArrayList.append(tmpNode.right.val)
                supportArrayList.append(newTmpArrayList)

            del supportArrayList[0]
            del support[0]

        return ret


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result_all = []
        self.array = []

    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        temp = []
        def dfs(root, sum_):
            if root:
                if not root.right and not root.left:  # 判断是否为叶节点
                    temp.append(root.val)
                    if sum(temp) == sum_:  # 满足条件,则添加到最终结果中
                        result.append(temp[0:])  # 此处取切片是为了深拷贝,不然temp的操作会对result进行改变
                    temp.pop()
                    return
                temp.append(root.val)  # 进栈
                dfs(root.left, sum_)
                dfs(root.right, sum_)
                temp.pop()  # 出栈

        dfs(root, sum_)
        return result

    def method2(self, root, expectNumber):
        if not root: return []
        self.array.append(root.val)
        expectNumber -= root.val
        if expectNumber == 0 and not root.left and not root.right:
            self.result_all.append(self.array[:])
            self.array.pop()
        self.pathSum(root.left, expectNumber)
        self.pathSum(root.right, expectNumber)
        self.array.pop()


if __name__ == '__main__':
    # 10,5,12,4,7

    node7 = TreeNode(7)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node12 = TreeNode(12)
    node10 = TreeNode(10)
    node10.left = node5
    node10.right = node12
    node5.left = node4
    node5.right = node7

    s = Solution1()
    ret = s.FindPath(node10, 22)
    print(ret)
