'''Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.'''

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    

n = int(input("input radius of circle: "))
c = Circle(n)

area = c.calculate_area()
perimeter = c.calculate_perimeter()

print("Area of circle: ", area)
print("Perimeter of circle: ", perimeter)