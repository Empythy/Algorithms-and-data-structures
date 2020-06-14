# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here

        pReversedHead = None
        pNode = pHead
        pPrev = None
        while pNode != None:
            pNext = pNode.next
            if pNext == None:
                pReversedHead = pNode

            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pReversedHead

    def method(self, pHead):
        if pHead == None:  # 空
            return None
        if pHead.next == None:  # 只有一个节点
            return pHead

        leftPointer = pHead
        midPointer = pHead.next
        rightPointer = pHead.next.next
        leftPointer.next = None

        while rightPointer != None:
            midPointer.next = leftPointer
            leftPointer = midPointer
            midPointer = rightPointer
            rightPointer = rightPointer.next
        midPointer.next = leftPointer

        return midPointer

    def ReverseListRec(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        else:
            pReversedHead = self.ReverseList(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
            return pReversedHead
