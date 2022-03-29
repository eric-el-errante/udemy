# Given the string 'amazing', create a variable called answer,
# which is a list containing all the letters from 'amazing'
# but not the vowels. The answer should look like
# ['m', 'z', 'n', 'g']

answer = [val for val in 'amazing' if val not in ('aeiou')]
print(answer)