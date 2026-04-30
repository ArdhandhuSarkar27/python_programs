#Index tuple without user input
tup = (1,2,3,2,4,5,)
print(tup.index(2))

#Index tuple with user input

#Take input as string
nums = input("Enter numbers separated by comma:\n")
#Convert to tuple
tup = tuple(map(int,nums.split(",")))
#Take element to find
x = int(input("Enter number to find:\n"))
print("The number found at index:",tup.index(x))


#Count tuple without user input
print("Tuple without user input")
tupl = (1,2,3,4,2,2)
print(tup.count(2))#counts the number of times 2 occured

#Count tuple with user input

#Take input as string
print("Tuple with user input")
nums = input("Enter numbers separated by comma for counting repeated numbers:\n")
#Convert to tuple
tup = tuple(map(int,nums.split(",")))
#Take element to find
x = int(input("Enter the number to be counted:\n"))
print("The number occured:",tup.count(x),"time(s)")


