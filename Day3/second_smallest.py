arr=[67,57,86,69,77]
smallest = arr[0]
second_smallest = float('inf')
for i in range(len(arr)):
    if arr[i] < smallest:
        second_smallest = smallest
        smallest = arr[i]
    elif arr[i] < second_smallest and arr[i] != smallest:
        second_smallest = arr[i]
print("Second Smallest element is:", second_smallest)