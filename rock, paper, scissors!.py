import random

items = ["rock", "paper", "scissors"]


def get_user_choice():
    # Your code here to get the user's choice (rock, paper, or scissors)
    x = input("Pick your choice!\n")
    if x in items:
        return x
    else:
        print("Wrong input!")
        get_user_choice()


def get_computer_choice():
    # Your code here to generate the computer's choice (rock, paper, or scissors)
    r = random.randint(0, 2)
    return items[r]


def determine_winner(u, c):
    # Your code here to determine the winner of the game
    if u == c:
        return None
    if (u == items[0] and c == items[1])\
            or (u == items[1] and c == items[2])\
            or (u == items[2] and c == items[0]):
        w = "computer"
    else:
        w = "user"
    return w


# Main game loop
while True:
    print("Welcome to Rock-Paper-Scissors!")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "user":
        print("Congratulations! You win!")
    elif winner == "computer":
        print("Oops! You lost. Try again.")
    else:
        print("It's a tie!")

    play_again = input("Do you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        break

print("Thanks for playing!")
