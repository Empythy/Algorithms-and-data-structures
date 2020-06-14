# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        nums = self.inOder(root)
        n = len(nums)
        if n == 0:
            return []
        res = [1, nums[0]]
        index = 0
        n = len(nums)
        cnt = 0
        while index < n - 1:
            if nums[index] == nums[index + 1]: # 如果下一个数和当前数相等
                cnt += 1
            else:  #  否则判断数字个数是否大
                if cnt > res[0]:
                    res = [cnt, nums[index]]
                else:
                    res.append(nums[index])
                cnt = 1

            index += 1
        # 边界条件
        if cnt > res[0]:
            res = [cnt, nums[index]]
        else:
            res.append(nums[index])
        return res[1:]

    def inOder(self, root) -> List[int]:
        if not root:
            return []
        return self.inOder(root.left) + [root.val] + self.inOder(root.right)
