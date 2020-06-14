class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_stack = []
        self.t_stack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.data_stack:
            self.t_stack.append(self.data_stack.pop())
        self.t_stack.append(x)
        while self.t_stack:
            self.data_stack.append(self.t_stack.pop())


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.data_stack.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.data_stack[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.data_stack) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()