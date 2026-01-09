class Student:
    id = ""
    gpa = ""

obj1 = Student()

print(isinstance(obj1, Student))

obj1.id = 101
obj1.gpa = 3.50

print(f'ID: {obj1.id}, GPA: {obj1.gpa}')

obj2 = Student()

obj2.id = 102
obj2.gpa = 3.90

print(f'ID: {obj2.id}, GPA: {obj2.gpa}')