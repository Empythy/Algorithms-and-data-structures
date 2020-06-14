class MaxPQ():
    def __init__(self, cap=10):
        # 索引0不用
        self.cap = cap+1
        self.pq = [None] * self.cap
        self.N = 0

    def max(self):
        return self.pq[1]

    def insert(self, e):
        self.N += 1
        self.pq[self.N] = e
        self.swim(self.N)

    def del_max(self):
        e = self.pq[1]
        self.exch(1, self.N)
        self.pq[self.N] = None
        self.N -= 1
        self.sink(1)
        return e
    # 上浮第k个元素 维护最大堆性质
    def swim(self, k):
        while(k>1 and self.less(self.parent(k), k)):
            # 如果第k个元素比上层元素大
            self.exch(self.parent(k), k)
            k = self.parent(k)
    # 下沉第k个元素 维护最大堆性质
    def sink(self, k):
        # 如果沉到堆底 就不沉不下去
        while self.left(k) <= self.N:
            older = self.left(k)
            if self.right(k) <= self.cap and self.less(older, self.right(k)):
                older = self.right(k)
            if self.less(older, k): break
            self.exch(k, older)
            k = older
    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    # pq[i] 是否比pq[j] 小
    def less(self, i, j):
        return self.pq[i] < self.pq[j]

    def parent(self, root):
        return root // 2

    def left(self, root):
        return root * 2

    def right(self, root):
        return root * 2 + 1

