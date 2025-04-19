
def read_phone_numbers():
    phonebook = {}
    while True:
        name_input = input("Enter a name: ")
        if name_input == "":
            break
        number_input = input("Enter a number: ")

        phonebook[name_input] = number_input # name_input is used as a key in the dictionary

    return phonebook

def print_phonebook(phonebook):
    for name,number in phonebook.items():
        print(f"{name} : {number}")

def lookup_numbers(phonebook):
    while True:
        user_input_for_name = input("Enter a name to search number or press blank enter to exit: ")
        if user_input_for_name == "":
            break
        if user_input_for_name in phonebook:
            print(f"{user_input_for_name}: {phonebook[user_input_for_name]}")
        else:
            print("name is not in the phonebook")

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)
if __name__ == '__main__':
    main()