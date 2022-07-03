#random number guessing 
import random

while True:
    number=int(input("Enter a number between 1 and 9: "))
    randomNumber=random.randint(1,9)
    if number==randomNumber:
        print("Well Guessed!")
        break
    elif number!=randomNumber:
        print("Wrong guess. Try Again!")
        
    
        


    