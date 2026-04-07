stack=[]
stack.append(10)
stack.append(70)
stack.append(40)
print("Stack after push:",stack)
stack.pop()
print("Stack after pop:",stack)
print("Top element :",stack[-1])
if len(stack)==0:
    print("Stack is empty")
else:
    print("Stack is not empty")