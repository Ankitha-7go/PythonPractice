arr=[97,28,88,12,47,90,33]
n=len(arr)
for i in range(n):
    max=i
    for j in range(i+1,n):
        if arr[j]>arr[max]:
            max=j
    arr[i],arr[max]=arr[max],arr[i]
print("Sorted array:",arr)
