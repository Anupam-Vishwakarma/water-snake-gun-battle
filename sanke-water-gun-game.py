import random

# Define the rules as a dictionary
rules = {
    1: "water",
    2: "snake",
    3: "gun"
}

# Define the winning conditions as a dictionary
win_conditions = {
    (1, 2): "Computer wins",
    (2, 3): "Computer wins",
    (3, 1): "Computer wins",
    (2, 1): "You won",
    (3, 2): "You won",
    (1, 3): "You won"
}

def get_user_choice():
    while True:
        user_choice = int(input("Enter your choice \n1 for water\n2 for snake\n3 for gun\n"))
        if user_choice in rules:
            return user_choice
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.randint(1, 3)

def play_game(user_choice, computer_choice):
    print(f"You chose {rules[user_choice]}. Computer chose {rules[computer_choice]}.")
    if user_choice == computer_choice:
        print("Draw")
    else:
        print(win_conditions.get((user_choice, computer_choice), "Invalid combination"))

def main():
    user_score = 0
    computer_score = 0
    for i in range(5):
        print(f"\nRound {i+1}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        play_game(user_choice, computer_choice)
        if win_conditions.get((user_choice, computer_choice)) == "You won":
            user_score += 1
        elif win_conditions.get((user_choice, computer_choice)) == "Computer wins":
            computer_score += 1
    print(f"\nFinal score: \nYou  {user_score}\nComputer  {computer_score}")
    print("You won" if user_score > computer_score else "Computer won" if computer_score > user_score else "Draw")
if __name__ == "__main__":
    main()