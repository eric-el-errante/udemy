# ask for age

# 18-21 wristband
# 21+ can drink , normal entry
# too young, sorry

age = input("What is your age? ")
age = int(age)

if age < 18:
    print("Sorry, you are too young to enter.")
elif age < 21:
    print("You can enter, but must wear a wristband.")
else:
    print("You have normal entry and can drink!")