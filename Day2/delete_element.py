arr=[4,9,5,10,6]
target=9
for i in range(len(arr)):
    if arr[i] == target:
        del arr[i]
        break
print(arr)
