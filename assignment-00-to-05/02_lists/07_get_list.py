def main():
    lst = []  # Make an empty list to store things in
    element = input("Enter a value: ") # Get an initial value
    while element: # While the user input isn't an empty value
        lst.append(element)  # Add element to list
        element = input("Enter a value: ") # Get the next element to add
    print("Here's the list:", lst)

if __name__ == '__main__':
    main()