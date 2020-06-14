from collection import deque
class MyStack(object):
    def __init__(self):
        self.data = deque()
        self.helper = deque()
    
    def push(self, x):
        self.data.append(x)
    
    
    def pop(self):
        while len(self.data) > 1:
            self.helper.append(self.data.popleft())
        
        tmp = self.data.popleft()
        self.helper, self.data = self.data, self.helper
        return tmp
       
    def top(self):
        while len(self.data) > 1:
            self.helper.append(self.data.popleft())
        
        tmp = self.data.popleft()
        
        self.helper.append(tmp)
        self.helper, self.data = self.data, self.helper
        return tmp
    
    def empty(self):
        return not bool(self.data)
        
 ## 使用单队列实现
 
 class MyStack(object):
    def __init__(self):
        self.data = deque()
    
    def push(self, x):
        self.data.append(x)
        q_len = len(self.data)
        while q_len > 1:
            self.data.append(self.data.popleft())
            q_len = q_len - 1
            
        
    
    def pop(self):
        return self.popleft()
        
       
    def top(self):
        return self.data[0]
    
    def empty(self):
        return not bool(self.data)
 
 
