class Vehicle:
    def drive(self):
        return "Vehicle driven by V"
    
class Car(Vehicle):
    def drive(self):
        return "Car driven by C"
    
class Bicycle(Vehicle):
    def drive(self):
        return "Bicycle driven by B"
    

c = Car()
b = Bicycle()

print(c.drive())
print(b.drive())