"""
    Create an empty list.
    Ask the user to input numbers and store them in a list. 
    Once they enter a blank line, break out of the loop and return the list.
    """

def get_user_number():
    user_number = []
    while True:
        user_input = int(input("Enter a number: "))

        if user_input == "":
            break

        user_number.append(user_input)

    return user_number

"""
    Create an empty dictionary.
    Loop over the list of numbers. 
    If the number is not in the dictionary, add it as a key with a value of 1.
    If the number is in the dictionary, increment its value by 1.
    """

def count_nums():
    num_dict = {}

    
    





