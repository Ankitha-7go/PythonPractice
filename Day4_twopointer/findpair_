arr = [7, 2, 15, 5, 11]
target = 18
arr.sort()
left = 0
right = len(arr) - 1
while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
        print("Pair found:", arr[left], arr[right])
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1