vowels = ['a','e','i','o','u']
text = input("Input: ")
print("Output: ",end="")
for char in text:
    if char.lower() in vowels:
        char.replace(' ','')
    else:
        print(char,end="")
print()