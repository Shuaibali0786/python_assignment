class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Price cannot be negative.")

    
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price



p = Product(1000)

print("Current price:", p.price)

p.price = 1500
print("Updated price:", p.price)


p.price = -500  


del p.price
