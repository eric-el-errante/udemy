# Program repeats user input back to them until they ask it to stop

response = input("Hey what's up?! ")
while response != "stop!":
    print(response)
    response = input()
print("Ok, fine I will stop hahah.")