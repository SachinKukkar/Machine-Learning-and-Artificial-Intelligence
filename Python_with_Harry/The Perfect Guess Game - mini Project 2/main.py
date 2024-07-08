import random
n=random.randint(1,10)

a=-1

guesses = 1 
while(a != n):
    a = int(input("Guess a number : "))
   
    if(a > n):
        print("Please enter a lower number : ")
        guesses+=1            
    else:
        print("Please enter a higher number : ")
        guesses+=1

print(f"You have guessed the correct number {n} in {guesses} attempts !")