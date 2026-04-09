string=input("Enter string:")
stack=list(string)
reversed_string=" "
while stack:
    reversed_string += stack.pop()
print("Reversed String:",reversed_string)