# Recursive function to calculate the sum of n natural numbers 

n = int(input("Enter the number upto which the sum is to be calculated : "))

def natural_sum(n):
    if(n==1):
        return 1
    return n + natural_sum(n-1)



print(natural_sum(n))