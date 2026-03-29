arr=[86,79,64,52,48,31,20]
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left += 1
    right -= 1
print("Reversed array:",arr)