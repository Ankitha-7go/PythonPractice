arr=[3,6,9,12,15,18]
target = 18
left=0
right=len(arr)-1
found = False
while left <= right:
    mid=(left+right)//2
    if arr[mid] == target:
        print("Element found at index:",mid)
        found=True
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1       
if not found:
    print("Element not found")