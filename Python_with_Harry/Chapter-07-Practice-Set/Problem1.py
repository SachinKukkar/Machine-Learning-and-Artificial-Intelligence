# Python program to print the table of a number 

n = int(input("Enter a number : "))
print("The table of the number is : ")


for i in range (1,11):
    # print(n,"*",i,"=",n*i) # Ye bhi sahi hai 

    print(f"{n} X {i} = {n*i}") # But prefer this one please