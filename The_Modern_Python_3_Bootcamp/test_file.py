cart = []

while True:
    item = input("Add something to the cart? Type q to quit:")
    if item != 'q':
        cart.append(item)
    else:
        break
print(cart)