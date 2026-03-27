arr=[4,8,2,10,6]
target=1
found=False
for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at position:",i)
        found=True
        break
if found == False:
        print("Element not found")