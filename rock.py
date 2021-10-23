import random

user_choice = int(input("Choose 0 for Rock, 1 for Paper or 2 for Scissors: \n"))

# computer chooses between  0 and 2
computer_choice = random.randint(0, 2)
print(f"Computer choice is: {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("user wins")
elif user_choice > 2:
    print("You typed an invalid number!")
elif computer_choice == user_choice:
    print("a draw")
elif computer_choice < user_choice:
    print("You win")
else:
    print("You lose, try again!")
