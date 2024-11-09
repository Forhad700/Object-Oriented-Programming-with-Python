'''Write a Python program to create a class that represents a shape. 
Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.'''

import math
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, base, height, a, b, c):
        self.base = base
        self.height = height
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.a + self.b + self.c    

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2
    
    def perimeter(self):
        return 4 * self.a


c = Circle(7)
print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

t = Triangle(5,4,4,3,5)
print("Triangle Area:", t.area())
print("Triangle Perimeter:", t.perimeter())

r = Rectangle(5,7)
print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())

s = Square(5)
print("Square Area:", s.area())
print("Square Perimeter:", s.perimeter())