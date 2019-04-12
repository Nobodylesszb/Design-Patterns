from burger import cheeseBurger,spicyChickenBurger
from snack import chickenWings,chips
from Beverage import coke,milk

# buider
class orderBuilder():
    bBurger=""
    bSnack=""
    bBeverage=""
    def addBurger(self,xBurger):
        self.bBurger=xBurger
    def addSnack(self,xSnack):
        self.bSnack=xSnack
    def addBeverage(self,xBeverage):
        self.bBeverage=xBeverage
    def build(self):
        return ordercls(self)

# 订单信息
class ordercls():
    burger = ''
    snack = ''
    beverage = ''
    def __init__(self,orderBuilder):
        self.burger=orderBuilder.bBurger
        self.snack=orderBuilder.bSnack
        self.beverage=orderBuilder.bBeverage
    def show(self):
        print ("Burger:%s"%self.burger.getName())
        print ("Snack:%s"%self.snack.getName())
        print ("Beverage:%s"%self.beverage.getName())

if __name__ == "__main__":
    order_builder=orderBuilder()
    order_builder.addBurger(spicyChickenBurger())
    order_builder.addSnack(chips())
    order_builder.addBeverage(milk())
    order_1=order_builder.build()
    order_1.show()

"""
output:
Burger:spicy chicken burger
Snack:chips
Beverage:milk
"""
    