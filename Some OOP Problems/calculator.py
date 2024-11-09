'''Write a Python program to create a calculator class. Include methods for basic arithmetic operations.'''

class Calculator:
    def addition(self, a, b):
        return a+b
    
    def subtraction(self, a, b):
        return a-b
    
    def multiplication(self, a, b):
        return a*b
    
    def division(self, a, b):
        return a/b
    
c = Calculator()
r = c.addition(3,2)
print("3 + 2: ", r)

r = c.subtraction(5,3)
print("5 - 3: ", r)

r = c.multiplication(5,4)
print("5 * 4: ", r)

r = c.division(10,2)
print("10 / 2: ", r)



# # another method
# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def addition(self):
#         return self.a + self.b
    
#     def subtraction(self):
#         return self.a - self.b
    
#     def multiplication(self):
#         return self.a * self.b
    
#     def division(self):
#         return self.a / self.b
    
# c = Calculator(10,5)
# print("Addition: ", c.addition())
# print("Subtraction: ", c.subtraction())
# print("Multiplication: ", c.multiplication())
# print("Division: ", c.division())