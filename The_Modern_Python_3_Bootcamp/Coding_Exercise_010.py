# I've written some code at the top of the file for you. Please don't touch
# it, if you'd like the tests to work :) All the code does is randomly set
# the food variable to eitehr 'apple', 'grape', 'bacon', 'steak', 'worm',
# or 'dirt'. Don't worry about how it works for now, we'll learn more shortly.

from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])

# When you run the prewritten code, food will be randomly assigned. Your
# task is to write code that will classify what food is.

# If food is set to either 'apple' or 'grape', your could should print 'fruit'.
# If food is set to eitehr 'bacon' or 'steak', your code should print 'meat'.
# If food is set to either 'dirt' or 'worm', your code should print 'yuck.'
print(f"The food is...{food}")
if food == "apple" or food == "grape":
    print("fruit")
elif food == "bacon" or food == "steak":
    print("meat")
elif food == "dirt" or food == "worm":
    print("yuck")