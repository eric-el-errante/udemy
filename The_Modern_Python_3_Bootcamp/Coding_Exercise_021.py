# Given lists [1,2,3,4] and [3,4,5,6], create a variable called answer
# which is a new list that is the intersection of the two
# your output should be [3,4]. Hint, use the in operator to test
# whether an element is in a list. for example, 5 in [1,5,2] is true
# 3 in [1,5,2] is false

nums1 = [1,2,3,4]
nums2 = [3,4,5,6]
answer = [number for number in nums1 if number in nums2]
print(answer)

# Given a list of words ["Elie", "Tim", "Matt"] create a variable
# called answer2, which is a new list with each word reversed
# and in lower case (use a slice to do the reversal). your output
# should be ['eile', 'mit', 'ttam']

names = ["Elie", "Tim", "Matt"]
answer2 = [name[::-1].lower() for name in names]
print(answer2)