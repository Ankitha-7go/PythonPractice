arr=[78,67,76,68,38]
largest=float('-inf')
second_largest = float('-inf')
for i in range(len(arr)):
    if arr[i] > largest:
        second_largest=largest
        largest=arr[i]
    elif arr[i]>second_largest and arr[i] != largest:
        second_largest=arr[i]
print("Second largest element is:",second_largest)