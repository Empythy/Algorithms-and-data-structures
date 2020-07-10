# class Node():
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.pre = None
#         self.next = None
#
#
# class DoubleList():
#     # 在链表头部添加节点 x， 时间 O(1)
#     def add_first(self, node):
#         pass
#
#     # 由于是双链表且给的是⽬标 Node 节点， 时间 O(1)
#     def remove(self, node):
#         pass
#
#     def remove_last(self):
#         pass
#
#     def size(self):
#         pass
#
#
# class LRUCache():
#     def __init__(self, cap=2):
#         self.dict = dict()
#         self.cache = DoubleList()
#         self.cap = cap
#
#     def get(self, key):
#         if not key in self.dict:
#             return -1
#         else:
#             val = self.dict.get(key).val
#             # 将数据(key, val)提到开头
#             self.put(key, val)
#             return val
#
#     def put(self, key, val):
#         node = Node(key, val)
#         if (key in self.dict):
#             # 删除旧的数据
#             self.cache.remove(self.dict.get(key))
#             # 将新节点插入开头
#             self.cache.add_first(node)
#             self.dict[key] = node
#         else:
#             # cache 已满
#             if (self.cap == self.cache.size()):
#                 # 删除链表最后一个数据
#                 last = self.cache.remove_last()
#                 # 删除map中映射到该数据的键
#                 self.dict.pop(last.key)
#             # 将新节点插入到开头
#             self.cache.add_first(node)
#             # map中新建key 对新节点的映射
#             self.dict[key] = node
import collections


class LRUCache1(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)  # 将key移动到最末尾
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value

        if len(self) > self.capacity:  # 判断是否超过容量
            self.popitem(last=False)  # 删除头部


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点 需要返回key
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head  # 左指针指向头节点
        node.next = self.head.next # 右指针指向 头结点的下一个节点
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
