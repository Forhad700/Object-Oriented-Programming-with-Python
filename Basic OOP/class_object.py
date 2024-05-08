class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

c = Car("Mitsubishi", "Pajero", 2015)
print("Car info..............")
print(c.make, c.model, c.year)