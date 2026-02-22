print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction=input("You are at a crossroad and there are two paths. Choose one of them\n"
      'Type "left" or "right"\n').lower()
if direction=="left":
    lake = input("You've come to a lake. There is an island in the middle of the lake\n"
          'Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()
    if lake=="wait":
        door=input("You have arrived at the island unharmed. There is a house with 3 doors with rooms behind it.\n"
                   "One Red, one Yellow, one Blue. Which one do you choose ?\n").lower()
        if door=="red":
            print("You got engulfed by the fire in the room. GAME OVER!!")
        elif door=="blue":
            print("You walked straight into the lion's den. GAME OVER!!")
        elif door=="yellow":
            print("CONGRATULATIONS!!! You found the treasure.")
        else:
            print("A tsunami took you away before you could choose. GAME OVER!!")
    else:
        print("A crocodile had you for lunch. GAME OVER!!.")
else:
    print("While walking a bear attacked you. GAME OVER!")


