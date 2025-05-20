import random

user_wins = 0
computer_wins = 0
tie = 0

options = ["rock", "paper", "scissors"]
# "[]" are used for lists. If anything the user inputs is found in the list... You can use it to check multiple things on line of code.

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        # "and" checks if both conditions are satisfied.
        # "or" checks if either of the conditions are true. Not used right now.
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        # "and" checks if both conditions are satisfied.
        # "or" checks if either of the conditions are true. Not used right now.
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        # "and" checks if both conditions are satisfied.
        # "or" checks if either of the conditions are true. Not used right now.
        print("You won!")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "rock":
        # "and" checks if both conditions are satisfied.
        # "or" checks if either of the conditions are true. Not used right now.
        print("Its a tie!")
        tie += 1

    elif user_input == "paper" and computer_pick == "paper":
        # "and" checks if both conditions are satisfied.
        # "or" checks if either of the conditions are true. Not used right now.
        print("Its a tie!")
        tie += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        # "and" checks if both conditions are satisfied.
        # "or" checks if either of the conditions are true. Not used right now.
        print("Its a tie!")
        tie += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "time(s).")
print("The computer won", computer_wins, "time(s).")
print(tie, "tie(s).")
print("Goodbye!")