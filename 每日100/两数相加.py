# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        is_add = False
        tmp_l1 = l1
        tmp_l2 = l2
        ret = ListNode(None)
        last_ret = ret
        while tmp_l1 or tmp_l2:
            if tmp_l1:
                a = tmp_l1.val
            else:
                a = 0
            if tmp_l2:
                b = tmp_l2.val
            else:
                b = 0
            if is_add:  # 是否进位
                is_add = False
                add_sum = a + b + 1
            else:
                add_sum = a + b
            if add_sum >= 10:
                is_add = True
                add_sum -= 10
            new_node = ListNode(add_sum)
            last_ret.next = new_node
            last_ret = new_node
            tmp_l1 = tmp_l1.next
            tmp_l2 = tmp_l2.next

        if is_add:
            new_node = ListNode(1)
            last_ret.next = new_node

        return ret.next