class Student:
    college_name = "ABC College" #this is common for all students
    def __init__(self,name,marks):
        self.Student_name = name
        self.Student_marks = marks
        print("Adding New Student Name and Marks....")
s1 = Student("Radheshwari",97)
print(s1.Student_name,s1.Student_marks) #Prints the o/p as Radheshwari
s2 = Student("Madhusudan",95)
print(s2.Student_name,s2.Student_marks) #Prints the o/p as Madhusudan
print("Students are from",Student.college_name)


    