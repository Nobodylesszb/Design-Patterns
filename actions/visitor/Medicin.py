class Medicine:
    name=""
    price=0.0
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def accept(self,visitor):
        pass
class Antibiotic(Medicine):
    def accept(self,visitor):
        visitor.visit(self)
class Coldrex(Medicine):
    def accept(self,visitor):
        visitor.visit(self)

