class Parent:
    def pDisplay(self):
        print("Parent Class")

class Child(Parent):
    def cDisplay(self):
        print("Child Class")

c = Child()
c.cDisplay()
c.pDisplay()