# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

# Starter Code

import random

def main():
    computer_guess = random.randint(0,99)
    print("I am thinking of a number between 0 and 99...")

    try:
        user_guess = int(input("Enter a guess: "))

        while computer_guess != user_guess:
            if user_guess > computer_guess:
                print("your guess is to high")
            else:
                print("your guess is too low")
            print()# add space 

            user_guess = int(input("Enter a new guess: "))
        print(f"Congrats! The number was {computer_guess}")

    except ValueError:
        print("please enter a valid number 0-99")

if __name__ == '__main__':
    main()