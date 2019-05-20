from Medicin import *

class Visitor:
    name=""
    def setName(self,name):
        self.name=name
    def visit(self,medicine):
        pass
class Charger(Visitor):
    def visit(self,medicine):
        print ("CHARGE: %s lists the Medicine %s. Price:%s " % (self.name,medicine.getName(),medicine.getPrice()))
class Pharmacy(Visitor):
    def visit(self,medicine):
        print( "PHARMACY:%s offers the Medicine %s. Price:%s" % (self.name,medicine.getName(),medicine.getPrice()))


class ObjectStructure:
    pass
class Prescription(ObjectStructure):
    medicines=[]
    def addMedicine(self,medicine):
        self.medicines.append(medicine)
    def rmvMedicine(self,medicine):
        self.medicines.append(medicine)
    def visit(self,visitor):
        for medc in self.medicines:
            medc.accept(visitor)


if __name__=="__main__":
    yinqiao_pill=Coldrex("Yinqiao Pill",2.0)
    penicillin=Antibiotic("Penicillin",3.0)
    doctor_prsrp=Prescription()
    doctor_prsrp.addMedicine(yinqiao_pill)
    doctor_prsrp.addMedicine(penicillin)
charger=Charger()
charger.setName("Doctor Strange")
pharmacy=Pharmacy()
pharmacy.setName("Doctor Wei")
doctor_prsrp.visit(charger)
doctor_prsrp.visit(pharmacy)

"""
output:
CHARGE: Doctor Strange lists the Medicine Yinqiao Pill. Price:2.0 
CHARGE: Doctor Strange lists the Medicine Penicillin. Price:3.0 
PHARMACY:Doctor Wei offers the Medicine Yinqiao Pill. Price:2.0
PHARMACY:Doctor Wei offers the Medicine Penicillin. Price:3.0
"""