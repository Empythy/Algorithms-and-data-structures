from copy import deepcopy
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        new_head = self.copy(head)
        new_head = self.delete(new_head)
        return new_head

    def copy(self, head):
        if head is None:
            return None
        tmp = head
        while tmp:
            new_node = Node(tmp.val, tmp.next)
            tmp.next = new_node
            tmp = tmp.next.next
        tmp = head
        while tmp and tmp.next:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next
        return head
    def delete(self, head):
        if head is None:
            return None
        new_head = head.next
        tmp = new_head
        while tmp and tmp.next:
            tmp.next = tmp.next.next
            tmp = tmp.next

        tmp.next = None
        return new_head

if __name__ == "__main__":
    l = [Node(i) for i in range(1, 6)]
    for i in range(4):
        l[i].next = l[i+1]

    solution = Solution()
    head = solution.copy(l[0])
    new_head = head
    while new_head:

        print(new_head.val)
        new_head = new_head.next

    head = solution.delete(head)
    new_head1 = head
    while new_head1:
        print(new_head1.val)
        new_head1 = new_head1.next

