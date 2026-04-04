text="Arirang Arirang Arariyo"
target="Arar"
for i in range(len(text)-len(target)+1):
    if text[i:i+len(target)] == target:
        print("Substring found at index",i)