
import random
NUM_ROUNDS = 5
score = 0
#Milestone #1: Generate the random numbers
print("Welcome to the High-Low Game!")
# Milestone 4: Play multiple rounds
for i in range(NUM_ROUNDS):
    print(f"Round {i + 1}")

    computer_number = random.randint(1, 100)
    user_number = random.randint(1,100)
    #print(f"The computer's number is {computer_number}")
    print(f"Your number is {user_number}")

    #Milestone #2: Get the user choice

    user_input = input("Do you think your number is higher or lower than the computer's? ").lower()

    #Milestone #3: Write the game logic

    if user_number == computer_number:
        print("It's a tie! But computer win this case.")
    elif user_input == "higher":
        if user_number > computer_number:
            print(f"you were right! your number is {user_number} is higher than the computer's number {computer_number}.")
            score += 1
            
        else:
            print(f"Sorry, you were wrong. Your number {user_number} is not higher than the computer's number {computer_number}.")

    elif user_input == "lower":
        if user_number < computer_number:
            print(f"you were right! your number is {user_number} is lower than the computer number {computer_number}")
            score += 1
            
        else:
            print(f"Sorry, you were wrong. your number {user_number} is not lower than the computer number {computer_number}")
    else:
        print("Invalid input! Please type 'higher' or 'lower'.")
        #Milestone #5: Keep track of the score
    print(f"current score: {score}")
    print() # blank line between rounds
    
print(f"Game Over! Your final score was: {score} out of {NUM_ROUNDS}")
print() # blank line
if score == NUM_ROUNDS:
    print("Wow! You played perfectly!")
elif score >=NUM_ROUNDS // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")