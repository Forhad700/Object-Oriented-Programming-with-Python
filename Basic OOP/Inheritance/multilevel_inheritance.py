class A:
    def dis1(self):
        print("Inside A class")

class B(A):
    def dis2(self):
        print("Inside B class")

class C(B):
    def dis3(self):
        print("Inside C class")


c = C()
c.dis2()
c.dis3()