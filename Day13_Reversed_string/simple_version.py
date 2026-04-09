stack=[]
string=input("Enter string:")
for ch in string:
    stack.append(ch)
reversed_string=" "
while len(stack)>0:
    reversed_string += stack.pop()
print("Reversed string:",reversed_string)
