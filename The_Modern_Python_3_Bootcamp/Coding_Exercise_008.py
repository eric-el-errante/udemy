# At the top of the file is some starter code that randomly picks a number
# between 1 and 10, and saves it to a variable called choice. Don't touch
# those lines! (please)
from random import randint
choice = randint(1,10)

# Your job is to write a simply conditional to check if choice is 7.
# If choice is 7, print out "lucky". Otherwise, print out "unlucky".

print(f"You rolled a...{choice}")
if choice == 7:
    print("Lucky! You rolled 7!")
else:
    print("Unlucky! You didn't roll 7.")