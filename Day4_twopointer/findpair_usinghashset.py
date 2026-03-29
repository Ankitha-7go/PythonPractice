arr = [7, 2, 15, 5, 11]
target = 18
seen = set()
for num in arr:    
    complement = target - num    
    if complement in seen:
        print("Pair found:", complement, num)
        break    
    seen.add(num)