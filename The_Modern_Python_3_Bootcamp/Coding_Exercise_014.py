# Use a while loop to generate a random number between 1 and 10, until
# you get the number 5. Every time the loop runs, increment the variable i.

from random import randint

number = 0
i = 0

while number != 5:
    number = randint(1,10)
    print(number)
    i += 1
print(f"It took {i} tries to randomly pick a 5.")