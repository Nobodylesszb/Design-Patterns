"""
有一个手机仓储管理系统，使用者有三方：销售、仓库管理员、采购。需求是：
销售一旦达成订单，销售人员会通过系统的销售子系统部分通知仓储子系统，
仓储子系统会将可出仓手机数量减少，同时通知采购管理子系统当前销售订单；
仓储子系统的库存到达阈值以下，会通知销售子系统和采购子系统，
并督促采购子系统采购；采购完成后，采购人员会把采购信息填入采购子系统，采购子系统会通知销售子系统采购完成，并通知仓库子系统增加库存。
从需求描述来看，每个子系统都和其它子系统有所交流，在设计系统时，
如果直接在一个子系统中集成对另两个子系统的操作，一是耦合太大，二是不易扩展。
为解决这类问题，我们需要引入一个新的角色-中介者-来将“网状结构”精简为“星形结构”。（
为充分说明设计模式，某些系统细节暂时不考虑，例如：仓库满了怎么办该怎么设计。类似业务性的内容暂时不考虑）
首先构造三个子系统，即三个类（在中介者模式中，这些类叫做同事些）：
"""

class Colleague:
    mediator = None
    def __init__(self,mediator):
        self.mediator = mediator
    
class purchaseColleague(Colleague):
    def buyStuff(self,num):
        print('PURCHASE:Bought %s"%num')
    
    def getNotice(self,content):
        print ("PURCHASE:Get Notice--%s"%content)

class warehouseColleague(Colleague):
    total=0
    threshold=100
    def setThreshold(self,threshold):
        self.threshold=threshold
    def isEnough(self):
        if self.total<self.threshold:
            print ("WAREHOUSE:Warning...Stock is low... ")
            self.mediator.execute("warning",self.total)
            return False
        else:
            return True
    def inc(self,num):
        self.total+=num
        print ("WAREHOUSE:Increase %s"%num)
        self.mediator.execute("increase",num)
        self.isEnough()
    def dec(self,num):
        if num>self.total:
            print ("WAREHOUSE:Error...Stock is not enough")
        else:
            self.total-=num
            print ("WAREHOUSE:Decrease %s"%num)
            self.mediator.execute("decrease",num)
        self.isEnough()
class salesColleague(Colleague):
    def sellStuff(self,num):
        print ("SALES:Sell %s"%num)
        self.mediator.execute("sell",num)
    def getNotice(self, content):
        print ("SALES:Get Notice--%s" % content)

"""
当各个类在初始时都会指定一个中介者，而各个类在有变动时，也会通知中介者，由中介者协调各个类的操作。
"""

class abstractMediator():
    purchase=""
    sales=""
    warehouse=""
    def setPurchase(self,purchase):
        self.purchase=purchase
    def setWarehouse(self,warehouse):
        self.warehouse=warehouse
    def setSales(self,sales):
        self.sales=sales
    def execute(self,content,num):
        pass
class stockMediator(abstractMediator):
    def execute(self,content,num):
        print ("MEDIATOR:Get Info--%s"%content)
        if  content=="buy":
            self.warehouse.inc(num)
            self.sales.getNotice("Bought %s"%num)
        elif content=="increase":
            self.sales.getNotice("Inc %s"%num)
            self.purchase.getNotice("Inc %s"%num)
        elif content=="decrease":
            self.sales.getNotice("Dec %s"%num)
            self.purchase.getNotice("Dec %s"%num)
        elif content=="warning":
            self.sales.getNotice("Stock is low.%s Left."%num)
            self.purchase.getNotice("Stock is low. Please Buy More!!! %s Left"%num)
        elif content=="sell":
            self.warehouse.dec(num)
            self.purchase.getNotice("Sold %s"%num)
        else:
            pass

if  __name__=="__main__":
    mobile_mediator=stockMediator()#先配置
    mobile_purchase=purchaseColleague(mobile_mediator)
    mobile_warehouse=warehouseColleague(mobile_mediator)
    mobile_sales=salesColleague(mobile_mediator)
    mobile_mediator.setPurchase(mobile_purchase)
    mobile_mediator.setWarehouse(mobile_warehouse)
    mobile_mediator.setSales(mobile_sales)

    mobile_warehouse.setThreshold(200)
    mobile_purchase.buyStuff(300)
    mobile_sales.sellStuff(120)

    
"""
output:
PURCHASE:Bought %s"%num
SALES:Sell 120
MEDIATOR:Get Info--sell
WAREHOUSE:Error...Stock is not enough
WAREHOUSE:Warning...Stock is low... 
MEDIATOR:Get Info--warning
SALES:Get Notice--Stock is low.0 Left.
PURCHASE:Get Notice--Stock is low. Please Buy More!!! 0 Left
PURCHASE:Get Notice--Sold 120
"""
