import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def changing_ace(list):
    if sum(list)>21:
        list[:] = [1 if x==11 else x for x in list]




def taking_a_card(list):
    another_user_card = random.choice(cards)
    list.append(another_user_card)
    return list



blackjack_forever=True
while blackjack_forever:
    print(art.logo)
    initial_user_hand=random.sample(cards, 2)
    initial_dealer_hand=random.sample(cards,2)
    print(f"Welcome to blackjack, your hand is {initial_user_hand} and the dealer's first card is {initial_dealer_hand[0]}")
    going_bust=True
    while going_bust:
        until_seventeen = True
        print(f"Your Current total {sum(initial_user_hand)}")
        ask_user_for_card = input("Do you wish to take a card?: press 'y' for yes and 'n' for no")
        if ask_user_for_card=="y":
            taking_a_card(initial_user_hand)
            changing_ace(initial_user_hand)
            print(initial_user_hand)
            if sum(initial_user_hand)>21:
                print("You've gone bust buddy! Unlucky!")
                going_bust=False
                until_seventeen=False
            while until_seventeen:
                if sum(initial_dealer_hand) > 17:
                    until_seventeen = False
                else:
                    taking_a_card(initial_dealer_hand)
                    if sum(initial_dealer_hand) > 21:
                        print("Dealer's gone bust, i think you win")
                        going_bust=False
                    else:
                        until_seventeen=False
        else:
            if sum(initial_user_hand)>sum(initial_dealer_hand) and sum(initial_user_hand)<=21:
                print("You win")
                print("\n" * 5)
                going_bust = False
            elif sum(initial_user_hand)==sum(initial_dealer_hand):
                print("It's a draw, play again")
                print("\n" * 5)
                going_bust = False
            else:
                print("You lose")
                print("\n" * 5)
                going_bust = False
    print(f"These were the last games ending hands, you:{initial_user_hand}, total:{sum(initial_user_hand)}, dealer:{initial_dealer_hand}, total:{sum(initial_dealer_hand)}")
    print("\n" * 10)