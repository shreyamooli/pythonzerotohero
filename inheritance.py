class company:
    def __init__(self,companyname):
        self.companyname=companyname

    def address(self):
        print("blg")
    def getname(self):
        return self.companyname


class employee(company):
    def __init__(self,name,id,companyname):
        self.name=name
        self.id=id
        super().__init__(companyname)

    def work(self):
        print("employee working")
    def getname(self):
        print(super().getname())
        return self.name

#multilevel inheritance
class wfh(employee):
    def promotion(self):
        print("no wfh this time")

class promotion():
    def promotion(self):
        print("not this time")

#multiple inheritance
class salaryhike(employee,promotion):
    def promotion(self):
        print("no hike this time")
        
emp1=employee("abhi",1234,"abccompany")
print(emp1.name,emp1.id,emp1.companyname)
print(emp1.getname())
