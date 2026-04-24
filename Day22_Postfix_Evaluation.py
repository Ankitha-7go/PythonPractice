stack=[]
expression="241-7*+9-"
for ch in expression:
    if ch.isdigit():
        stack.append(int(ch))
    else:
        b=stack.pop()
        a=stack.pop()
        if ch == '+':
            stack.append(a+b)
        elif ch == '-':
            stack.append(a-b)
        elif ch == '*':
            stack.append(a*b)
        elif ch == '/':
            stack.append(a/b)
print("Result:",stack.pop())