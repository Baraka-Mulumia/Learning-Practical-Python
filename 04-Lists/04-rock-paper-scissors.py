# The world rock paper scissors association
import random

rock = "🪨R🪨OCK🪨"
paper = "📃PA📃PER📃"
scissors = "✂️SCI✂️ORS✂️"

game_images = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)
print(f"You chose {game_images[user_choice]}")
print(f"computer chose {game_images[computer_choice]}")

"""
Rock wins against scissors.

Scissors win against paper.

Paper wins against rock.
"""

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")
