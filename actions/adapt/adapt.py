from staff import BCpnStaff,ACpnStaff

class CpnStaffAdapter:
    b_cpn=""
    def __init__(self,id):
        self.b_cpn=BCpnStaff(id)
    def getName(self):
        return self.b_cpn.get_name()
    def getPhone(self):
        return self.b_cpn.get_telephone()
    def setName(self,name):
        self.b_cpn.set_name(name)
    def setPhone(self,phone):
        self.b_cpn.set_telephone(phone)

if __name__=="__main__":
    acpn_staff=ACpnStaff("123")
    acpn_staff.setName("X-A")
    acpn_staff.setPhone("10012345678")
    print ("A Staff Name:%s"%acpn_staff.getName())
    print ("A Staff Phone:%s"%acpn_staff.getPhone())
    bcpn_staff=CpnStaffAdapter("456")
    bcpn_staff.setName("Y-B")
    bcpn_staff.setPhone("99987654321")
    print ("B Staff Name:%s"%bcpn_staff.getName())
    print ("B Staff Phone:%s"%bcpn_staff.getPhone())

"""
A protocol setPhone method...id:123
A protocol getName method...id:123
A Staff Name:X-A
A protocol getPhone method...id:123
A Staff Phone:10012345678
B protocol set_name method...id:456
B protocol get_name method...id:456
B protocol get_name method...id:456
B Staff Name:Y-B
B protocol get_telephone method...id:456
B Staff Phone:99987654321
"""