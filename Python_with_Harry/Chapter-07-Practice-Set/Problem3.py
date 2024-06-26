# Program to check whether a number is Prime or not

n = int(input("Enter a number : "))

for i in range(2,n):
    if(n%i==0):
        print("The entered number is NOT a prime number.")
        break
    else:
        print("The number is prime number.")