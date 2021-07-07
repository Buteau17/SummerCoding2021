#ASCII art
# This  image is a hint providing by ASCII art
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
user_action=int(input("Enter a choice(0 for rock, 1 for paper,2 for scissors):"))
possible_actions=[rock, paper, scissors]
print(possible_actions[user_action])
computer_action=random.randint(0,2)
print("Computer chose:")
print(possible_actions[computer_action])

if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
elif user_action == 0:
    if computer_action == 2:
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == 1:
    if computer_action == 0:
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == 2:
    if computer_action == 1:
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")     
    
