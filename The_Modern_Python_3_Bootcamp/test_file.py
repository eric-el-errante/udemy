numbers = [1,2,3,4]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])

for num in numbers:
    print(num)

x = 0
while x < len(numbers):
    print(f"Index: {x} is {numbers[x]}")
    x += 1