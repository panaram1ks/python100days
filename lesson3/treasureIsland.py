print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

chose1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right"\n').lower()

if chose1 == "left":
    chose2 = input('You\'ve come to a lake.'
                   'There is an island in the middle of the lake.'
                   'Type "wait" to wait a boat or type "swim" to reach the island.\n').lower()
    if chose2 == "wait":
        chose3 = input(
            "You arrive at the island unharmed."
            "There is house with 3 doors."
            "One red, one yellow and one blue."
            "Which colour do you choose?\n").lower()
        if chose3 == "red":
            print("It's a room full of fire. Game Over!")
        elif chose3 == "yellow":
            print("You found the treasure. You Win!")
        elif chose3 == "blue":
            print("You enter a room of beasts. Game Over!")
        else:
            print("You chose a door that doesn't exist. Game Over!")
    else:
        print("You got attacked by an angry trout. Game Over!")
else:
    print("You fell in to a hole. Game Over!")
