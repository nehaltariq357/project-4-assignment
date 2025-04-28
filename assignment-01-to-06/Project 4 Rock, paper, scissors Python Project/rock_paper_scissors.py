import random

def game():
    print("Welcome to Rock, Paper, Scissors!")
    choices = {"r": "rock", "s": "scissors", "p": "paper"}
    
    user_input = input("Enter r for rock, s for scissors, p for paper: ").lower()
    
    if user_input not in choices:
        print("⚠ Invalid input! Please enter only r, s, or p.")
        return
    
    computer_choice_key, computer_choice_value = random.choice(list(choices.items())) 
    print(f"Computer choose {computer_choice_value}.") 

    if user_input == computer_choice_key:
        print("It's a tie!")
    elif (user_input == "r" and computer_choice_key == "s") or \
        (user_input == "s" and computer_choice_key == "p") or \
        (user_input == "p" and computer_choice_key == "r"):
        print("You win!")
    else:
        print("You lose!")

game()
