print("Welcome to treasure Island")
print("Your mission is to find the treasure")

direction = input(
    'You are at a cross road. Where do you want to go? Type "left" or "right" \n')

if direction == 'left':
    action = input(
        'You came to a lake. Their is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross \n')
    if action == 'wait':
        door = input(
            "You arrive at the island unharmed. their is a house with 3 doors. One red, one yellow and one blue. Which one do you choose? \n")
        if door == "blue":
            print("You enter a room of beasts 🐻‍❄️🐻‍❄️🐻‍❄️🐻‍❄️ game over")
        elif door == "red":
            print("You enter a room of fire 🔥🔥🔥🔥🔥🔥 burn")
        else:
            print("Hurray You found the treasure")
    else:
        print("You got attacked by a hungry tout. Game over")
else:
    print("Game over")
