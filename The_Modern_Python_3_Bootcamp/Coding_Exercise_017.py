sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# concatenate the individual indices in sounds using while loop
x = 0
result = ""
while x < len(sounds):
    result += sounds[x]
    x += 1
result = result.upper()
print(result)

# concatenate the individual indices in sounds using for loop
string = ""
for fragment in sounds:
    string += fragment
string = string.upper()
print(string)