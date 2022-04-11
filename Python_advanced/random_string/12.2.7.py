import random

n = int(input())

pupils = []
for _ in range(n):
    pupils.append(input())

my_friends = []

for item in pupils:
    while True:
        random_choice = random.choice(pupils)
        friends = []
        for friend in my_friends:
            friends.append(friend[1])
        if item != random_choice and (item, random_choice) not in my_friends and random_choice not in friends:
            my_friends.append((item, random_choice))
            break
for item in my_friends:
    print(f'{item[0]} - {item[1]}')
