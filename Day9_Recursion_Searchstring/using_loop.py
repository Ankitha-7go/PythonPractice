text="Arirang Arirang Arariyo"
target="A"
found =  False
for ch in text:
    if ch == target:
        found = True
        break
if found:
    print("Character found")
else:
    print("Character not found")