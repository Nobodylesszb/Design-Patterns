class Burger():
    name = ''
    price = 0.0
    def getPrice(self):
        return self.name

    def setPrice(self,price):
        self.price = price
        
    def getName(self):
        return self.name
    
class cheeseBurger(Burger):
    def __init__(self):
        self.name = 'cheese burger'
        self.price = 10.0

class spicyChickenBurger(Burger):
    def __init__(self):
        self.name="spicy chicken burger"
        self.price=15.0