arr=[78,38,67,76,68]
largest=arr[0]
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
        break
print("Largest Element is:",largest)