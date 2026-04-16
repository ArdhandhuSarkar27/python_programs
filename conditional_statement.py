#Program 1

light = "green"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("Go")
elif(light =="yellow"):
    print("Look")
else:
    print("end of code")

#Program 2

marks = int(input("Enter Student Marks:\n"))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
print("Grade:",grade)