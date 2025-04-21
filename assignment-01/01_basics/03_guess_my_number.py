import random

def main():
    computer_number = random.randint(0,99)
    guess = int(input("Enter a guess: "))
    while guess != computer_number:
        if guess < computer_number:
            print("your guess is too low!")
        else:
            print("your guess is too high")

        guess = int(input("Enter a new guess: "))

    print("Congrats! The number was: " + str(computer_number))
        
        

if __name__ == '__main__':
    main()