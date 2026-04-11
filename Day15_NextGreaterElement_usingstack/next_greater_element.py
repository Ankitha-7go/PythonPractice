arr=[9,6,7,13,11,5]
stack=[]
for num in arr:
    while stack and num> stack[-1]:
        stack.append(num)
while stack:
    print(stack.pop(),"-->",-1)







