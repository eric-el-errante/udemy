# Print some cool emoji art using a for loop, and a while loop

for x in range(1,11):
    print("\U0001f600" * x)

count = 1
while count <= 10:
    print("\U0001f640" * count)
    count += 1

space = " "
num = 8
for x in range(1,11,2):
    print(space * num + "\U0001f640" * x)
    num -= 2
num = 2
for x in range(7,0,-2):
    print(space * num + "\U0001f640" * x)
    num += 2