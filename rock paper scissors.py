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
print("Welcome to the game rock paper scissors")
users_choice=int(input("Type 0 for rock, 1 for paper and 2 for scissors"))
if users_choice==0:
    print("You chose:rock",rock)
elif users_choice==1:
    print("You chose:paper",paper)
elif users_choice==2:
    print("You chose:scissors",scissors)
else:
    print("You need to chose from 0,1,2")

import random
computer_choice=random.randint(0,2)
if computer_choice==0:
    print("Computer chose:rock",rock)
elif computer_choice==1:
    print("Computer chose:paper",paper)
else:
    print("Computer chose:scissors",scissors)


if users_choice>=3 or users_choice<0:
    print("You chose an invalid number,you loose!")
elif users_choice==0 and computer_choice==2:
    print("You win!!")
elif computer_choice==0 and users_choice==2:
    print("You loose")
elif computer_choice>users_choice:
    print("You lose")
elif users_choice>computer_choice:
    print("You win")
elif users_choice==computer_choice:
    print("It's a tie")

