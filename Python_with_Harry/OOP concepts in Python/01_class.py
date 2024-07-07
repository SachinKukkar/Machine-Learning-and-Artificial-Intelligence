class Employee:
    
    language = "Python" # This is a class attribute 
    salary = 1200000

sachin = Employee()  # This is object creation 
sachin.name = "Sachin"  # This is an instance(object) attribute
print(sachin.salary,sachin.language)

rohan = Employee()
rohan.name = "Rohan RORO"
print(rohan.name,rohan.salary,rohan.language)

# Here , name is an "object attribute" and language & salary are "class attributes" as they directly belong to the class 



