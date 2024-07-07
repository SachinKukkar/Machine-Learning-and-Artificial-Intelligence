# Self refers to the instance of the class.
# It is automatically passed with a function call from an object

class Employee:
    
    language = "Python" 
    salary = 1200000

    def getInfo(self):
        print(f"The language is : {self.language}. The salary is {self.salary}")

    @staticmethod     # This is a function which does not take self_parameter 
    def greet():
        print("Good Morning !")
  

sachin = Employee() 
sachin.name = "Sachin" 
# print(sachin.salary,sachin.language)
sachin.greet()
sachin.getInfo()
# Employee.getInfo(sachin)


