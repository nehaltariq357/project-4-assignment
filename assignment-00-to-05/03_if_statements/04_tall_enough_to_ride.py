MINIMUM_HEIGHT : int = 50 # arbitrary units :)

def main():
    while True:
        height_input = input("How tall are you: ")
        if height_input=="":
            print("Good bye!")
            break

        try:
            height = float(height_input)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")

        except ValueError:
            print("Please enter a valid number for height.")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()