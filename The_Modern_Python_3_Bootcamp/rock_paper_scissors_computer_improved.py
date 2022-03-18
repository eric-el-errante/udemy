from random import randint, random

winning_score = 3

print("Welcome to Rock - Paper - Scissors!")
print(f"First to win {winning_score} games is the winner!")

computer_count = 0
user_count = 0
tie_count = 0

while computer_count < winning_score and user_count < winning_score:

    print(f"User wins: {user_count}")
    print(f"Computer wins: {computer_count}")
    print(f"Ties: {tie_count}")

    random_number = randint(0,2)
    if random_number == 0:
        computer = "rock"
    elif random_number == 1:
        computer = "paper"
    else:
        computer = "scissors"

    user = input("Player, enter your choice!: ")
    print("Computer chooses: ", computer)
    if user == computer:
        print("It's a tie!")
        tie_count += 1
    elif user == "rock":
        if computer == "paper":
            print("Computer wins!")
            computer_count += 1
        else:
            print("Player wins!")
            user_count += 1
    elif user == "paper":
        if computer == "rock":
            print("User wins!")
            user_count += 1
        else:
            print("Computer wins!")
            computer_count += 1
    else:
        if computer == "rock":
            print("Computer wins!")
            computer_count += 1
        else:
            print("Player wins!")
            user_count += 1

if computer_count > user_count:
    print(f"Computer wins by a score of {computer_count} to {user_count}, with {tie_count} ties.")
else:
    print(f"User wins by a score of {user_count} to {computer_count}, with {tie_count} ties.")