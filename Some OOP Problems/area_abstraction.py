from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def calculate_area(self):
        pass

class Triangle(Shape):
    def calculate_area(self):
        area = 0.5 * self.dim1 * self.dim2
        print(area)

class Rectangle(Shape):
    def calculate_area(self):
        area = self.dim1 * self.dim2
        print(area)


t = Triangle(20, 30)
t.calculate_area()

r = Rectangle(20, 30)
r.calculate_area()