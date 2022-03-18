# Prompts user to guess a number between 1 and 10
# Let's the user know if it is too high, too low, or correct
# If too high/low, user can continue to guess until correct
# prompts the user to play again or finish

from random import randint

answer = randint(1,10)
guess = None

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > answer:
        print("Too high!")
    elif guess < answer:
        print("Too low!")
    else:
        play_again = input(f"{guess} was correct! Play again (y/n)? ")
        if play_again == "y":
            answer = randint(1,10)
        else:
            print("Thanks for playing!")
            break