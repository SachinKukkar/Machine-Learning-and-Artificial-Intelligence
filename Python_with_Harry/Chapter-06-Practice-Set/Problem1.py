# Program to find the greatest of four numbers entered by the user 

n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number :  "))
n3 = int(input("Enter the third number :  "))
n4 = int(input("Enter the fourth number :  "))

if(n1>n2 and n1>n3 and  n1>n4):
    print("First number is the greatest : " , n1)

elif(n2>n1 and n2 >n3 and n2>n4):
    print("Second number is the greatest : ", n2)

elif(n3>n1 and n3>n2 and n3>n4):
    print("Third number is the largest : ", n3)
 
else:
    print("Fourth number is the largest : " , n4)            