from typing import List

from collections import deque
class MonotonicQueue():
    def __init__(self):
        # 递减的队列
        self.data = deque()

    def push(self, n):
        # 每次push的时候，把队列中，小于当前元素的值删除
        while len(self.data) and self.data[-1] < n:
            self.data.pop()

        self.data.append(n)

    def max(self):
        return self.data[0]

    def pop(self, n):
        if len(self.data) and self.data[0] == n:
            self.data.popleft()

class Max_queue():
    def __init__(self):

        self.q = []

    def push(self, val):
        while self.q and self.q[len(self.q)-1] < val:
            self.q.pop()
        self.q.append(val)
    #弹出首元素时，只需要判断是否为最大的元素
    def pop(self, val):
        if self.q and self.q[0] == val:
            self.q.pop(0)

    def max(self):
        return self.q[0] if self.q else -1


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mq = MonotonicQueue()
        res = []
        for i in range(len(nums)):
            #前k个元素
            if i < k-1:
                mq.push(nums[i])
            #向后滑动
            else:
                mq.push(nums[i])
                res.append(mq.max())
                #删除滑出滑窗的元素，[1,2,3,4]:[1,2,3]->[2,3,4]，mq中要删除1
                mq.pop(nums[i-(k-1)])
        return res
