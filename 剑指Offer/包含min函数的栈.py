class Solution:
    def __init__(self):
        self.minStack = []
        self.stack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if len(self.minStack) == 0:
            self.minStack.append(node)
        if node < self.minStack[-1]:
            self.minStack.append(node)
        else:
            self.minStack.append(self.minStack[-1])
    def pop(self):
        # write code here
        if len(self.stack) == 0:
            return None
        self.minStack.pop()
        return self.stack.pop()
    def top(self):
        # write code here
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
    def min(self):
        # write code here
        if len(self.minStack) == 0:
            return None
        return self.minStack[-1]
