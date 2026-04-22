str1=input("Enter the first string:")
str2=input("Enter the second string:")
if len(str1) != len(str2):
    print("Not Anagram")
else:
    count=0
    for ch in str1:
        if ch in str2:
            count+=1
    if count == len(str1):
        print("Anagram")
    else:
        print("Not Anagram")