stack=[]
string=input("Enter expression:")
balanced=True
for ch in string:
    if ch in "({[":
        stack.append(ch)
    elif ch in ")}]":
        if len(stack)==0:
            balanced=False
            break
        top = stack.pop()
        if(ch==")"and top!="(") or \
        (ch=="}"and top!="{") or \
        (ch=="]"and top!="[") :
            balanced=False
            break
if len(stack)==0 and balanced:
    print("Balanced")
else:
    print("Not Balanced")
