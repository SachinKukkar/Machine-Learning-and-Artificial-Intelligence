class Employee:
    company = "ITC"
    def show(self):
        print("The name of the employee is {self.name} and the Salary of the employee is {self.salary}")



# class Programmer:
#     company="ITC"
#     def show(self):
#         print(f"The name of the employee is {self.name} and the Salary of the employee is {self.salary}")
#     def showLanguage(self):
#         print(f"The name of the Programmer is {self.name} and he is goot at {self.language} language")    

class Programmer(Employee):
    company="ITC Infotech"
  
    def showLanguage(self):
        print(f"The name of the Programmer is {self.name} and he is goot at {self.language} language")    




a = Employee()
b = Programmer()

print(a.company,b.company)