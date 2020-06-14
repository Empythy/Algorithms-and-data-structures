class MinStack:
    """
    定义栈的数据结构，
    请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
    调用 min、push 及 pop 的时间复杂度都是 O(1)。
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data_stack = []
        self.min_stack = []


    def push(self, x: int) -> None:
        self.data_stack.append(x)

        if self.min_stack or x < self.min_stack[-1]:
            # 如果栈为空 或者 x 小于最小值
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.min_stack.pop()
        return self.data_stack.pop()


    def top(self) -> int:
        return self.data_stack[-1]


    def min(self) -> int:
        return self.min_stack[-1]

list

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()