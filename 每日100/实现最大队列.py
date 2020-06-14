import queue
from collections import deque
class MaxQueue:
    def __init__(self):
        self.deque = deque()
        self.queue = queue.Queue()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans

if __name__ == "__main__":
    """
    ["MaxQueue","max_value",
    "pop_front","pop_front",
    "push_back","push_back",
    "push_back","pop_front",
    "push_back","pop_front"]
    
[[],[],[],[],[94],[16],[89],[],[22],[]]"""
    s = MaxQueue()
    # print(s.max_value())
    # print(s.pop_front())
    # print(s.pop_front())
    s.push_back(94)
    s.push_back(16)
    s.push_back(89)
    s.pop_front()
    s.push_back(22)
