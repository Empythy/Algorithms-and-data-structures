# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        pTmp1 = pHead1
        pTmp2 = pHead2
        ## 计算长度差
        while pTmp1 and pTmp2:
            if pTmp1 == pTmp2:
                return pTmp1
            pTmp1 = pTmp1.next
            pTmp2 = pTmp2.next
        k = 0
        isPTmp1Longer = False

        if pTmp1 is None and pTmp2:
            while pTmp2:
                pTmp2 = pTmp2.next
                k += 1


        if pTmp2 is None and pTmp1:
            while pTmp1:
                pTmp1 = pTmp1.next
                k += 1
            isPTmp1Longer = ~isPTmp1Longer

        pTmp1 = pHead1
        pTmp2 = pHead2

        if isPTmp1Longer:
            for i in range(k):
                pTmp1 = pTmp1.next
        else:
            for i in range(k):
                pTmp2 = pTmp2.next

        while pTmp1 and pTmp2:
            if pTmp1 == pTmp2:
                return pTmp1
            else:
                pTmp1 = pTmp1.next
                pTmp2 = pTmp2.next

        return None
