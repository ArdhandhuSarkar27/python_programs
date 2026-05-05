student = {
    "name": "Radha",
    "subjects":{
        "phy":97,
        "chem":98,
        "math":95
    }
}
print(student.keys())
print(student.get("name 2"))#there is no string named "name 2" but if we use .get() fun then it exectues the next line without any error which is helpful in real world probelms nut prints "None instead of error"
print("This line is executed after the error line 'name 2'")
print("Hi")
print("Hello")