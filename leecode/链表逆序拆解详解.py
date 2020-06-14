class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(pHead):
    if pHead is None:
        print("None")
        return
    pTmp = pHead
    while(pTmp):
        print(pTmp.val)
        pTmp = pTmp.next

def newList():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    return node1

def reverseList(pHead):
    new_head = None
    pTmp = pHead
    # for i in range(5):
    while pTmp:
        next = pTmp.next
        pTmp.next = new_head
        new_head = pTmp
        pTmp = next

    return new_head




if __name__ == '__main__':
    linkList = newList()
    print_list(linkList)
    new_head = reverseList(linkList)
    print_list(new_head)






