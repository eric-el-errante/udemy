# for 4 and 13, print 'x is unlucky'
# for even numbers, print 'x is even'
# for odd number,s print 'x is odd'

for num in range(1,21):
    if num == 4 or num == 13:
        state = "unlucky"
    elif num % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num} is {state}.")