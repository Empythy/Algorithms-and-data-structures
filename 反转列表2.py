# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre = None # 记录 m-1 位置上的node
        last = None # 记录 n 位置上的node
        tmp = head  # 临时头结点
        ## 寻找 pre 和 last
        for i in range(1, n + 1):
            if i == m - 1:
                pre = tmp
            if i == n:
                last = tmp
            tmp = tmp.next
        # 记录 last后一个节点
        last_next = last.next

        last.next = None
        if pre is None: # 如果head开始反转
            new_list = self.reverse(head)
        else:
            new_list = self.reverse(pre.next)
            pre.next = new_list

        tmp_new_head = new_list
        while tmp_new_head.next != None:
            tmp_new_head = tmp_new_head.next
        tmp_new_head.next = last_next
        if pre is None:
            return new_list
        return head

    def reverse(self, head):
        # print(head.val)
        if head is None or head.next is None:
            return head

        last = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return last

class Solution2():
    def __init__(self):
        self.successor = None  #  后驱节点
    def reverseN(self, head, n):
        # 反转以 head 为起点的 n 个节点， 返回新的头结点
        if n == 1: #  记录第 n + 1 个节点
            self.successor = head.next
            return head
        # 以 head.next 为起点， 需要反转前 n - 1 个节点
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        # 让反转之后的head节点和后⾯的节点连起来
        head.next = self.successor
        return last

    def reverseBetween(self, head, m, n):
        # base case
        if (m == 1):
            return self.reverseN(head, n)
        #前进到反转的起点触发 base case
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

if __name__ == "__main__":
    print("反转链表")
    l = [ListNode(i) for i in range(1, 6)]
    for i in range(4):
        l[i].next = l[i+1]
    tmp = l[0]
    while tmp:
        print(tmp.val)
        tmp = tmp.next

    solution = Solution()
    new = solution.reverseBetween(l[0], 2, 4)
    while new:
        print(new.val)
        new = new.next



