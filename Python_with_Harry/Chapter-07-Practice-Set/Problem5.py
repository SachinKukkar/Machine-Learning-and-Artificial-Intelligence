# Program to calculate the factorial of a number 

n = int(input("Enter a number : "))

product = 1 

for i in range (1,n+1):
    product=product*i
    
    
print(f"The factorial of of {n} is {product}")    