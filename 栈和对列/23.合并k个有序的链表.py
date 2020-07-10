from queue import PriorityQueue
from typing import List
import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    用堆
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                # 注意可以使用元组 但是第二项需要存储 node的index
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        head = tmp_head = ListNode(0)
        while heap:
            val, idx = heapq.heappop(heap)  # 每次pop最小的node值以及 链表index
            new_node = ListNode(val) # 根据值new 一个node
            tmp_head.next = new_node # 更改 临时节点的指向
            tmp_head = tmp_head.next # 更新临时节点
            if lists[idx] and lists[idx].next: #如果 node 还有下一个节点
                heapq.heappush(heap, (lists[idx].next.val, idx))
                lists[idx] = lists[idx].next
        return head.next


class Solution1(object):
    """
       优先级队列
    """
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next

def create_list(str_data):
    l = str_data.split('->')
    l = [ListNode(int(item)) for item in l]
    for i in range(len(l)-1):
        l[i].next = l[i+1]
    return l[0]

def print_list(head):
    p = head
    while p:
        print(p.val, end="->")
        p = p.next
    print("None")


if __name__ == "__main__":
    l1 = "1->3"
    l2 = "1"
    l3 = "2"
    data = []
    for item in [l1,l2,l3]:
        tmp_head = create_list(item)
        print_list(tmp_head)
        data.append(tmp_head)

    print("=" * 30)
    for item in data:
        print_list(item)
    print("=" * 30)
    s = Solution()
    ans = s.mergeKLists(data)
    print_list(ans)