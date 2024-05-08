class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)
    
    def __str__(self):
        return f'point({self.x}, {self.y})'
    
point1 = Point(1,2)
point2 = Point(3,4)

result = point1 + point2

print(f'Point1: {point1}')
print(f'Point2: {point2}')
print(f'point1 + point2: {result}')