# Instance attributes take priority over class attributes during assignment and retrieval

class Employee:
    
    language = "Python" # This is a class attribute 
    salary = 1200000

sachin = Employee()  # This is object creation 
sachin.name = "Sachin"  # This is an instance(object) attribute
sachin.language = "Javascript"
print(sachin.name,sachin.salary,sachin.language)


