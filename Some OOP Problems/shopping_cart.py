'''Write a Python program to create a class representing a shopping cart. 
Include methods for adding and removing items, and calculating the total price.'''

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.prices = {}

    def add_item(self, item, price):
        self.items.append(item)
        self.prices[item] = price

    def remove_item(self, item_name):
        for item in self.items:
            if item == item_name:
                self.items.remove(item)
                del self.prices[item]
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total = total + self.prices[item]
        return total
    
    def display(self):
        print("\nShopping Cart............")
        for item in self.items:
            print(f'{item}  {self.prices[item]}tk')
    
sc = ShoppingCart()
sc.add_item("biscuit", 100)
sc.add_item("sweets", 200)
sc.add_item("cake", 150)

sc.display()

p = sc.calculate_total()
print("Total price: ", end=' ')
print(p)

sc.remove_item('cake')

sc.display()

p = sc.calculate_total()
print("Total price: ", end=' ')
print(p)