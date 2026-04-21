string=input("Enter a sentence:")
count=1
for ch in string:
    if ch == " ":
        count += 1
print("Number of words:",count)
