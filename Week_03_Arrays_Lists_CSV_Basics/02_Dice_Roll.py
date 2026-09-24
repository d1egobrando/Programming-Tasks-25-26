import random

rolling = int(input("How many times do you want to roll?"))
num_available = [0, 0, 0, 0, 0, 0]
every_roll = []

for i in range(rolling):
    dice = random.randint(1, 6)
    print(dice)

    every_roll.append(dice)
    num_available[dice] += 1

print("Total Amount of sides", num_available)
