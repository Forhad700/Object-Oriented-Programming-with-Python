class Student:
    id = ""
    gpa = ""

    def setValue(self, x, y):
        self.id = x
        self.gpa = y

    def dis(self):
        print(f'ID: {self.id}, GPA: {self.gpa}')


obj1 = Student()
obj1.setValue(101, 3.50)
obj1.dis()


obj2 = Student()
obj2.setValue(102, 3.90)
obj2.dis()







# class Student:
#     id = ""
#     gpa = ""

#     def dis(self):
#         print(f'ID: {self.id}, GPA: {self.gpa}')


# obj1 = Student()
# obj1.id = 101
# obj1.gpa = 3.50
# obj1.dis()


# obj2 = Student()
# obj2.id = 102
# obj2.gpa = 3.90
# obj2.dis()