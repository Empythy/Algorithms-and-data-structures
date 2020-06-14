    from collections import deque


class MyStack:
    """
    使用队列实现栈的下列操作：
        push(x) -- 元素 x 入栈
        pop() -- 移除栈顶元素
        top() -- 获取栈顶元素
        empty() -- 返回栈是否为空
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_q = deque([])
        self.t_q = deque([])


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.t_q.append(x)
        while self.data_q:
            self.t_q.append(self.data_q.popleft())

        while self.t_q:
            self.data_q.append(self.t_q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.data_q.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.data_q[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        # 判断是否为空 使用len函数
        return len(self.data_q) == 0



# Your MyStack object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.top())
    print(obj.pop())
    param_4 = obj.empty()