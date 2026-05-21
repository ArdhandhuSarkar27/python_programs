nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
x = 36
i = 0
found = False  # 1. Start by assuming we haven't found it

while i < len(nums):
    if nums[i] == x:
        print("Number found at index", i)
        found = True  # 2. Flip the switch to True when found
    else:
        print("Finding please wait.....")
    
    i += 1

# 3. After the loop finishes entirely, check our tracker
if not found:
    print("Reached the end of the tuple but did not find the element:", x)