# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock

print("...rock...")
print("...paper...")
print("...scissors...")

player_1 = input("(enter Player 1's choice): ")
player_2 = input("(enter Player 2's choice): ")

print("SHOOT!")

if player_1 == "rock":
    if player_2 == "scissors":
        print(f"Player 1 wins! {player_1} smashes {player_2}!")
    elif player_2 == "paper":
        print(f"Player 2 wins! {player_2} covers {player_1}!")

if player_1 == "paper":
    if player_2 == "scissors":
        print(f"Player 2 wins! {player_2} cuts {player_1}!")
    elif player_2 == "rock":
        print(f"Player 1 wins! {player_1} covers {player_2}!")

if player_1 == "scissors":
    if player_2 == "rock":
        print(f"Player 2 wins! {player_2} smashes {player_1}!")
    elif player_2 == "paper":
        print(f"Player 1 wins! {player_1} cuts {player_2}!")

if player_1 == player_2:
    print("Tie!")