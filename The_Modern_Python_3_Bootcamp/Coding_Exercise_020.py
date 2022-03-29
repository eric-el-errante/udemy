# Given a list ["Ellie", "Tim", "Matt"], create a variable
# called answer, which is a new list containing the first
# letter of each name in the list. I would use a list
# comprehension, though you could also loop over manually

names = ["Ellie", "Tim", "Matt"]
answer = [name[0] for name in names]
print(answer)

# Given a list [1,2,3,4,5,6], create a new variable called
# answer2, which is a new list of all the even values
# another good candidate for list comprehension

numbers = [1,2,3,4,5,6]
answer2 = [num for num in numbers if num % 2 == 0]
print(answer2)