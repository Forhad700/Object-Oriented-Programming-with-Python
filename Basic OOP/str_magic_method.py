class Bike:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __str__(self):
        return (f'Brand: {self.brand}, Color: {self.color}')


b1 = Bike("Honda CBR150R", "Red")
print(b1)

b2 = Bike("MTT 420RR", "Black")
print(b2)