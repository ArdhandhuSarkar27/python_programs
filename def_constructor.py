class Student:
    def __init__(self,fullname):
        self.name=fullname
        print("Adding new student in the Database")
s1 = Student("Karan")
print(s1.name)