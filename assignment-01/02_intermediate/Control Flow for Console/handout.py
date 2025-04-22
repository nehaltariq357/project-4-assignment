import random
#Milestone #1: Generate the random numbers
print("Welcome to the High-Low Game!")

computer_number = random.randint(1, 100)
user_number = random.randint(1,100)

print(f"The computer's number is {computer_number}")
print(f"Your number is {user_number}")

#Milestone #2: Get the user choice

user_input = input("Do you think your number is higher or lower than the computer's? ")

#Milestone #3: Write the game logic

if user_input == "higher":
    print(f"You were right! The computer's number was {computer_number}")
if user_input == "lower":
    print(f"You were right! The computer's number was {computer_number}")
if user_input == computer_number:
    print(f'computer win {computer_number}')


