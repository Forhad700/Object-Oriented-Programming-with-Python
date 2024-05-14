class MethOverload:
    def display(self, a=None, b=None):
        print(a, b)

m = MethOverload()
m.display()
m.display(10)
m.display(10,20)