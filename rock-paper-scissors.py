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

import random

should_continue = True
while should_continue:
    choice=int(input("\nEnter a number, 0 for rock, 1 for paper and 2 for scissors:"))
    choice_list=[rock, paper, scissors]
    print("\n\nYour choice is: \n", choice_list[choice])

    computer = random.randint(0, 2)
    print("Computer chose:\n", choice_list[computer])

    if (choice==0 and computer==2) or (choice==1 and computer==0) or (choice==2 and computer==1):
        print("You won!\n\n")
    elif choice==computer:
        print("It's a draw!\n\n")
    else:
        print("You lose!\n\n")
    
    response=input("Start again?, type yes or no: \n").lower()
    if response=="no":
        should_continue=False
        print("Game Ended.")


















