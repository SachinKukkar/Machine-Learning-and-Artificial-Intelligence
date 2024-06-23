
# If - elif - else ladder in python 

age =  int(input("enter your age : "))

if(age>=18):
    print("You are above the age of consent !")

elif(age<0):
    print("You have entered invalid negative age !")    

elif(age==0):
    print("You have entered age as zero which is not a valid age !")

else:
    print("You are below the age of consent , please bring your parents with you ")        
    
print("End of the program , jao yaha se ab :-) ")    