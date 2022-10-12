
import numbers
import random

player_wins = 0
computer_wins = 0
options = ["red", "blue", "purple"]

# red: 0, blue:1, purple:2
number_generator = random.randint(0, 2)

computer_choice = options[number_generator]

while True:
    input_value = input("Please type Red/Blue/Purple or Q to quit the game: ").lower()
    if input_value == "q":
        quit()

    if input_value not in options:
        print("Sorry, this is not part of the options list, please choose red, blue or purple")
        continue    

    print("Computer has chosen", computer_choice + ".")

    if input_value == "red" and computer_choice == "blue":
        print("You win!")
        player_wins +=1
  

    elif input_value == "purple" and computer_choice == "red":
        print("You win!")
        player_wins +=1
 
    
    elif input_value == "blue" and computer_choice == "purple":
        print("You win!")
        player_wins +=1
        continue
    else:
        print("Computer won, try again next time.")
        