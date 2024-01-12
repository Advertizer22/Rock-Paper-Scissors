import random

def play_round(user_input, computer_input, user_points, computer_points):
    print(f"Your input is {user_input}")
    print(f"Computer input is {computer_input}")

    if user_input == computer_input:
        print("It's a tie!")
    elif (user_input == "rock" and computer_input == "scissors") or \
         (user_input == "paper" and computer_input == "rock") or \
         (user_input == "scissors" and computer_input == "paper"):
        print("You win!")
        user_points += 1
    else:
        print("Computer wins!")
        computer_points += 1

    return user_points, computer_points

def main():
    user_points = 0
    computer_points = 0

    while True:
        options = ["rock", "paper", "scissors"]
        user_input = input("Choose rock, paper, scissors, or exit: ").lower()

        if user_input == "exit":
            print("Game ended")
            print(f"You won a total score of {user_points} and the computer's total score is {computer_points}")
            break

        if user_input in options:
            computer_input = random.choice(options)
            user_points, computer_points = play_round(user_input, computer_input, user_points, computer_points)
        else:
            print("Invalid Input. Please choose rock, paper, scissors, or exit.")

if __name__ == "__main__":
    main()
