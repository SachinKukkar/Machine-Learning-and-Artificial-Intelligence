class Employee:
    company = "ITC"
    name = "Default"
    def show(self):

        print(f"The name of the employee is {self.name} and the company of the employee is {self.company}")
class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages , your language is : {self.language}")


class Programmer(Employee,Coder):
    company="ITC Infotech"
  
    def showLanguage(self):
        print(f"The name of the Programmer's company is {self.company} and he is goot at {self.language} language")    




a = Employee()
b = Programmer()

b.show()
b.showLanguage()
b.printLanguage()