'''Write a Python program to create a person class. 
Include attributes like name, country and date of birth. Implement a method to determine the person's age.'''

from datetime import date
class Person:
    def __init__(self, name, country, DOB):
        self.name = name
        self.country = country
        self.DOB = DOB

    def calculate_age(self):
        today = date.today()
        age = today.year - self.DOB.year
        if today < date(today.year, self.DOB.month, self.DOB.day):
            age = -1
        return age

p1 = Person('person 1', 'Turkey', date(1985, 5, 20))
p2 = Person('person 2', 'England', date(1990, 7, 10))
p3 = Person('person 3', 'USA', date(2000, 3, 25))

print("Person 1 Info................")
print("Name: ", p1.name)
print("Country: ", p1.country)
print("Date of Birth: ", p1.DOB)
print("Age: ", p1.calculate_age())

print("Person 2 Info................")
print("Name: ", p2.name)
print("Country: ", p2.country)
print("Date of Birth: ", p2.DOB)
print("Age: ", p2.calculate_age())

print("Person 3 Info................")
print("Name: ", p3.name)
print("Country: ", p3.country)
print("Date of Birth: ", p3.DOB)
print("Age: ", p3.calculate_age())