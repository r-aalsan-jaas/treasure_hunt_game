print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island.")
print("Your Mission is to Find the Treasure.")

print("You're at a cross road. Where do you want to go?")
input_1 = input("Type 'left' or 'right'").lower()
if input_1 == 'left' :
    print("You've come to a lake. There is an island in the middle of the lake.")
    input_2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()
    if input_2 == 'wait':
        print("You arrived at the island unharmed. There is a house with 3 doors.")
        input_3 = input("Red, Blue or Yellow. Which colour do you choose?").lower()
        if input_3 == 'red':
            print("Burned by FIRE")
            print("GAME OVER")
        elif input_3 == 'blue':
            print("Eaten by SHARK")
            print("GAME OVER")
        elif input_3 == 'yellow':
            print("You Win!")
        else:
            print("GAME OVER.")
    else:
        print("Attacked by Trout.")
        print("GAME OVER")
else:
    print("Fall into a Hole.")
    print("GAME OVER.")
