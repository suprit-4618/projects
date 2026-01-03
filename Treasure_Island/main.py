print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''
)

print("Welcome to the treasure island \nYour mission is to find the treasure")
print("You are at a cross road. Where do you want to go?")
print('     Type "left" or "right"       ')
choice = input("--------> ")
if choice == "right":
    print("You had to choose this huh")
    print("Game Over")
elif choice == "left":
    print(
        'You reached a lake, do you want to wait for boat or swim \n"Type "wait" or "swim" '
    )
    user_input = input("---------> ")
    if user_input == "swim":
        print("Just wait for the boat dumbass, dont be an Hole")
        print("Game Over")
    elif user_input == "wait":
        print(
            "You reached an island, there are three doors in front of you \nChoose one door to clear the Game !"
        )
        print('"RED","BLUE","GREEN"')
        user_choice = input("-------> ")
        if user_choice == "red":
            print("cha")
            print("Game Over")
        elif user_choice == "blue":
            print("Dont tell anyone")
            print("YOU WIN 😍 !")
        else:
            print("BYE bye")
            print("Game Over")
