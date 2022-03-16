from random import randint

computer = randint(0,2)

if computer == 0:
    comp = "rock"
elif computer == 1:
    comp = "paper"
else:
    comp = "scissors"

print("...rock...")
print("...paper...")
print("....scissors...")

p1 = input("Player...enter your choice!")
print(f"Computer plays...{comp}!")

if p1 == comp:
    print("Tie!")
elif p1 == "rock":
    if comp == "paper": print("computer wins")
    else: print("player 1 wins")
elif p1 == "paper":
    if comp == "rock": print("player wins!")
    else: print("computer wins!")
elif p1 == "scissors":
    if comp == "rock": print("computer wins!")
    else: print("player wins!")

