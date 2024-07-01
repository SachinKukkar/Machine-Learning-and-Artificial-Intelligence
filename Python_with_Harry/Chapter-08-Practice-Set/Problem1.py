# Function to find out greatest among three numbers 

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))


def greatest(a,b,c):
    if(a>b and a>c):
        print("The greatest number is :" , a)
    elif(b>a and b>c):
         print("The greatest number is :" , b)
    else:
         print("The greatest number is :" , c)
         
         
         
greatest(a,b,c)              
            