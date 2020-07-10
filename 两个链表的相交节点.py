# -*- coding: utf-8 -*-#
"""
Created on  2020/7/5  18:27 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def get_len(self, head):
        cnt = 0
        t = head
        while t:
            cnt += 1
            t = t.next
        return cnt

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_A = self.get_len(headA)
        len_B = self.get_len(headB)

        t1, t2 = headA, headB
        k = len_B - len_A
        if k > 0:
            while k:
                t2 = t2.next
                k -= 1

        else:
            k = abs(k)
            while k:
                t1 = t1.next
                k -= 1

        while t1 and t2:
            if t1 is t2:
                return t1

            t1 = t1.next
            t2 = t2.next

        return None


def create_list(l):
    node_ls = [ListNode(item) for item in l]
    for i in range(len(l) - 1):
        node_ls[i].next = node_ls[i + 1]

    return node_ls[0]


def print_list(head):
    ls = []
    t = head
    while t:
        ls.append(str(t.val))
        t = t.next
    print('->'.join(ls))


if __name__ == '__main__':
    headC = create_list([1, 8, 4, 5])
    print_list(headC)
    headA = create_list([4])
    headB = create_list([5, 6])
    headA.next = headC
    headB.next = headC
    solution = Solution()
    ans = solution.getIntersectionNode(headA, headB)
    print(ans.val)
