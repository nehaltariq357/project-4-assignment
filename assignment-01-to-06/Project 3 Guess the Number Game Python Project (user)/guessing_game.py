
import random

def computer_guess():
    high = 100
    low = 1
    feedback = ""
    print("Think a number between 1 to 100 and computer will guess it!")

    while feedback != "c":
        if low <=high:
            guess = random.randint(low,high)
        else:
            print("Invalid state: low > high! Existing game.")
            break
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess +1
        elif feedback == "c":
            print(f" Yay! The computer guessed your number {guess} correctly!")
            return
        else:
            print("⚠ Invalid input! Please enter H, L, or C.")
    print("Game Over.")

computer_guess()