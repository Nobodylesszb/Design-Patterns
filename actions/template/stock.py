"""
投资股票是种常见的理财方式，我国股民越来越多，
实时查询股票的需求也越来越大。今天，
我们通过一个简单的股票查询客户端来认识一种简单的设计模式：模板模式。
根据股票代码来查询股价分为如下几个步骤：
登录、设置股票代码、查询、展示。构造如下的虚拟股票查询器：
"""

class StockQueryDevice():
    stock_code="0"
    stock_price=0.0
    def login(self,usr,pwd):
        pass
    def setCode(self,code):
        self.stock_code=code
    def queryPrice(self):
        pass
    def showPrice(self):
        pass

"""
现在查询机构很多，
我们可以根据不同的查询机构和查询方式，
来通过继承的方式实现其对应的股票查询器类。
例如，WebA和WebB的查询器类可以构造如下
"""

class WebAStockQueryDevice(StockQueryDevice):
    def login(self,usr,pwd):
        if usr=="myStockA" and pwd=="myPwdA":
            print ("Web A:Login OK... user:%s pwd:%s"%(usr,pwd))
            return True
        else:
            print ("Web A:Login ERROR... user:%s pwd:%s"%(usr,pwd))
            return False
    def queryPrice(self):
        print ("Web A Querying...code:%s "%self.stock_code)
        self.stock_price=20.00
    def showPrice(self):
        print ("Web A Stock Price...code:%s price:%s"%(self.stock_code,self.stock_price))


class WebBStockQueryDevice(StockQueryDevice):
    def login(self,usr,pwd):
        if usr=="myStockB" and pwd=="myPwdB":
            print ("Web B:Login OK... user:%s pwd:%s"%(usr,pwd))
            return True
        else:
            print ("Web B:Login ERROR... user:%s pwd:%s"%(usr,pwd))
            return False
    def queryPrice(self):
        print ("Web B Querying...code:%s "%self.stock_code)
        self.stock_price=30.00
    def showPrice(self):
        print ("Web B Stock Price...code:%s price:%s"%(self.stock_code,self.stock_price))

if  __name__=="__main__":
    web_a_query_dev=WebAStockQueryDevice()
    web_a_query_dev.login("myStockA","myPwdA")
    web_a_query_dev.setCode("12345")
    web_a_query_dev.queryPrice()
    web_a_query_dev.showPrice()

"""
output:
Web A:Login OK... user:myStockA pwd:myPwdA
Web A Querying...code:12345 
Web A Stock Price...code:12345 price:20.0
"""