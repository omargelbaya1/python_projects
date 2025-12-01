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

types_of_hands =[rock,paper,scissors]
computer_hand= random.randint(0,2)
computer_choice=types_of_hands[computer_hand]

print("0 for rock, 1 for paper, 2 for scissors")
choice_of_hand=int(input())
print(computer_choice)
if choice_of_hand==0 and computer_hand==0:
    print("draw")
    print(rock)
elif choice_of_hand==0 and computer_hand==1:
    print("lose")
    print(rock)
elif choice_of_hand==0 and computer_hand==2:
    print("win")
    print(rock)

