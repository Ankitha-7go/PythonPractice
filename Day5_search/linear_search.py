arr=[6,8,4,9,2,8,1,5]
target=9
found=False
for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index:",i)
        found=True
        break
else:
    print("Element not found")

