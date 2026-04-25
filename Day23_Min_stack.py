class MinStack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
    def push(self,x):
        self.stack.append(x)
        if len(self.min_stack)== 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.min_stack[-1]
s=MinStack()
s.push(3)
s.push(5)
s.push(1)
s.push(2)
print("Minimum:",s.getMin())
s.pop()
print("Minimum:",s.getMin())