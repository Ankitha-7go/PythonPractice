def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0
expression = "(A+B)*C+D/E"
stack=[]
output =""
for ch in expression:
    if ch.isalnum():
        output +=ch
    elif ch == '(':
        stack.append(ch)
    elif ch ==')':
        while stack and stack[-1] != '(':
            output += stack.pop()
        stack.pop()
    else:
        while stack and precedence(ch) <= precedence(stack[-1]):
            output += stack.pop()
        stack.append(ch)
while stack:
    output += stack.pop()
print("Postfix Expression:",output)
