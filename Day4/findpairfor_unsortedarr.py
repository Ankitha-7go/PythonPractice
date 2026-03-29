arr=[8,4,2,6,3,1]
arr.sort()
target=8
left=0
right=len(arr)-1
while left<right:
    current_sum = arr[left]+arr[right]
    if current_sum == target:
        print("pair found:",arr[left],arr[right])
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1

    