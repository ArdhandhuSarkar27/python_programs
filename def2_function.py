class Student:
    college_name = "ABC college"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def welcome(self):
        print("Welcome Student,",self.name)
    def get_marks(self):
        return self.marks
s1 = Student("Radha",99)
s1.welcome()
print(s1.get_marks())
