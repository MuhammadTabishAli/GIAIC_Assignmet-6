class Product:
    def __init__(self, price):
        self._price = price 
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = new_price
    
    @price.deleter
    def price(self):
        del self._price

# Test
p = Product(100)
print(p.price)
p.price = 200
print(p.price)
del p.price