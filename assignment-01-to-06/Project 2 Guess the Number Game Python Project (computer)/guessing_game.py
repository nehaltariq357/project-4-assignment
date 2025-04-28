import random


def guess_the_number():
    random_number = random.randint(1,100)
    count = 0
    max_count = 7
    while count < max_count:
            try:
                user_input = int(input("Enter a number: "))
                count += 1
                if user_input < random_number:
                    print("Too Low!")
                    
                elif user_input > random_number:
                    print("Too High")
                    
                else:
                    print("Congratulations")
                    break
            except ValueError:
                print("Please enter a number")
    if user_input != random_number:
        print(f"Sorry! You've used all {max_count} attempts. The correct number was {random_number}")

guess_the_number()