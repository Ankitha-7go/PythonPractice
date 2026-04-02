def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[]
    middle=[]
    right=[]
    for x in arr:
        if x>pivot:
            left.append(x)
        elif x<pivot:
            right.append(x)
        else:
            middle.append(x)
    return quick_sort(left) + middle + quick_sort(right)
arr=[66,34,78,91,26,48]
sorted_array=quick_sort(arr)
print("Sorted array:",sorted_array)