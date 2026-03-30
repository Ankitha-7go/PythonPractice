arr=[77,64,98,25,66]
target=25
A={}
for i in range(len(arr)):
    A[arr[i]]=i
if target in A:
    print("Element found at position:",A[target]+1)
else:
    print("Element not found")