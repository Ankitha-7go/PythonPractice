stack=[]
def push():
    element=int(input("Enter an element:"))
    stack.append(element)
    print("Pushed",stack)
def pop():
    if len(stack)==0:
        print("Stack is empty")
    else:
        print("Popped:",stack.pop())
def peek():
    if len(stack)==0:
        print("Stack is empty")
    else:
        print("Top element:",stack[-1])
push()
push()
push()
peek()
pop()
