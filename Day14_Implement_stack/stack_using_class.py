class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
        print("Pushed:",element)
    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty")
        else:
            print("Removed:",self.stack.pop())
    def peek(self):
            if len(self.stack)==0:
                print("Stack is empty")
            else:
                print("Top element:",self.stack[-1])
    def display(self):
        print("Stack elements:",self.stack)
s = Stack()
s.push(60)
s.push(30)
s.push(35)
s.display()
s.pop()
s.peek()
s.display()
