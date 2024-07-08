try:
    a = int(input("Enter a number please : "))
    print(a)

# except ValueError as v:
#     print("Hello !!!")
#     print(v)

except Exception as e:
    print(e)    

else:
    print("I am here , inside the else block")     # this code runs when the "try" block runs successfully 