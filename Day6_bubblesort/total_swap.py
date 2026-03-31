arr=[62,45,66,98,11,48]
n=len(arr)
swap_count=0
for i in range(n):
    swapped = False
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swap_count+=1
            swapped = True

    if not swapped:
        break
print("Sorted array:",arr)
print("Total swaps:",swap_count)