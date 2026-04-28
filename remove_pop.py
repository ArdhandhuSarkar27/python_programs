#remove and pop functions without user input

#Remove

my_list = [2,1,3,1]
my_list.remove(1)
print(my_list)

#Pop

my_list = [2,1,3,1]
my_list.pop(2)
print(my_list)

#remove and pop functions with user input

#Remove

List = list(map(int, input("Enter the numbers for remove Function(comma separated):\n").split(',')))
List.remove(int(input("Enter the number you want to remove:\n")))
print(List)

#Pop

List = list(map(int, input("Enter the numbers for pop Function(comma separated):\n").split(',')))
List.pop(int(input("Enter the number you want to remove:\n")))
print(List)