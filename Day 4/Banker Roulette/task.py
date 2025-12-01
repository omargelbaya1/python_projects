import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


number_of_people= len(friends)
print(number_of_people)

y=random.randint(0,number_of_people-1)
print(y)

who_pays=friends[y]
print(who_pays)

print(random.choice(friends))