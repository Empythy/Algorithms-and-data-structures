"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""


# -*- coding:utf-8 -*-


# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False

        rootNum = sequence.pop()
        index = None
        for i in range(len(sequence)-1):
            if index == None and sequence[i] > rootNum:
                index = i
            if index != None and sequence[i] < rootNum:
                return False
        if len(sequence[:index]) == 0:
            leftRet = True
        else:
            leftRet =  self.VerifySquenceOfBST(sequence[:index])
        if len(sequence[index:]) == 0:
            rightRet = True
        else:
            rightRet = self.VerifySquenceOfBST(sequence[index:])
        return leftRet and rightRet



class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == []:
            return False

        root = sequence[-1]
        index = None
        for i in range(len(sequence) - 1):
            if index == None and root < sequence[i]:
                index = i
            if index != None and sequence[i] < root:
                return False

        if len(sequence[:index]) == 0:
            leftRet = True
        else:
            leftRet = self.VerifySquenceOfBST(sequence[:index])
        if len(sequence[index:-1]) == 0:
            rightRet = True
        else:
            rightRet = self.VerifySquenceOfBST(sequence[index:-1])
        return leftRet and rightRet
