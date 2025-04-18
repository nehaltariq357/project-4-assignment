
def print_one_digit(num):
    remainder = num % 10 # agr number 42 hoga, tw 42 % 10 hoga, means 2 is remainder , remiander print hoga
    print("The ones digit is", remainder)


def main():
    user_input = int(input("Enter a number: "))
    print_one_digit(user_input)
if __name__ == '__main__':
    main()