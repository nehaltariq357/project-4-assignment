
import random

word_list = ["python", "java", "kotlin", "javascript"]

random_word = random.choice(word_list)
print(random_word)

guesses = ["*"] * len(random_word)
attempts = 3
while attempts !=0:
    print(f"Guess the word: {' '.join(guesses)}")

    # take user input for guessed letters
    user_input = input("Guess the letter: ").lower()

    if len(user_input) != 1 or not user_input.isalpha():
        print("Please enter a valid letter.")
        continue

    if user_input in random_word:
        print(f"{user_input} is in the word_list")
        #update the guess list
        
        for index,letter in enumerate(random_word):
            if letter == user_input:
                guesses[index] = user_input
    else:
        print(f"{user_input} is not in the word_list")
        attempts -=1
        if attempts >= 1:
            print(attempts, "left")
        else:
            print("game over no attempt left")
        
    
    if "*" not in guesses:
        print(f"Congratulation you guessed the word {random_word}")
        break