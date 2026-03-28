arr=[67,86,57,69,77]
smallest = arr[0]
for i in range(len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]
print("Smallest element is:", smallest)