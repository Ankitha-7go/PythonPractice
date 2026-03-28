arr=[34,76,88,34,67,90,34]
count=0
target=34
for i in range(len(arr)):
    if arr[i] == target:
        count += 1
print("Frequency of an element:",count)