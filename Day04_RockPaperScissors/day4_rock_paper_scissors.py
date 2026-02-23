import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options=[rock,paper,scissors]
player_choice=int(input("What do you choose ? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
if player_choice < 0 or player_choice > 2:
    print("You chose a wrong number")
else:
    print("You chose:")
    print(options[player_choice])

    print("Computer chose:")
    comp_choice=random.randint(0,2)
    print(options[comp_choice])


    if player_choice==comp_choice:
        print("It's a Draw !")
    elif (player_choice==0 and comp_choice==2) or \
        (player_choice==1 and comp_choice==0) or \
        (player_choice==2 and comp_choice==1) :
        print("Congrats! You Win")
    else:
        print("You Lose!")






