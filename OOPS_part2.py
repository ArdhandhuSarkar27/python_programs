class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Kishori Ju")
print(s1.name)
del s1.name #makes an error regarding the print(s1.name) also with an attribute error saying 'Student'object has no attribute 'name'
print(s1.name)