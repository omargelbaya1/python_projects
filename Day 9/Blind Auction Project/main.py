# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
bids_dict={}
no_more_bids=True
while no_more_bids==True:
    user_name= input("What is your name")
    user_bid=input("what is your bid")
    user_around=input("is someone around u")
    if user_around =="no":
        no_more_bids=False
    print("\n" *1000)
    bids_dict[user_name]=user_bid

biggest_value=0
for i in bids_dict:
    value_of_bid=bids_dict[i]
    new_value=int(value_of_bid)
    if new_value>biggest_value:
        biggest_value=new_value

print(biggest_value)
