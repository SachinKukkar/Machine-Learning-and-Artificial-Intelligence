for i in range(100):
    if(i==36):
        break  # Exit the loop just right now man ! 
    print(i)


for i in range(100):
    if(i==36):
        continue  # Exit the loop just for this iteration ! 
    print(i)
    
    
    # Pass statement is a NULL statement in Python 
    # It instructs to do nothing 
    
l = [1,3,5]
for i in l:
    pass  # without pass , the program will throw an error     