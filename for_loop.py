str = "Radha Vallab Shri Harivasnh"
for char in str:
    if char == 'n':
        print("n found")
        break
    print(char)
else:
    print("Character not Found")

'''Same program taking input from the user'''

name = input("Enter the string: ")
target = input("Enter character to find: ")
idx = 0
for char in name:
    if char == target:
        print("Character found at index:", idx)
        break
    idx += 1
else:
    print("The character was not found")