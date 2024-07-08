a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

# c = int("Enter third number :")
if(b==0):
    raise ZeroDivisionError("You cannot divide by zero , Moron !")
else:
    print(f"The division of {a} and {b} is {a/b}")