class Student:
    id = ""
    gpa = ""

    def __init__(self, x, y):
        self.id = x
        self.gpa = y

    def dis(self):
        print(f'ID: {self.id}, GPA: {self.gpa}')
    

obj1 = Student(101, 3.50)
obj1.dis()

obj2 = Student(102, 3.90)
obj2.dis()