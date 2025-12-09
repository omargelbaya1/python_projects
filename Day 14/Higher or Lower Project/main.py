import random
import game_data
import art


total_number_of_people=(len(game_data.data))

def random_celeb_no(list):
    total_number_of_people = (len(list))
    return random.randint(0,total_number_of_people-1)

def random_celeb(list):
    print(list[random_celeb_no(list)]['name'])
    return list[random_celeb_no(list)]['follower_count']

def compare_celeb(celeb_one,celeb_two,user_input,count):
    if user_input== 1 and (celeb_one > celeb_two):
        print("You win")
        count += 1
        print(count)
        return count
    elif user_input == 2 and (celeb_two > celeb_one):
        print("You win")
        count += 1
        print(count)
        return count
    else:
        print("You lose")
        winning = False
        main_game()

def main_game():
    print(art.logo)
    print("Welcome to higher or lower")
    count=0
    winning = True
    while winning:
        random_celeb_1=random_celeb(game_data.data)
        random_celeb_2=random_celeb(game_data.data)
        user_choice = int(input("Which celebrity has a higher follower 1 or 2"))
        compare_celeb(random_celeb_1,random_celeb_2,user_choice,count)

main_game()

