# class Student:
#     id = 123
#     name = "Abc"
#     dept = "CSE"

#     def read(self):
#         print("Reading.....")

# s = Student()
# print("ID: ", s.id)
# print("Name: ", s.name)
# print("Dept: ", s.dept)
# s.read()



class Student:
    id = 123
    name = "Abc"
    dept = "CSE"

    def read(self):
        id = 456
        print("ID: ", id)
        print("Reading.....")

s = Student()
print("ID: ", s.id)
print("Name: ", s.name)
print("Dept: ", s.dept)
s.read()



# # implicit instance of class
# class Student:
#     id = 123
#     name = "Abc"
#     dept = "CSE"

#     def read(self):
#         id = 456
#         print("ID: ", id)
#         print("ID (Instance variable): ", self.id)
#         print("Reading.....")

# s = Student()
# print("ID: ", s.id)
# print("Name: ", s.name)
# print("Dept: ", s.dept)
# s.read()