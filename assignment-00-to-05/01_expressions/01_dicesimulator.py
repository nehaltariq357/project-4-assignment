import random
num_sides = 6
def roll_dice():
    '''
    simulates rolling two dice and prints their total
    '''
    die1 = random.randint(1,num_sides) # die value randomly come from 1 to 6
    die2 = random.randint(1,num_sides) # die value randomly come from 1 to 6
    total = die1 + die2
    print(f"Dice 1 = {die1}\nDice 2 = {die2}\nThe total of two dice = {total}")

def main():
    die1 = 10 # this die1 works in main()
    print(f"die1 in main() starts as: {die1}")

    #rolling dice 3 times
    roll_dice()
    roll_dice()
    roll_dice()

    print(f"die1 in main() is: {die1}")



if __name__ == '__main__':
    main()