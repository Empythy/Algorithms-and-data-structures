# -*- coding:utf-8 -*-
"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，
否则，输出null。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here

        ## 先判断有没有环
        pFast = pHead
        pSlow = pHead
        while pFast and pFast.next:
            pFast = pFast.next.next
            pSlow = pSlow.next
            if pFast == pSlow:
                break


        if pFast is None or pFast.next is None:
            return None


        """
        slow L
        fast 2L 
        开始到第一个点 s
        slow 在环中没走的长度是m
                
        2L = s + (m + d)*n + d  走n圈
        L = s + d
        """
        pFast = pHead
        while pFast != pSlow:
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast

