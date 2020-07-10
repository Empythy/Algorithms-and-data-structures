# -*- coding: utf-8 -*-#
"""
Created on  2020/7/4  18:05 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
import heapq
from typing import List

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i], i))
                lists[i] = lists[i].next

        head = tmp_head = ListNode(None)

        while heap:
            val, idx = heapq.heappop(heap)
            new_node = ListNode(val)
            tmp_head.next = new_node
            tmp_head = tmp_head.next
            if not lists[idx] is None:
                heapq.heappush(heap, (lists[idx].next.val, idx))
                lists[idx] = lists[idx].next

        return head.next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        heap = []
        # 首先 for 嵌套 while 就是将所有元素都取出放入堆中
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        dummy = ListNode(None)
        cur = dummy
        # 依次将堆中的元素取出(因为是小顶堆，所以每次出来的都是目前堆中值最小的元素），然后重新构建一个列表返回
        while heap:
            temp_node = ListNode(heapq.heappop(heap))
            cur.next = temp_node
            cur = temp_node
        return dummy.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)

        # basic cases
        if n == 0: return None
        if n == 1: return lists[0]
        if n == 2: return self.mergeTwoLists(lists[0], lists[1])

        # divide and conqure if not basic cases
        mid = n // 2
        return self.mergeTwoLists(self.mergeKLists(lists[:mid]),
                                  self.mergeKLists(lists[mid:n]))

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        c1, c2, c3 = l1, l2, res
        while c1 or c2:
            if c1 and c2:
                if c1.val < c2.val:
                    c3.next = ListNode(c1.val)
                    c1 = c1.next
                else:
                    c3.next = ListNode(c2.val)
                    c2 = c2.next
                c3 = c3.next
            elif c1:
                c3.next = c1
                break
            else:
                c3.next = c2
                break

        return res.next

