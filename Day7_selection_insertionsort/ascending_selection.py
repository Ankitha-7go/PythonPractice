arr=[97,33,88,12,47,90,28]
n=len(arr)
for i in range(n):
    min=i
    for j in range(i+1,n):
        if arr[j]<arr[min]:
            min=j
    arr[i],arr[min]=arr[min],arr[i]
print("Sorted array:",arr)
