# -*- coding:utf-8 -*-
"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，
一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，
否则判题程序会直接返回空）
"""
import copy


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        # return copy.deepcopy(pHead)
        if pHead is None:
            return None

        if pHead.next is None:
            newHead= RandomListNode(pHead.label)
            return newHead


        pTmp = pHead
        # 复制节点
        while pTmp:
            node = RandomListNode(pTmp.label)
            node.next = pTmp.next
            pTmp.next = node
            pTmp = node.next

        # 实现 新建node random指向
        pTmp = pHead
        while pTmp:
            if pTmp.random:
                pTmp.next.random = pTmp.random.next
            pTmp = pTmp.next.next

        pTmp = pHead
        newHead = pHead.next
        pNewTmp = pHead.next

        while pTmp:
            pTmp.next = pTmp.next.next
            if pNewTmp.next:
                pNewTmp.next = pNewTmp.next.next
                pNewTmp = pNewTmp.next
            pTmp = pTmp.next

        return newHead

if __name__ == '__main__':
    node1 = RandomListNode(1)
    # node2 = RandomListNode(2)
    # node3 = RandomListNode(3)
    # node4 = RandomListNode(4)
    # node5 = RandomListNode(5)
        # node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5

    newHead = Solution().Clone(node1)

    while newHead:
        print(newHead.label)
        newHead = newHead.next




