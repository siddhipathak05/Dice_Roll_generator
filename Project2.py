import random
MaximumNumber=6
while True:
    print(random.randint(1, MaximumNumber))
    dice_roll = input("Want to roll the dice again? (y/n): ") 
    if dice_roll.lower() == "y":
        continue
    else:
        break
