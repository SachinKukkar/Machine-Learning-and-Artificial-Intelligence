# Self refers to the instance of the class.
# It is automatically passed with a function call from an object

class Employee:
    
    language = "Python" 
    salary = 1200000

    def __init__(self,name,salary,language):   # dunder method kehte hai isko , they are called as soon as an object is created 
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object !")

    def getInfo(self):
        print(f"The language is : {self.language}. The salary is {self.salary}")

    @staticmethod     # This is a function which does not take self_parameter 
    def greet():
        print("Good Morning !")
  

sachin = Employee("Sachin" , 12000000 , "JavaScript") 
# sachin.name = "Sachin Kukkar"
print(sachin.name , sachin.salary , sachin.language)

