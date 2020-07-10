# -*- coding: utf-8 -*-#
"""
Created on  2020/7/5  14:32 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:

        slow = head
        fast = head
        while k and fast:
            fast = fast.next
            k -= 1
        if k > 0: return None

        while fast:
            fast = fast.next
            slow = slow.next

        return slow