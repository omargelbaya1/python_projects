import random

numbers=[]
for i in range(0,101):
    numbers.append(i)

computer_choice=random.choice(numbers)
attempts=0


still_wanting_to_play=True

while still_wanting_to_play:
    computer_choice = random.choice(numbers)
    attempts = 0

    print("Welcome to the guessing numbers game brother")
    user_choice_difficulty = input("Easy or Hard bro?:")

    if user_choice_difficulty == "Easy":
        attempts = 10
    if user_choice_difficulty == "Hard":
        attempts = 5

    while attempts>0:
        user_choice_number=int(input("pick a number between 1 and 100:"))
        if user_choice_number==computer_choice:
            print("You Guessed Correctly")
            attempts=0
        elif user_choice_number>computer_choice:
            attempts-=1
            print(f"you have {attempts} attempts left")
            print("too high")
        elif user_choice_number<computer_choice:
            attempts-=1
            print(f"you have {attempts} attempts left")
            print("too low")

    print("\n"*20)

