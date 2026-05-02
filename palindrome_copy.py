#Without user Input

list1 = [1,2,1]
list2 = [1,2,3]
copy_list1 = list1.copy()
copy_list1.reverse()
if copy_list1 == list1:
    print("The given list is: Palindrome")
else:
    print("The given list is: Not Palindrome")

#With user input

nums = input("Enter numbers separated by comma:\n")
lis1 = list(map(int, nums.split(",")))
copy_lis1 = list1.copy()
copy_lis1.reverse()
if copy_lis1 == lis1:
    print("The given list you provided is: A Palindrome number")
else:
    print("The given list which you provided is: Not a Palindrome number")
