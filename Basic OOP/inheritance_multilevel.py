class GrandFather:
    def gfDisplay(self):
        print("GrandFather Class")
class Parent(GrandFather):
    def pDisplay(self):
        print("Parent Class")

class Child(Parent):
    def cDisplay(self):
        print("Child Class")

c = Child()
c.cDisplay()
c.gfDisplay()
c.pDisplay()