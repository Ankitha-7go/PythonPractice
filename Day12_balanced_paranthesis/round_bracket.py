stack=[]
s=input("Enter bracket:")
balanced=True
for ch in s:
    if ch == "(":
        stack.append(ch)
    elif ch == ")":
        if len(stack)==0:
            balanced=False
            break
        stack.pop()
if len(stack)==0:
    print("Balanced")
else:
    print("Not balanced")
        