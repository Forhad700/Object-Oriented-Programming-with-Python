class Bike:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __eq__(self, x):
        return self.brand == x.brand and self.color == x.color


b1 = Bike("MTT 420RR", "Black")
b2 = Bike("MTT 420RR", "Black")

print(b1==b2)