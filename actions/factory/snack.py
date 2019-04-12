class Snack():
    name = ''
    price = 0.0
    type = 'SNACK'

    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name

        
class chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class chickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0