import random

print("Press Enter to roll dice, To quit rolling enter 'n'")

while True:
    roll_dice = input("Do you want to roll dice?")
    if roll_dice == 'n':
        quit()
        
    num_on_dice = random.randint(1,6)
    print(num_on_dice)