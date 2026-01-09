# MRO (Method Resolution Order) → C → A → B → object

class A:
    def dis(self):
        print("Inside A class")

class B:
    def dis(self):
        print("Inside B class")

class C(A,B):
    pass


c = C()
c.dis()





# MRO (Method Resolution Order) → C → B → A → object

class A:
    def dis(self):
        print("Inside A class")

class B:
    def dis(self):
        print("Inside B class")

class C(B,A):
    pass


c = C()
c.dis()





# overrides dis() method from both A and B

class A:
    def dis(self):
        print("Inside A class")

class B:
    def dis(self):
        print("Inside B class")

class C(A,B):
    def dis(self):
        print("Inside C class")


c = C()
c.dis()