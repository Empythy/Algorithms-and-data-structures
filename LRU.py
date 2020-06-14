class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
class DoubleList():
    # 在链表头部添加节点 x， 时间 O(1)
    def add_first(self, node):
        pass
    # 由于是双链表且给的是⽬标 Node 节点， 时间 O(1)
    def remove(self, node):
        pass

    def remove_last(self):
        pass

    def size(self):
        pass

class LRUCache():
    def __init__(self, cap=2):
        self.dict = dict()
        self.cache = DoubleList()
        self.cap = cap

    def get(self, key):
        if not key in self.dict:
            return -1
        else:
            val = self.dict.get(key).val
            # 将数据(key, val)提到开头
            self.put(key, val)
            return val
    def put(self, key, val):
        node = Node(key, val)
        if (key in self.dict):
            # 删除旧的数据
            self.cache.remove(self.dict.get(key))
            # 将新节点插入开头
            self.cache.add_first(node)
            self.dict[key] = node
        else:
            # cache 已满
            if (self.cap == self.cache.size()):
                # 删除链表最后一个数据
                last = self.cache.remove_last()
                # 删除map中映射到该数据的键
                self.dict.pop(last.key)
            # 将新节点插入到开头
            self.cache.add_first(node)
            # map中新建key 对新节点的映射
            self.dict[key] = node




