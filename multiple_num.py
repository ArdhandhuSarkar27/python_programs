num = int(input("Enter the Number:"))
n = int(input("Enter the number you want to check multiple of:"))
if(num % 2 == 0):
    print(num,"is an even Number")
else:
    print(num,"is an odd Number")
if(num % n == 0):
    print(num,"is an multiple of",n)
else:
    print(num,"is a not a multiple of",n)