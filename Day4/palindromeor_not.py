arr=[1,2,3,4,2,1]
is_palindrome = True
left=0
right=len(arr)-1
while left<right:
    if arr[left] != arr[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1    
if is_palindrome:
    print("Array is palindrome")
else:
    print("Array is not palindrome")

