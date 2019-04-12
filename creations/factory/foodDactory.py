#foodFactory为抽象的工厂类，而burgerFactory，snackFactory，beverageFactory为具体的工厂类。
from burger import cheeseBurger,spicyChickenBurger
from snack import chickenWings,chips
from Beverage import coke,milk

class foodFactory():
    type = ''
    def createFood(self,foodClass):
        print(self.type, 'factory produce a instance.')
        foodIns=foodClass()
        return foodIns

class burgerFactory(foodFactory):
    def __init__(self):
        self.type="BURGER"
class snackFactory(foodFactory):
    def __init__(self):
        self.type="SNACK"
class beverageFactory(foodFactory):
    def __init__(self):
        self.type="BEVERAGE"

if __name__ == "__main__":
    burger_factory = beverageFactory()
    snack_factorry=snackFactory()
    beverage_factory=beverageFactory()
    cheese_burger=burger_factory.createFood(cheeseBurger)
    print (cheese_burger.getName(),cheese_burger.getPrice())
    chicken_wings=snack_factorry.createFood(chickenWings)
    print (chicken_wings.getName(),chicken_wings.getPrice())
    coke_drink=beverage_factory.createFood(coke)
    print (coke_drink.getName(),coke_drink.getPrice())

"""
output:
BURGER factory produce a instance.
cheese burger 10.0
SNACK factory produce a instance.
chicken wings 12.0
BEVERAGE factory produce a instance.
coke 4.0
"""
