class Parent:
    def Transportation(self):
        print("Car")

class Child(Parent):
    def Transportation(self):
        print("Bike")

c = Child()
c.Transportation()