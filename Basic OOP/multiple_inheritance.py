class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

class Student:
    def __init__(self, stu_id, grade):
        self.stu_id = stu_id
        self.grade = grade

class PersonInfo(Person, Employee, Student):
    def __init__(self, name, age, emp_id, salary, stu_id, grade):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        Student.__init__(self, stu_id, grade)


person_info = PersonInfo('Miller', 27, 'MD701', 70000, 'STM099', 'A+')
print("Personal Information...............")
print("Name: ", person_info.name)
print("Age: ", person_info.age)
print("Employee ID: ", person_info.emp_id)
print("Employee Salary: ", person_info.salary)
print("Student ID: ", person_info.stu_id)
print("Student Grade: ", person_info.grade)