import random
import os


os.system('cls')
while True:
    print("Press Enter to roll dice" + " To quit rolling enter n" )
    roll_num = random.randint(1,6)
    print(" ---")
    print("| "+str(roll_num)+" |")
    print(" ---")
    roll = input("Do you want to roll dice:")
    if roll == 'n':
        print('Thanks for using Dice Stimulator')
        quit()
        
    os.system('cls')
    