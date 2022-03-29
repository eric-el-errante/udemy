nums = [1,2,3]

# List Comprehension
nums10 = [x*10 for x in nums]
print(nums)
print(nums10)

# Could also just do a regular for loop
# But clearly much more obtuse
nums = [1,2,3]
ten_times = []

for num in nums:
    ten_time = num * 10
    ten_times.append(ten_time)

print(ten_times)

# Will turn each letter uppercase
# note, name is a string and is made into a list
name = 'eric'
print([char.upper() for char in name])

# Capitalizes first letter in each name
friends = ['ashley', 'matt', 'michael']
print([friend.title() for friend in friends])

[num*10 for num in range(1,6)]

nums = [1,2,3]
print([str(num) + "HELLO" for num in nums])

# Can add conditional logic

numbers = [1,2,3,4,5,6,7,8,9,10]

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

print(evens)
print(odds)

# Number*2 if even otherwise number/2 for odd
print([num*2 if num % 2 == 0 else num/2 for num in numbers])