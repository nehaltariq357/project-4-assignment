
def read_phone_numbers():
    phonebook = {}
    while True:
        name_input = input("Enter a name: ")
        if name_input == "":
            break
        number_input = input("Enter a number: ")

        phonebook[name_input] = number_input # name_input is used as a key in the dictionary

    return phonebook

def print_phonebook():
    phonebook = read_phone_numbers()

    for name,number in phonebook.items():
        print(f"{name} : {number}")

    return phonebook

print_phonebook()