# -*- coding:utf-8 -*-
"""
输入两个单调递增的链表，输出两个链表合成后的链表，当
然我们需要合成后的链表满足单调不减规则。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表

    def Merge_test(self, pHead1, pHead2):

        if pHead1 is None:
            return pHead2

        if pHead2 is None:
            return pHead1

        newHead = None
        head = None
        while pHead1 and pHead2 :
            if pHead1.val > pHead2.val:
                newNode = pHead2
                pHead2 = pHead2.next

            else:
                newNode = pHead1
                pHead1 = pHead1.next

            # 返回重建节点的头节点
            if newHead is None:
                newHead = newNode
                head = newNode
            else:
                head.next = newNode
                head = head.next

        while pHead1:
            head.next = pHead1
            head = head.next
            pHead1 = pHead1.next

        while pHead2:
            head.next = pHead2
            head = head.next
            pHead2 = pHead2.next

        return newHead


    def Merge(self, pHead1, pHead2):

        # write code here success
        if pHead1 is None:
            return pHead2

        if pHead2 is None:
            return pHead1

        newHead = pHead1 if pHead1.val < pHead2.val else pHead2
        pTmp1 = pHead1
        pTmp2 = pHead2
        if newHead == pTmp1:
            pTmp1 = pTmp1.next
        else:
            pTmp2 = pTmp2.next
        previousPointer = newHead

        while pTmp1 and pTmp2:
            if pTmp1.val < pTmp2.val:
                previousPointer.next = pTmp1
                pTmp1 = pTmp1.next
            else:
                previousPointer.next = pTmp2
                pTmp2 = pTmp2.next
            previousPointer = previousPointer.next

        while pTmp1:
            previousPointer.next = pTmp1
            pTmp1 = pTmp1.next
            previousPointer = previousPointer.next
        while pTmp2:
            previousPointer.next = pTmp2
            pTmp2 = pTmp2.next
            previousPointer = previousPointer.next

        return newHead


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(5)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(2)
    node5 = ListNode(4)
    node6 = ListNode(6)
    node4.next = node5
    node5.next = node6

    S = Solution()
    # ret = S.Merge_test(node1, node4)
    #
    # while ret:
    #     print(ret.val)
    #     ret = ret.next

    ret2 = S.Merge_test(node1, node4)
    ret = ret2
    while ret:
        print(ret.val)
        ret = ret.next
