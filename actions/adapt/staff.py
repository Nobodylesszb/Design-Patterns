class ACpnStaff:
    name=""
    id=""
    phone=""
    def __init__(self,id):
        self.id=id
    def getName(self):
        print ("A protocol getName method...id:%s"%self.id)
        return self.name
    def setName(self,name):
        print ("A protocol setName method...id:%s"%self.id)
        self.name=name
    def getPhone(self):
        print ("A protocol getPhone method...id:%s"%self.id)
        return self.phone
    def setPhone(self,phone):
        print ("A protocol setPhone method...id:%s"%self.id)
        self.phone=phone
class BCpnStaff:
    name=""
    id=""
    telephone=""
    def __init__(self,id):
        self.id=id
    def get_name(self):
        print ("B protocol get_name method...id:%s"%self.id)
        return self.name
    def set_name(self,name):
        print ("B protocol set_name method...id:%s"%self.id)
        self.name=name
    def get_telephone(self):
        print ("B protocol get_telephone method...id:%s"%self.id)
        return self.telephone
    def set_telephone(self,telephone):
        print ("B protocol get_name method...id:%s"%self.id)
        self.telephone=telephone