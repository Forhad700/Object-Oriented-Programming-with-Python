class Parent:
    def pDisplay(self):
        print("Parent Class")
class Child1(Parent):
    def c1Display(self):
        print("Child1 Class")
class Child2(Parent):
    def c2Display(self):
        print("Child2 Class")

c1 = Child1()
c1.c1Display()
c1.pDisplay()

c2 = Child2()
c2.c2Display()
c2.pDisplay()