# -*- coding:utf-8 -*-
"""
输入一个链表，输出该链表中倒数第k个结点
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def FindKthToTail(self, head, k):
        # write code here
        """
        判断k的值
        如果k大于链表长度 返回None
        """
        first_point = head
        second_point = head
        if k < 0:
            return None

        for i in range(k):
            if first_point == None :
                return None
            first_point = first_point.next

        while first_point:
            first_point = first_point.next
            second_point = second_point.next

        return second_point.val
