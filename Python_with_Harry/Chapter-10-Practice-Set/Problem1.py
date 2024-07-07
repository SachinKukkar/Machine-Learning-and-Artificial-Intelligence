class Programmer :
    company = "Microsoft"
    def __init__(self,name,salary,pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode


p=Programmer("Sachin",12000000,335512)
print(p.name,p.salary,p.pincode,p.company)

rohan=Programmer("Rohan",1100000,302017)
print(rohan.name,rohan.salary,rohan.pincode,rohan.company)

