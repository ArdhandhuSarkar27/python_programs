'''WAP to print length of a list(list is the parameter)'''

cities = ["Barsana","Vrindavan","Kedarnath"]
Gods = ["Radha Rani","Krishna","Mahadev"]
def print_len(list):
    print(len(list))
def print_list(list): #for printing our list in the same line
    for item in list:
        print(item,end=" ")
print_list(Gods)
print()

print_len(cities)
print_len(Gods)