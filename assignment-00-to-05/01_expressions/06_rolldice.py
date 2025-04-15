import random
num_sides:int = 6
def main():
    # Roll die
    die1:int = random.randint(1,num_sides)
    die2:int = random.randint(1,num_sides)
    #get their sum
    total:int = die1 + die2

    # Print out the results

    print("Dice have", num_sides, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)


if __name__ == '__main__':
    main()  