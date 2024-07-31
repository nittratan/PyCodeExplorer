# guess the number game 

# guess number between 1 to 10

import random

n = random.randint(1, 10)
guess = 0
while n != guess:
    guess = int(input("Enter an integer from 1 to 10: "))
    if guess < n:
        print("guess is low")
    elif guess > n:
        print("guess is high")
    else:
        print("you guessed it!")
        