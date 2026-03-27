arr=[5,9,3,7]
position=1
element=4
arr.append(0)
for i in range(len(arr)-1,position,-1):
    arr[i]=arr[i-1]
arr[position]=element
print(arr)
