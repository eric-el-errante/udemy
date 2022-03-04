# You will be provided with a random number in a variable called num.
# Use a conditional statement to check if the number is odd. If num is odd,
# print "odd". Otherwise print "even".
# Hint: use modulus % to figure out if the number is odd!

from random import randint
num = randint(1, 1000)

remainder = num%2

print(f"You rolled a...{num}")
if remainder == 1:
    print(f"{num} is odd.")
else:
    print(f"{num} is even.")