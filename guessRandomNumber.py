import random

randNumber=random.randint(0,100)
print(randNumber)
userGuess=None
guess=0
while(userGuess!=randNumber)and (guess<=4):
    userGuess=int(input("Enter your guess: "))
    guess += 1
    if (userGuess==randNumber):
         print("You are right")
    else:
        print("You are wrong")
        

print(f"Number of guesses {guess}")
    