arr=[9,7,5,4,3,1]
reverse_arr=[]
for i in range(len(arr)-1,-1,-1):
    reverse_arr.append(arr[i])
print("Reversed array=",reverse_arr)