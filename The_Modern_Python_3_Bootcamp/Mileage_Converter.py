# Takes an input of kilometers from the user and converts it to miles

print("Enter the number of kilometers...")
kilometers = input()
kilometers = round(float(kilometers), 1)
miles = round(kilometers/1.60934, 1)
print(f"{kilometers} kilometers is equal to {miles} miles.") # f-strings

# print("{} kilometers is equal to {} miles.".format(kilometers, miles)) # .format method
# print(f"{round(kilometers, 2)} kilometers is equal to {round(miles, 2)} miles.")